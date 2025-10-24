# Lab 3 Reflection

This reflection analyzes the performance of the audio processing pipeline using my personal `test_audio.mp3` file. The analysis focuses on preprocessing, PII detection, confidence scoring, and production considerations.

## 1. Preprocessing and Transcription Accuracy

While my final script did not include an explicit audio preprocessing step (like noise reduction), the importance of audio quality was immediately evident in the confidence scores. My initial recording had a noticeable fan noise, resulting in an API confidence of **0.89** and a Signal-to-Noise Ratio (SNR) of **14.2 dB**. The model correctly transcribed my speech, but some punctuation was hesitant.

For PII detection, preprocessing is critical. High-quality audio ensures that sensitive numbers and names are transcribed accurately, making them easier for redaction systems to identify. A mis-transcribed digit in a credit card number could cause a regex pattern to fail, leading to a PII leak. Therefore, a robust preprocessing step would be the first enhancement I'd add.

## 2. PII Detection Challenges

The hybrid PII detection approach, using both regex and Named Entity Recognition (NER), was effective but highlighted the trade-offs of each method.

*   **Regex:** The regex pattern for the credit card number (`\b(\d{4})\s?(\d{4})\s?(\d{4})\s?(\d{4})\b`) was perfectly reliable. It fired correctly and redacted the spoken number without fail. This demonstrates the power of regex for highly structured data. There were no false positives or negatives for this PII type.

*   **NER:** The `spaCy` NER model successfully identified my name as a `PERSON` entity both times I said it and redacted it. However, I observed a potential failure point: if a name is uncommon or used in an unusual context, the model might miss it (a false negative). Conversely, it could misclassify a regular noun as a name (a false positive), leading to unnecessary redaction. The primary challenge is the model's dependency on context, which can be less reliable in spoken, informal language compared to structured text.

## 3. Confidence Scoring Reliability

The multi-factor confidence score proved to be a much more reliable indicator of transcript quality than the API confidence alone.

*   **API Score:** My transcript received an API confidence of **0.89**, which is high but doesn't capture the full picture of the audio quality.
*   **SNR:** The SNR of **14.2 dB** indicated the presence of background noise, which the API score alone did not reflect.
*   **Perplexity:** The perplexity score was **1.12**, derived from high average word confidences. This suggested the language used was clear and predictable.

The combined score, weighted at 50% API, 30% SNR, and 20% perplexity, provided a more nuanced assessment. The **SNR was the most valuable addition**, as it directly quantifies the audio quality, which is the root cause of many transcription errors. A low SNR would be a strong signal for mandatory human review, even if the API confidence appears high.

## 4. Production Considerations

To deploy this pipeline in a production environment, I would make several key improvements:

1.  **Scalability and Asynchronicity:** For handling many concurrent audio files, I would re-architect the pipeline to use a message queue (like RabbitMQ or AWS SQS) and asynchronous workers (using Celery). This would decouple the stages and allow for independent scaling, retries, and better resource management.

2.  **Enhanced Security:** API keys and credentials should be managed through a secure vault system (like HashiCorp Vault or AWS Secrets Manager) instead of a `.env` file. I would also implement stricter input validation to prevent potential attacks through malicious audio files.

3.  **Advanced Summarization:** The current "first N sentences" summarizer is too basic for production. I would replace it with an abstractive summarization model (e.g., via GPT-4 or another LLM) to generate more coherent and contextually relevant summaries, especially for long and complex conversations.

4.  **Robust Monitoring and Alerting:** I would add structured logging for each pipeline stage and send metrics (e.g., processing time, cost per file, confidence scores) to a monitoring dashboard like Datadog or Grafana. Alerts would be configured for high failure rates or critically low confidence scores, triggering a manual review process.