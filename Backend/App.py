from flask import Flask, request, jsonify
from flask_cors import CORS
from googleapiclient.discovery import build
from textblob import TextBlob
from dotenv import load_dotenv
import os

# Load environment variables from the .env.local file
load_dotenv('.env.local')

app = Flask(__name__)
CORS(app)

# YouTube API setup
YOUTUBE_API_KEY = os.getenv('YOUTUBE_API_KEY')
youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)

def get_sentiment_emoji(sentiment_score):
    if sentiment_score > 0.5:
        return '😃'
    elif sentiment_score > 0:
        return '🙂'
    elif sentiment_score == 0:
        return '😐'
    elif sentiment_score > -0.5:
        return '😟'
    else:
        return '😡'

@app.route('/comments', methods=['GET'])
def get_comments():
    video_id = request.args.get('videoId')
    response = youtube.commentThreads().list(part='snippet', videoId=video_id, textFormat='plainText').execute()
    comments = [item['snippet']['topLevelComment']['snippet']['textDisplay'] for item in response['items']]

    analysis = [{
        'comment': comment,
        'sentiment': TextBlob(comment).sentiment.polarity,
        'emoji': get_sentiment_emoji(TextBlob(comment).sentiment.polarity)
    } for comment in comments]
    
    avg_sentiment = sum([comment['sentiment'] for comment in analysis]) / len(analysis) if analysis else 0

    return jsonify({
        'analysis': analysis,
        'avg_sentiment': avg_sentiment,
        'emoji': get_sentiment_emoji(avg_sentiment)
    })

if __name__ == '__main__':
    app.run(debug=True)
