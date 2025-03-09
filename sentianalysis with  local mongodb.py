from pymongo import MongoClient
from datetime import datetime
from bson import ObjectId  # To handle MongoDB ObjectIds
from transformers import pipeline

# Connect to local MongoDB7q

client = MongoClient("mongodb://localhost:27017/")

# Select database and collection
db = client["alumni_database"]
collection = db["messages"]

# Load BERT sentiment analysis model
sentiment_pipeline = pipeline("sentiment-analysis", model="nlptown/bert-base-multilingual-uncased-sentiment")


# Function to analyze sentiment
def analyze_sentiment(text):
    try:
        result = sentiment_pipeline(text)
        label = result[0]['label']  # Example: '5 stars', '1 star'

        sentiment_map = {
            "1 star": "Very Negative",
            "2 stars": "Negative",
            "3 stars": "Neutral",
            "4 stars": "Positive",
            "5 stars": "Very Positive"
        }
        return sentiment_map.get(label, "Neutral")
    except Exception as e:
        return f"Error in sentiment analysis: {str(e)}"


# Fetch messages, sorted by timestamp (latest first)
for record in collection.find({}, {"_id": 1, "sender": 1, "content": 1, "timestamp": 1}).sort("timestamp", -1):
    message_id = str(record.get("_id", "N/A"))  # Convert ObjectId to string
    sender_id = str(record.get("sender", "Unknown"))  # Convert ObjectId if necessary
    content = record.get("content", "[No content]")
    timestamp = record.get("timestamp", "[No timestamp]")

    sentiment = analyze_sentiment(content)  # Sentiment analysis

    print(f"Message ID: {message_id}")
    print(f"Sender ID: {sender_id}")
    print(f"Content: {content}")
    print(f"Sentiment: {sentiment}")
    print(f"Timestamp: {timestamp}\n")

# Close Connection
client.close()
