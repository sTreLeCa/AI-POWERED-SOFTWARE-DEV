# Lab 3 – Audio AI Pipeline

This lab guides you through building an audio processing pipeline using Google Cloud services. You will transcribe speech, evaluate confidence using multiple signals, redact personally identifiable information (PII), generate audio summaries and record what happened for auditing. The code here is intended as a starting point for your own experiments and the homework assignment described in LAB-3-HOMEWORK.md.

## Directory layout

- README.md – Overview and setup instructions.
- LAB-3-HOMEWORK.md – Homework specification and deadlines.
- requirements.txt – Python dependencies pinned to specific versions.
- .env.example – Template for Google Cloud credentials.
- audio_samples/ – Example audio files for lab exercises (contains .gitkeep placeholder).
- scripts/
  - 1_basic_stt.py – Transcription using Google Cloud Speech-to-Text.
  - 2_confidence_scoring.py – Multi-factor confidence analysis.
  - 3_pii_redaction.py – PII detection and redaction.
  - 4_tts_summary.py – Summarisation and text-to-speech.
  - verify.py – Diagnostic checks for your environment.
  - utils_audio.py – Audio utilities (resampling, SNR calculation).
  - utils_pii.py – PII utilities (number normalisation, Luhn, phone and NER).
- tools/make_submission_zip.py – Helper to package your homework submission.
- audio_pipeline.py – Optional full pipeline script for homework.

## Setup

Follow these steps to get the lab running on your machine:

1. Install Python 3.10 or newer.
2. Install FFmpeg. Librosa uses FFmpeg to decode MP3 files. On macOS run brew install ffmpeg. On Windows run choco install ffmpeg. On Debian/Ubuntu run sudo apt-get install ffmpeg.
3. Create a virtual environment and install dependencies. Run python -m venv .venv, activate it, pip install -r requirements.txt and python -m spacy download en_core_web_sm.
4. Authenticate with Google Cloud and enable APIs: gcloud auth application-default login and gcloud services enable speech.googleapis.com texttospeech.googleapis.com.
5. Configure environment variables. Copy .env.example to .env and edit the values needed for your credentials. Use a tool like python-dotenv or export variables in your shell.
6. Run diagnostic checks: python scripts/verify.py. The script reports on FFmpeg availability, API connectivity and spaCy model installation. If any checks fail, revisit the setup steps.

## Lab workflow

The lab is organised into four incremental steps, each in the scripts directory.

1. Basic speech-to-text – run 1_basic_stt.py to transcribe an audio file and inspect word-level confidence and timing information.
2. Confidence scoring – run 2_confidence_scoring.py to compute a composite confidence score based on the API’s reported confidence, the signal-to-noise ratio (SNR) calculated from the audio itself and the inverse of the average word confidence.
3. PII redaction – run 3_pii_redaction.py to detect and redact sensitive information such as credit card numbers, phone numbers, email addresses, names and dates.
4. Summarisation and TTS – run 4_tts_summary.py to summarise a transcript and convert the summary back to audio using Text-to-Speech.

When running these scripts, pass the path to an audio file in the audio_samples directory. If you do not have the example audio files, create your own recordings in WAV format and place them in audio_samples.

## Homework

Assemble the above components into a single pipeline, record your own audio and analyse the results. See LAB-3-HOMEWORK.md for the full specification, rubric and due dates. Use tools/make_submission_zip.py to package your submission.

## Deadlines

Please note the following deadlines (Asia/Tbilisi timezone):

- Homework submission: Wednesday, 22 October 2025 at 23:59.
- Quiz on Weeks 1–4: Thursday, 23 October 2025.
- Design Review submission: Friday, 24 October 2025.

Late submissions are not accepted without prior approval. If you encounter issues with the setup or APIs, contact the instructor as soon as possible.
