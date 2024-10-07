from flask import Flask, render_template, request
from textblob import TextBlob

app = Flask(__name__)

def analyze_sentiment(text):
    analysis = TextBlob(text)
    return analysis.sentiment.polarity  # Returns a score between -1 and 1

@app.route("/", methods=["GET", "POST"])
def home():
    sentiment_score = None
    if request.method == "POST":
        user_input = request.form["text"]
        sentiment_score = analyze_sentiment(user_input)
        if sentiment_score > 0:
            sentiment_label = "Positive"
        elif sentiment_score < 0:
            sentiment_label = "Negative"
        else:
            sentiment_label = "Neutral"
        return render_template("index.html", sentiment_label=sentiment_label, user_input=user_input)
    return render_template("index.html", sentiment_label=None)

if __name__ == "__main__":
    app.run(debug=True)
