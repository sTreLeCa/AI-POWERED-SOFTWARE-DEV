from google.cloud import speech
import sys


def transcribe_audio(audio_file_path):
    """Transcribe audio using Google Cloud Speech-to-Text"""
    # Initialize client (uses Application Default Credentials)
    client = speech.SpeechClient()

    # Read audio file
    with open(audio_file_path, 'rb') as audio_file:
        content = audio_file.read()

    # Configure audio settings
    audio = speech.RecognitionAudio(content=content)

    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.MP3,
        sample_rate_hertz=16000,
        language_code="en-US",
        enable_word_time_offsets=True,        # Word-level timestamps
        enable_automatic_punctuation=True,     # Add punctuation
        enable_word_confidence=True,           # Word-level confidence
        model="latest_long",                   # Best accuracy model
    )

    # Perform transcription
    print(f"Transcribing: {audio_file_path}...")
    response = client.recognize(config=config, audio=audio)

    # Extract results
    for result in response.results:
        alternative = result.alternatives[0]
        print(f"\nTranscript: {alternative.transcript}")
        print(f"Confidence: {alternative.confidence:.2f}")

        # Word-level details
        print("\nWord-level details:")
        for word_info in alternative.words:
            word = word_info.word
            confidence = word_info.confidence
            start_time = word_info.start_time.total_seconds()
            end_time = word_info.end_time.total_seconds()

            print(f"  {word}: {confidence:.2f} [{start_time:.2f}s - {end_time:.2f}s]")

    return response


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python 1_basic_stt.py <audio_file>")
        sys.exit(1)

    transcribe_audio(sys.argv[1])
