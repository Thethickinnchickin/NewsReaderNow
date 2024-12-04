import os
import requests
from dotenv import load_dotenv
from transformers import pipeline
import requests

# Load environment variables
load_dotenv()

NEWS_API_KEY = os.getenv("NEWS_API_KEY")
NEWS_API_URL = "https://newsapi.org/v2/top-headlines"
# Load the summarization model
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def fetch_news(category="general", country="us", page_size=10):
    try:
        params = {
            "apiKey": NEWS_API_KEY,
            "category": category,
            "country": country,
            "pageSize": page_size,
        }
        response = requests.get(NEWS_API_URL, params=params)
        response.raise_for_status()
        articles = response.json().get("articles", [])
        
        # Extract only required fields
        simplified_articles = [
            {
                "title": article["title"],
                "description": article["description"],
                "url": article["url"],
                "urlToImage": article["urlToImage"],
                "publishedAt": article["publishedAt"],
                "source": article["source"]["name"],
            }
            for article in articles
        ]
        return {"status": "ok", "articles": simplified_articles}
    except requests.exceptions.RequestException as e:
        return {"status": "error", "message": str(e)}

def summarize_text(text):
    """
    Summarize a given text using Hugging Face's BART model.

    Args:
        text (str): The text to summarize.

    Returns:
        str: The summarized text.
    """
    try:
        # Define dynamic max_length and min_length
        input_length = len(text.split())
        max_length = min(130, input_length - 1)  # Ensure max_length is less than input length
        min_length = max(30, max_length // 2)    # Minimum length should be a fraction of max_length

        if input_length < 20:  # For very short texts, return the original text
            return text

        summary = summarizer(
            text,
            max_length=max_length,
            min_length=min_length,
            do_sample=False
        )
        return summary[0]["summary_text"]
    except Exception as e:
        return "Error in summarization: " + str(e)

def fetch_news_with_summaries(category="general", country="us", page_size=10):
    """
    Fetch top headlines without generating summaries.

    Args:
        category (str): News category.
        country (str): Country code.
        page_size (int): Number of articles.

    Returns:
        dict: Simplified news articles.
    """
    try:
        params = {
            "apiKey": NEWS_API_KEY,
            "category": category,
            "country": country,
            "pageSize": page_size,
        }
        response = requests.get(NEWS_API_URL, params=params)
        response.raise_for_status()
        articles = response.json().get("articles", [])

        # Simplify articles (no summaries)
        simplified_articles = [
            {
                "title": article["title"],
                "description": article["description"],
                "url": article["url"],
                "urlToImage": article["urlToImage"],
                "publishedAt": article["publishedAt"],
                "source": article["source"]["name"],
            }
            for article in articles
        ]

        return {"status": "ok", "articles": simplified_articles}
    except requests.exceptions.RequestException as e:
        return {"status": "error", "message": str(e)}


def fetch_article_content(article_url):
    """
    Fetch the article content from a given URL.

    Args:
        article_url (str): URL of the article.

    Returns:
        str: Content of the article or None if fetching fails.
    """
    try:
        # Example: Scrape or fetch content from the URL (simplified logic)
        response = requests.get(article_url)
        response.raise_for_status()

        # This is a mock implementation. Replace with actual scraping/parsing logic.
        content = response.text[:1000]  # Only take a portion to mimic content fetching
        return content
    except requests.RequestException:
        return None
