# YouTube Comments Sentiment Analyzer

This project is a simple Flask web application that analyzes YouTube video comments' sentiments using TextBlob. The app fetches comments from a given YouTube video, analyzes their sentiments, and returns a sentiment score along with an emoji representation of the sentiment.

## Features

- Fetches comments from a YouTube video using the YouTube Data API.
- Analyzes sentiment using TextBlob.
- Provides a sentiment score and an emoji representation.
- Supports Cross-Origin Resource Sharing (CORS).

## Requirements

- Python 3.x
- Flask
- Flask-CORS
- Google API Python Client (`googleapiclient`)
- TextBlob

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

### 2. Set Up Environment Variables

Create a `.env.local` file in the same directory as `App.py`, and add your YouTube API key like this:

```bash
YOUTUBE_API_KEY=your_youtube_api_key_here
```

Make sure that `.env.local` is added to `.gitignore` to avoid pushing sensitive information.

### 3. Install Dependencies

First, create a virtual environment and activate it:

```bash
# For Windows
python -m venv venv
venv\Scripts\activate

# For macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

Then install the required packages:

```bash
pip install -r requirements.txt
```

### 4. Run the Application

To run the Flask app, execute the following command:

```bash
python App.py
```

The app will be available at [http://127.0.0.1:5000](http://127.0.0.1:5000).

### 5. API Endpoints

- **GET /comments**: Fetches YouTube comments and returns the sentiment analysis.
  
  **Parameters**:
  - `videoId`: The ID of the YouTube video you want to analyze.
  
  **Example**:
  ```
  http://127.0.0.1:5000/comments?videoId=YOUR_VIDEO_ID
  ```

  **Response**:
  ```json
  {
    "analysis": [
      {
        "comment": "This is a great video!",
        "sentiment": 0.8,
        "emoji": "😃"
      }
    ],
    "avg_sentiment": 0.8,
    "emoji": "😃"
  }
  ```

## Project Structure

```bash
.
├── App.py                  # Main Flask application
├── requirements.txt        # Python dependencies
├── .env.local              # Environment variables (YouTube API key)
├── .gitignore              # Git ignore file
└── README.md               # This readme file
```

## How It Works

1. **YouTube API**: The app uses the YouTube Data API to fetch comments for a given video ID.
2. **Sentiment Analysis**: Comments are analyzed using TextBlob's polarity feature. The sentiment score ranges from -1 (negative) to 1 (positive).
3. **Emoji Representation**: The sentiment score is converted into an emoji for better visual representation.

## Environment Variables

This project uses a `.env.local` file to store sensitive API keys. Add your API key like so:

```bash
YOUTUBE_API_KEY=your_youtube_api_key_here
```

## To-Do

- Add more advanced sentiment analysis using other libraries.
- Improve error handling.
- Add support for replies to comments.

## Contributing

Contributions are welcome! Feel free to fork this project and submit a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

