import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Home from './pages/Home';
import News from './pages/News';

const App = () => {
    return (
        <Router>
            <div>
                <nav className="navbar">
                    <ul className="nav-list">
                        <li className="nav-item"><a href="/" className="nav-link">Home</a></li>
                        <li className="nav-item"><a href="/news" className="nav-link">News</a></li>
                    </ul>
                </nav>
                <Routes>
                    <Route path="/" element={<Home />} />
                    <Route path="/news" element={<News />} />
                </Routes>
            </div>
        </Router>
    );
};

export default App;
