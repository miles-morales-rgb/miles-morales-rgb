from flask import Flask, request, jsonify
from textblob import TextBlob
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/sentiment', methods=['POST'])
def sentiment():
    data = request.json
    text = data.get("text", "")
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    result = "Positive" if polarity > 0 else "Negative" if polarity < 0 else "Neutral"
    return jsonify({"result": result, "polarity": polarity})

if __name__ == "__main__":
    app.run(debug=True)
