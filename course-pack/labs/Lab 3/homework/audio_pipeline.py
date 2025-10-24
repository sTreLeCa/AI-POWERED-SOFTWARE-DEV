import os
from datetime import datetime, timezone
import json
import sys
import re
import argparse
import traceback
from typing import Tuple, List, Dict, Any

# Third-party libraries
from dotenv import load_dotenv
from google.cloud import speech, texttospeech
import librosa
import numpy as np
import spacy

# Load the spaCy model for Named Entity Recognition (NER)
try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    print("Downloading 'en_core_web_sm' model for spaCy. This may take a moment...")
    spacy.cli.download("en_core_web_sm")
    nlp = spacy.load("en_core_web_sm")

def load_env(env_path: str = ".env") -> None:
    """Load environment variables from the given path."""
    load_dotenv(dotenv_path=env_path)

def transcribe_audio(audio_path: str) -> Tuple[str, List[Dict[str, Any]], float]:
    """Transcribe audio using Google Cloud Speech-to-Text."""
    print(f"Step 1: Transcribing audio file: {audio_path}")
    client = speech.SpeechClient()

    with open(audio_path, "rb") as audio_file:
        content = audio_file.read()

    audio = speech.RecognitionAudio(content=content)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.MP3,
        language_code="en-US",
        enable_automatic_punctuation=True,
        enable_word_confidence=True,
    )
    response = client.recognize(config=config, audio=audio)

    if not response.results:
        raise ValueError("No speech detected in the audio.")

    result = response.results[0]
    alternative = result.alternatives[0]
    transcript = alternative.transcript
    words = [{"word": word_info.word, "confidence": word_info.confidence} for word_info in alternative.words]
    api_confidence = alternative.confidence
    print("   -> Transcription successful.")
    return transcript, words, api_confidence

def calculate_snr(audio_path: str) -> float:
    """Compute the signal-to-noise ratio (SNR) of the audio."""
    try:
        y, sr = librosa.load(audio_path, sr=None)
        signal_power = np.mean(y**2)
        noise_power = np.var(y)
        if noise_power == 0: return float('inf')
        return 10 * np.log10(signal_power / noise_power)
    except Exception:
        return 0.0

def calculate_perplexity(word_confidences: List[float]) -> float:
    """Compute a perplexity-like metric from a list of word confidences."""
    valid_confidences = [conf for conf in word_confidences if conf > 0]
    if not valid_confidences: return float("inf")
    average_confidence = sum(valid_confidences) / len(valid_confidences)
    return 1.0 / average_confidence

def multi_factor_confidence(api_confidence: float, snr: float, perplexity: float) -> Tuple[float, str]:
    """Combine multiple confidence factors into a single score and label."""
    print("Step 2: Calculating multi-factor confidence score...")
    snr_normalized = min(max((snr - 10) / 20, 0), 1)
    perplexity_normalized = max(1 - (perplexity - 1.0) * 2, 0)
    combined_score = (0.5 * api_confidence + 0.3 * snr_normalized + 0.2 * perplexity_normalized)
    
    if combined_score > 0.85: level = "HIGH"
    elif combined_score > 0.70: level = "MEDIUM"
    else: level = "LOW"

    print(f"   -> API Confidence: {api_confidence:.2f}, SNR: {snr:.2f}dB, Perplexity: {perplexity:.2f}")
    print(f"   -> Combined Confidence Score: {combined_score:.2f} ({level})")
    return combined_score, level

def redact_pii(text: str) -> Tuple[str, List[Dict[str, str]]]:
    """Redact personally identifiable information from the transcript."""
    print("Step 3: Redacting PII from transcript...")
    redacted_text = text
    redactions = []
    cc_pattern = r'\b(\d{4})\s?(\d{4})\s?(\d{4})\s?(\d{4})\b'
    
    # NER for person names
    doc = nlp(text)
    temp_text = list(text)
    for ent in reversed(doc.ents):
        if ent.label_ == 'PERSON':
            temp_text[ent.start_char:ent.end_char] = list('[REDACTED_PERSON]')
            redactions.append({'type': 'PERSON', 'original': ent.text})

    redacted_text = "".join(temp_text)
    
    # Re-run regex on the original text to log the redaction
    for match in re.finditer(cc_pattern, text):
        redactions.append({'type': 'CREDIT_CARD', 'original': match.group(0)})
    
    # Final regex pass to ensure all CCs are redacted in the final text
    redacted_text = re.sub(cc_pattern, '[REDACTED_CREDIT_CARD]', redacted_text)

    print(f"   -> PII Redaction complete. Found {len(redactions)} items.")
    return redacted_text, redactions

def summarize_text(text: str) -> str:
    """Create a short summary of the transcript."""
    print("Step 4: Generating summary...")
    sentences = re.split(r'(?<=[.!?])\s+', text)
    summary = " ".join(sentences[:2]).strip()
    if not summary: return "No summary could be generated."
    print("   -> Summary generated.")
    return summary

def synthesize_speech(text: str, output_path: str) -> str:
    """Generate speech audio from text using Google Cloud Text-to-Speech."""
    print(f"Step 5: Synthesizing summary to audio file: {output_path}")
    client = texttospeech.TextToSpeechClient()
    synthesis_input = texttospeech.SynthesisInput(text=text)
    voice = texttospeech.VoiceSelectionParams(language_code="en-US", name="en-US-Neural2-A")
    audio_config = texttospeech.AudioConfig(audio_encoding=texttospeech.AudioEncoding.MP3)
    response = client.synthesize_speech(input=synthesis_input, voice=voice, audio_config=audio_config)

    with open(output_path, "wb") as out:
        out.write(response.audio_content)
    
    print("   -> Audio summary synthesis successful.")
    return output_path

def write_audit_log(log_data: Dict[str, Any], log_path: str) -> None:
    """Write a structured audit log to disk in JSON Lines format (NumPy-safe)."""
    import numpy as np

    def np_encoder(obj):
        if isinstance(obj, (np.integer,)):
            return int(obj)
        elif isinstance(obj, (np.floating,)):
            return float(obj)
        elif isinstance(obj, (np.ndarray,)):
            return obj.tolist()
        return str(obj)

    with open(log_path, "a", encoding="utf-8") as f:
        f.write(json.dumps(log_data, default=np_encoder) + "\n")

    print(f"   -> Audit log updated: {log_path}")


def main(args):
    """Main entry point for the pipeline."""
    load_dotenv()
    
    # ----- START OF FIX 2: CONVERT PATH AND FIX DEPRECATION WARNING -----
    # Convert the input path to an absolute path to resolve any ambiguity.
    absolute_input_path = os.path.abspath(args.input_file)
    # Use timezone-aware datetime objects.
    start_time = datetime.now(timezone.utc)
    # ----- END OF FIX 2 -----

    print("\n--- Starting Audio Processing Pipeline ---")
    try:
        # Use the absolute path for all file operations
        transcript, words, api_conf = transcribe_audio(absolute_input_path)
        word_confidences = [w.get("confidence", 0.0) for w in words]
        snr = calculate_snr(absolute_input_path)
        perplexity = calculate_perplexity(word_confidences)
        combined_score, level = multi_factor_confidence(api_conf, snr, perplexity)
        redacted_text, redactions = redact_pii(transcript)
        summary = summarize_text(redacted_text)
        summary_audio_path = "output_summary.mp3"
        synthesize_speech(summary, summary_audio_path)
        
        print("Step 6: Writing final output files...")
        with open("output_transcript.txt", "w", encoding="utf-8") as f:
            f.write(redacted_text)
        
        end_time = datetime.now(timezone.utc)
        log_data = {
            "timestamp_utc": start_time.isoformat(),
            "run_duration_seconds": (end_time - start_time).total_seconds(),
            "input_file": os.path.basename(absolute_input_path),
            "confidence_metrics": { "api_confidence": api_conf, "snr_db": snr, "perplexity": perplexity, "combined_score": combined_score, "confidence_level": level },
            "pii_redaction": { "count": len(redactions), "items": redactions },
            "outputs": { "transcript_file": "output_transcript.txt", "summary_audio_file": summary_audio_path, "log_file": "audit.log" },
            "status": "SUCCESS"
        }
        write_audit_log(log_data, "audit.log")

        print("\n--- Pipeline Finished Successfully! ---")
        print("Check the current directory for your output files.")

    except Exception as e:
        import traceback
        print("\n--- PIPELINE FAILED ---")
        print("Error type:", type(e))
        print("Error message:", str(e))
        traceback.print_exc()

        print(f"\n--- PIPELINE FAILED: {e} ---")
        end_time = datetime.now(timezone.utc)
        log_data = { 
            "timestamp_utc": start_time.isoformat(), 
            "run_duration_seconds": (end_time - start_time).total_seconds(), 
            "input_file": os.path.basename(absolute_input_path), 
            "status": "FAILURE", 
            "error_message": str(e) 
        }
        write_audit_log(log_data, "audit.log")
        sys.exit(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process an audio file through the AI pipeline.")
    parser.add_argument("input_file", type=str, help="The path to the input audio file (e.g., test_audio.mp3).")
    
    if len(sys.argv) < 2:
        parser.print_help()
        sys.exit(1)
        
    args = parser.parse_args()
    main(args)