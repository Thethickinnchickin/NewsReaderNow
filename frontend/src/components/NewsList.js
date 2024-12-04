import React from 'react';
import NewsCard from './NewsCard';

const NewsList = ({ articles }) => {
    return (
        <div>
            {articles.map((article, index) => (
                <NewsCard key={index} article={article} />
            ))}
        </div>
    );
};

export default NewsList;
