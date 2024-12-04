from flask import Flask
from app.routes import news_bp

app = Flask(__name__)
app.register_blueprint(news_bp, url_prefix="/api")

if __name__ == "__main__":
    app.run(debug=True)

