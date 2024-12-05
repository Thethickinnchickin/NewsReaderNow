import React, { useEffect, useState } from 'react';
import axios from 'axios';

const News = () => {
    const [articles, setArticles] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);
    const [loadingSummaryIndex, setLoadingSummaryIndex] = useState(null);
    const [searchTerm, setSearchTerm] = useState(''); // For search input
    const [isSearching, setIsSearching] = useState(false); // Search state

    // Fetch default articles (on initial load)
    useEffect(() => {
        const fetchArticles = async () => {
            try {
                const response = await axios.get(
                    `${process.env.REACT_APP_API_URL || 'http://localhost:5000/api'}/news?category=technology&country=us&page_size=10`
                );
                setArticles(response.data.articles);
            } catch (err) {
                setError("Failed to fetch articles.");
            } finally {
                setLoading(false);
            }
        };

        fetchArticles();
    }, []);

    // Function to handle search
    const handleSearch = async () => {
        if (!searchTerm.trim()) return;
    
        setIsSearching(true); // Indicate search is in progress
        setLoading(true); // Show loading state
        setError(null); // Reset errors
    
        try {
            const response = await axios.get(
                `${process.env.REACT_APP_API_URL || 'http://localhost:5000/api'}/search?keywords=${encodeURIComponent(searchTerm)}&page=1&pageSize=10&language=en&sortBy=relevancy`
            );
            console.log(response)
            // Assuming search results are returned in a key called 'articles'
            setArticles(response.data.results.articles || []); // Update articles with search results
        } catch (err) {
            setError("Failed to fetch search results. Please try again.");
        } finally {
            setIsSearching(false); // Reset search state
            setLoading(false); // Reset loading state
        }
    };
    

    // Function to fetch a summary for an article
    const loadSummary = async (index, articleUrl) => {
        setLoadingSummaryIndex(index); // Set the loading state for the current article
        try {
            const response = await axios.get(
                `${process.env.REACT_APP_API_URL || 'http://localhost:5000/api'}/news/summary?article_url=${encodeURIComponent(articleUrl)}`
            );
            const updatedArticles = [...articles];
            updatedArticles[index].summary = response.data.summary; // Add the summary to the article
            setArticles(updatedArticles);
        } catch (err) {
            alert("Failed to load summary. Please try again later.");
        } finally {
            setLoadingSummaryIndex(null); // Reset loading state
        }
    };

    if (loading && !isSearching) return <p>Loading news...</p>;
    if (error) return <p>{error}</p>;
    return (
        <div>
            {/* Search Bar */}
            <div className="search-bar">
                <input
                    type="text"
                    value={searchTerm}
                    onChange={(e) => setSearchTerm(e.target.value)}
                    placeholder="Search for news articles..."
                />
                <button onClick={handleSearch} disabled={isSearching}>
                    {isSearching ? "Searching..." : "Search"}
                </button>
            </div>
    
            {/* News Articles */}
            <div className="news-container">
                {loading ? (
                    <p>Loading...</p>
                ) : error ? (
                    <p>{error}</p>
                ) : articles.length > 0 ? (
                    articles.map((article, index) => (
                        <div key={index} className="article-card">
                            <a href={article.url} target="_blank" rel="noopener noreferrer">
                                <img src={article.urlToImage} alt={article.title} />
                            </a>
                            <h3>{article.title}</h3>
                            <p>Source: {article.source?.name || "Unknown"}</p>
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
                    ))
                ) : (
                    <p>No articles found.</p>
                )}
            </div>
        </div>
    );    
};

export default News;
