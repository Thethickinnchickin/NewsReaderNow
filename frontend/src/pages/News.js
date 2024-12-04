import React, { useEffect, useState } from 'react';
import axios from 'axios';

const News = () => {
    const [articles, setArticles] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);
    const [loadingSummaryIndex, setLoadingSummaryIndex] = useState(null);

    useEffect(() => {
        const fetchArticles = async () => {
            try {
                const response = await axios.get('/api/news?category=technology&country=us&page_size=10');
                setArticles(response.data.articles);
            } catch (err) {
                setError("Failed to fetch articles.");
            } finally {
                setLoading(false);
            }
        };

        fetchArticles();
    }, []);

    const loadSummary = async (index, articleUrl) => {
        setLoadingSummaryIndex(index); // Set the loading state for the current article
        try {
            const response = await axios.get(`/api/news/summary?article_url=${encodeURIComponent(articleUrl)}`);
            const updatedArticles = [...articles];
            updatedArticles[index].summary = response.data.summary; // Add the summary to the article
            setArticles(updatedArticles);
        } catch (err) {
            alert("Failed to load summary. Please try again later.");
        } finally {
            setLoadingSummaryIndex(null); // Reset loading state
        }
    };

    if (loading) return <p>Loading news...</p>;
    if (error) return <p>{error}</p>;

    return (
        <div className="news-container">
            {articles.map((article, index) => (
                <div key={index} className="article-card">
                    <a href={article.url} target="_blank" rel="noopener noreferrer">
                        <img src={article.urlToImage} alt={article.title} />
                    </a>
                    <h3>{article.title}</h3>
                    <p>Source: {article.source}</p>
                    {article.summary ? (
                        <p className="summary">{article.summary}</p>
                    ) : (
                        <button
                            onClick={() => loadSummary(index, article.url)}
                            disabled={loadingSummaryIndex === index}
                        >
                            {loadingSummaryIndex === index ? "Loading..." : "Load Summary"}
                        </button>
                    )}
                </div>
            ))}
        </div>
    );
};

export default News;

