import os
import requests
from dotenv import load_dotenv
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
import numpy as np
from nltk.tokenize import sent_tokenize
import nltk
from bs4 import BeautifulSoup
nltk.download("punkt")

# Load environment variables
load_dotenv()

NEWS_API_KEY = os.getenv("NEWS_API_KEY")
NEWS_API_URL = "https://newsapi.org/v2/top-headlines"

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

def clean_html(text):
    """
    Remove HTML tags from the text using BeautifulSoup.
    """
    return BeautifulSoup(text, "html.parser").get_text()

def summarize_text(text, n_clusters=3):
    """
    Summarize a given text using Scikit-learn's TF-IDF and KMeans.

    Args:
        text (str): The text to summarize.
        n_clusters (int): Number of sentences to include in the summary.

    Returns:
        str: The summarized text.
    """
    try:
        # Clean the text to remove HTML tags
        text = clean_html(text)

        # Tokenize text into sentences
        sentences = sent_tokenize(text)
        if len(sentences) <= n_clusters:
            return text  # If too few sentences, return original text

        # Convert sentences to TF-IDF feature matrix
        vectorizer = TfidfVectorizer(stop_words="english")
        X = vectorizer.fit_transform(sentences)

        # Apply KMeans clustering
        kmeans = KMeans(n_clusters=n_clusters, random_state=0)
        kmeans.fit(X)

        # Identify representative sentences for each cluster
        representative_sentences = []
        for cluster_id in range(n_clusters):
            cluster_indices = np.where(kmeans.labels_ == cluster_id)[0]
            cluster_center = kmeans.cluster_centers_[cluster_id]
            closest_idx = min(
                cluster_indices, 
                key=lambda idx: np.linalg.norm(X[idx].toarray() - cluster_center)
            )
            representative_sentences.append(sentences[closest_idx])

        # Return the summary in order of original text
        summary = " ".join(sorted(representative_sentences, key=sentences.index))
        print(summary)
        return summary
    except Exception as e:
        print(f"Error in summarization: {e}")
        return "Error in summarization."
    
def fetch_news_with_summaries(category="general", country="us", page_size=10):
    """
    Fetch top headlines and generate summaries.

    Args:
        category (str): News category.
        country (str): Country code.
        page_size (int): Number of articles.

    Returns:
        dict: Simplified news articles with summaries.
    """
    news = fetch_news(category, country, page_size)
    if news["status"] == "ok":
        for article in news["articles"]:
            content = fetch_article_content(article["url"])
            if content:
                article["summary"] = summarize_text(content)
            else:
                article["summary"] = "Summary not available."
    return news

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
        content = response.text  # Only take a portion to mimic content fetching
        summary = summarize_text(content)
        return summary
    except requests.RequestException:
        return None
