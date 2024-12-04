from flask import Blueprint, jsonify, request
from app.utils.news_fetcher import fetch_news
from app.utils.news_fetcher import fetch_news_with_summaries, fetch_article_content, summarize_text

news_bp = Blueprint("news", __name__)

@news_bp.route("/news", methods=["GET"])
def get_news():
    category = request.args.get("category", "general")
    country = request.args.get("country", "us")
    page_size = int(request.args.get("page_size", 10))

    news_data = fetch_news_with_summaries(category, country, page_size)
    return jsonify(news_data)

@news_bp.route("/news/summary", methods=["GET"])
def get_article_summary():
    """
    Endpoint to fetch the summary for a specific article.
    Expects the `article_url` query parameter.
    """
    article_url = request.args.get("article_url")
    if not article_url:
        return jsonify({"status": "error", "message": "Missing article URL"}), 400

    try:
        # Fetch article content based on URL (mock implementation)
        # In a real setup, you might need to scrape the article's text or store it earlier.
        article_content = fetch_article_content(article_url)  # Placeholder function
        if not article_content:
            return jsonify({"status": "error", "message": "Article content not found"}), 404

        # Generate the summary
        summary = summarize_text(article_content)
        return jsonify({"status": "ok", "summary": summary})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500
    

