from flask import Blueprint, jsonify, request
from app.utils.news_fetcher import fetch_news_with_summaries, fetch_article_content, summarize_text
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_cors import cross_origin
# from app import cache  # Now import the cache object initialized in app/__init__.py

# Blueprint setup
news_bp = Blueprint("news", __name__)

# Flask-Limiter setup
limiter = Limiter(get_remote_address)

# Optimized endpoints

@news_bp.route("/news", methods=["OPTIONS", "GET"])
# @cache.cached(timeout=300, query_string=True)  # Cache responses for 5 minutes
@limiter.limit("10 per minute")  # Limit requests to 10 per minute per user
@cross_origin(origin='https://news-reader-now.vercel.app', methods=["GET", "OPTIONS"])
def get_news():
    """
    Fetch news articles with summaries based on category and country.
    Caches the response and limits the rate of requests.
    """
    category = request.args.get("category", "general")
    country = request.args.get("country", "us")
    page_size = int(request.args.get("page_size", 10))

    try:
        news_data = fetch_news_with_summaries(category, country, page_size)
        return jsonify(news_data), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500


@news_bp.route("/news/summary", methods=["GET"])
@limiter.limit("5 per minute")  # Limit requests to 5 per minute per user
def get_article_summary():
    """
    Fetch or generate a summary for a specific article.
    Leverages caching to avoid re-computation for the same article URL.
    """
    article_url = request.args.get("article_url")
    if not article_url:
        return jsonify({"status": "error", "message": "Missing article URL"}), 400

    try:
        # Check for cached summary
        # cached_summary = cache.get(article_url)
        # if cached_summary:
        #     return jsonify({"status": "ok", "summary": cached_summary}), 200

        # Fetch article content
        article_content = fetch_article_content(article_url)
        if not article_content:
            return jsonify({"status": "error", "message": "Article content not found"}), 404

        # Generate summary
        summary = summarize_text(article_content)
        cache.set(article_url, summary, timeout=600)  # Cache summary for 10 minutes
        return jsonify({"status": "ok", "summary": summary}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500
