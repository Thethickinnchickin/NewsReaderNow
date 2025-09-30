from flask import Flask
from flask_cors import CORS
import nltk

nltk.download('punkt_tab')

def create_app():
    app = Flask(__name__)

    from .routes import news_bp
    app.register_blueprint(news_bp, url_prefix="/api")

    CORS(app, supports_credentials=True, resources={r"/api/*": {
        "origins": [
            "https://news-reader-now.vercel.app",
            "http://localhost:3000"
        ]
    }})

    return app
