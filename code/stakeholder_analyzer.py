
from textblob import TextBlob

def analyze_sentiment(text):
    analysis = TextBlob(text)
    return analysis.sentiment.polarity

if __name__ == "__main__":
    feedback = "The AI project is promising but stakeholders are concerned about privacy."
    print({"sentiment_score": analyze_sentiment(feedback)})
