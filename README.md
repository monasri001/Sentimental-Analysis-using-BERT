# Sentiment Analysis on MongoDB Messages

## 📌 Overview
This project connects to a MongoDB database, retrieves messages, and performs sentiment analysis using a pre-trained BERT model. The analyzed messages are displayed along with their respective sentiments.

## ✨ Features
- ✅ Connects to a local MongoDB database (`alumni_database`).
- ✅ Retrieves messages from the `messages` collection.
- ✅ Analyzes sentiment using the `nlptown/bert-base-multilingual-uncased-sentiment` model.
- ✅ Sorts messages by timestamp in descending order.
- ✅ Outputs the message details along with sentiment classification.

## Sentiment Mapping
Stars	Sentiment
⭐	Very Negative
⭐⭐	Negative
⭐⭐⭐	Neutral
⭐⭐⭐⭐	Positive
⭐⭐⭐⭐⭐	Very Positive

## ⚠️ Error Handling
- If sentiment analysis fails, an error message is displayed instead of the sentiment label.
- If fields are missing in MongoDB documents, they are replaced with placeholder values.

## 📋 Prerequisites
Make sure you have the following installed before running the script:

- Python 3.8+
- MongoDB installed and running locally
- Required Python libraries:
  ```sh
  pip install pymongo torch transformers

## Usage
Ensure MongoDB is running.
-Run the script:
  ```sh
    python sentimentanalysis.py





