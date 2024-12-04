from flask import Flask
from flask_caching import Cache
from flask_cors import CORS

# Initialize the Flask app and Cache
app = Flask(__name__)

CORS(app, origins=["https://news-reader-now.vercel.app"])


app.config['CACHE_TYPE'] = 'simple'  # You can choose 'simple', 'redis', 'filesystem', etc.
app.config['CACHE_DEFAULT_TIMEOUT'] = 300  # Set your cache timeout, in seconds

# Initialize cache with the app
cache = Cache(app)

def create_app():
    # You can initialize more app configurations here if needed
    from .routes import news_bp  # Import the blueprint here
    app.register_blueprint(news_bp, url_prefix="/api")
    return app