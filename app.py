from flask import Flask, request, jsonify
from textblob import TextBlob

app = Flask(__name__)


@app.route('/analyze_sentiment', methods=['POST'])
def analyze_sentiment():
    data = request.get_json()
    text = data.get('text', '')
    if not text:
        return jsonify({"error": "No text provided"}), 400
    blob = TextBlob(text)
    sentiment_score = blob.sentiment.polarity
    sentiment_label = 'Neutral'
    if sentiment_score > 0:
        sentiment_label = 'Positive'
    elif sentiment_score < 0:
        sentiment_label = 'Negative'
    result = {"sentiment": sentiment_label, "score": sentiment_score}
    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)
