# Lab 3: Audio AI Pipeline



This repository accompanies **Lab 3** for the AI‑powered software development course.  In this lab you will build a complete audio processing pipeline that:



1. Preprocesses an input recording (normalisation and noise removal).

2. Transcribes the recording using Google Cloud Speech‑to‑Text.

3. Computes a multi‑factor confidence score combining API confidence, signal‑to‑noise ratio and language perplexity.

4. Redacts sensitive personal information (PII) from the transcript using both regular expressions and named‑entity recognition.

5. Generates a short text summary and converts it back to audio using Google Cloud Text‑to‑Speech.

6. Writes a structured audit log of every step.



## Due date



This lab is assigned on **17 October 2025** and is due **24 October 2025 23:59** (Georgia time).  Late submissions may receive a penalty.  Submit your solution through the learning management system.



## Getting started



Clone or download this repository to your local machine.  The directory structure is as follows:



```

lab-3/

├── README.md               – this file

├── .env.example            – example environment configuration

├── docs/

│   └── google_cloud_setup.md  – guide for setting up your Google Cloud account

├── starter_code/

│   ├── audio_pipeline.py   – template for the assignment

│   └── requirements.txt    – Python dependencies

├── scripts/

│ │   ├── 1_basic_stt.py – basic transcription example used in the lab
│   ├── 2_confidence_scoring.py – multi-factor confidence scoring example
│   ├── 3_pii_redaction.py – PII redaction example with regex and NER
│   ├── 4_tts_summary.py – summary generation and TTS example
  └── test_setup.py       – script to verify your environment

└── audio_samples/

    ├── clean_speech.mp3    – simple test recording

    ├── noisy_background.mp3

    ├── contains_credit_card.mp3

    ├── fast_speech.mp3

    ├── low_quality_phone.mp3

    └── students/

        └── test_audio_[YOUR_NAME].mp3 – personalised input for your homework

```
Note: The `scripts` folder contains example scripts used during the lab session (1_basic_stt.py, 2_confidence_scoring.py, 3_pii_redaction.py and 4_tts_summary.py). These scripts illustrate individual steps of the pipeline and are provided for reference only; they are not required as part of your homework submission.




Use `python3 -m venv venv` to create a virtual environment and run `pip install -r starter_code/requirements.txt` inside it.  See `docs/google_cloud_setup.md` for instructions on authenticating with Google Cloud and enabling the required APIs.



### Running the environment check



Run the provided setup script to verify that your machine is ready for the lab:



```bash

python scripts/test_setup.py

```



The script will check for Google Cloud authentication, enabled APIs and installed packages.  Fix any errors before you proceed.



## Assignment tasks



Implement the audio processing pipeline in `starter_code/audio_pipeline.py`.  Each section of the file includes `TODO` comments describing what you need to implement.  At a minimum your pipeline must:



- Normalise audio levels and reduce background noise.

- Transcribe speech using Google Cloud Speech‑to‑Text with word‑level confidence and timestamps.

- Compute a combined confidence score from the API score, the signal‑to‑noise ratio and a simple perplexity measure of the transcript.

- Redact credit cards, social security numbers, phone numbers, emails, personal names and dates.

- Create a concise summary (two or three sentences) from the transcript and convert it to speech using Google Cloud Text‑to‑Speech.

- Log every step and any redactions to a JSONL log file called `audit.log`.



You should test your pipeline with the sample files in `audio_samples/`, starting with `clean_speech.mp3` and gradually using the noisier examples.  For your final submission you must process your personalised audio file from the `audio_samples/students/` folder and include the generated transcript, summary audio file and audit log.



## Deliverables



Submit the following files in a directory called `homework`:



1. `audio_pipeline.py` – your completed pipeline.

2. `requirements.txt` – list of all Python dependencies.

3. `test_audio.mp3` – your personalised input file.

4. `output_transcript.txt` – redacted transcript from your pipeline.

5. `output_summary.mp3` – generated audio summary.

6. `audit.log` – JSONL file containing the audit trail.

7. `reflection.md` – a 300‑word reflection answering the questions listed in the homework specification.



See the course LMS for submission instructions.



## Support



If you encounter problems with setup or the assignment, consult the troubleshooting section in `docs/google_cloud_setup.md` and the `scripts/test_setup.py` script.  For further help post in the course forum or attend office hours.
