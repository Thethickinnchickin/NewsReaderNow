import React from 'react';

const NewsCard = ({ article }) => {
    return (
        <div className="news-card">
            {article.urlToImage && (
                <img src={article.urlToImage} alt={article.title} className="news-image" />
            )}
            <div className="news-content">
                <h2>{article.title}</h2>
                <p>{article.summary}</p>
                <a href={article.url} target="_blank" rel="noopener noreferrer">
                    Read More
                </a>
                <p className="news-source">Source: {article.source}</p>
            </div>
        </div>
    );
};

export default NewsCard;
