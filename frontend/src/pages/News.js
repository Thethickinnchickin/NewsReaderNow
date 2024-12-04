import React, { useEffect, useState } from 'react';
import axios from 'axios';

const News = () => {
    const [articles, setArticles] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);
    const [summaries, setSummaries] = useState({}); // Store fetched summaries
    const [loadingSummaries, setLoadingSummaries] = useState({}); // Track loading states for summaries

    useEffect(() => {
        const fetchNews = async () => {
            try {
                const response = await axios.get('/api/news?category=technology');
                setArticles(response.data.articles);
                setLoading(false);
            } catch (err) {
                setError(err.message);
                setLoading(false);
            }
        };

        fetchNews();
    }, []);

    const handleFetchSummary = async (articleUrl, index) => {
        if (summaries[index]) return; // Prevent re-fetching if summary is already loaded

        // Set the loading state for the specific article
        setLoadingSummaries((prev) => ({
            ...prev,
            [index]: true,
        }));

        try {
            const response = await axios.get(`/api/news/summary?article_url=${encodeURIComponent(articleUrl)}`);
            setSummaries((prevSummaries) => ({
                ...prevSummaries,
                [index]: response.data.summary, // Store summary for the specific article
            }));
        } catch (err) {
            alert('Failed to load summary. Please try again.');
        } finally {
            // Remove the loading state for the specific article
            setLoadingSummaries((prev) => ({
                ...prev,
                [index]: false,
            }));
        }
    };

    if (loading) return <p>Loading news...</p>;
    if (error) return <p>Error loading news: {error}</p>;

    return (
        <div className="news-page container">
            {articles.map((article, index) => (
                <div key={index} className="article-card">
                    <a href={article.url} target="_blank" rel="noopener noreferrer">
                        <img src={article.urlToImage} alt={article.title} className="clickable-image" />
                    </a>
                    <h3>{article.title}</h3>
                    <p>Source: {article.source}</p>
                    {summaries[index] ? (
                        // Display summary if already fetched
                        <p className="summary">{summaries[index]}</p>
                    ) : loadingSummaries[index] ? (
                        // Show loading indicator while summary is being fetched
                        <p>Loading summary...</p>
                    ) : (
                        // Show button if summary is not yet fetched
                        <button onClick={() => handleFetchSummary(article.url, index)}>
                            Load Summary
                        </button>
                    )}
                </div>
            ))}
        </div>
    );
};

export default News;
