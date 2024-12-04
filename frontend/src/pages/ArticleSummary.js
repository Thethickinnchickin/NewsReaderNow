import React, { useState, useEffect } from "react";
import { useLocation } from "react-router-dom";
import axios from "axios";

function ArticleSummaryPage() {
    const [summary, setSummary] = useState(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);
    const location = useLocation();

    // Extract the article URL from the query string
    const queryParams = new URLSearchParams(location.search);
    const articleUrl = queryParams.get("article_url");

    useEffect(() => {
        const fetchSummary = async () => {
            try {
                const response = await axios.get(`/api/news/summary?article_url=${encodeURIComponent(articleUrl)}`);
                setSummary(response.data.summary);
            } catch (err) {
                setError("Failed to load summary. Please try again.");
            } finally {
                setLoading(false);
            }
        };

        if (articleUrl) fetchSummary();
    }, [articleUrl]);

    if (loading) return <p>Loading...</p>;
    if (error) return <p>{error}</p>;

    return (
        <div className="summary-page container">
            <h2>Article Summary</h2>
            <p>{summary}</p>
        </div>
    );
}

export default ArticleSummaryPage;
