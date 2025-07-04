# 📰 News Summarization Web App

**Author:** Matthew Reiley
**Date:** December 9, 2024
---

## 🌐 Live Demo

👉 [https://news-reader-now.vercel.app/](https://news-reader-now.vercel.app/)
---

## 🌟 Overview

The **News Summarization Web App** is a modern, responsive tool designed to make reading the news more efficient. It condenses lengthy articles into concise, clear summaries using **Natural Language Processing (NLP)** — helping users stay informed while saving time.

Users can:

* Browse the latest news articles
* Load additional articles dynamically
* View AI-generated summaries of individual articles
* Search for specific topics or keywords

This project demonstrates seamless integration between frontend and backend technologies, showcasing my skills in full-stack development, NLP, and scalable deployment.

---

## 🎯 Features

✅ Browse and load news articles with pagination
✅ "Load More" button for seamless article browsing
✅ AI-generated summaries of individual articles
✅ Dedicated article pages with metadata & summary
✅ Search functionality with keyword filtering
✅ Responsive, mobile-friendly design

---

## 🖥️ Tech Stack

| Layer        | Technology                                         |                  |
| ------------ | -------------------------------------------------- | ---------------- |
| **Backend**  | Flask (Python) — REST API for articles & summaries |                  |
| **Database** | MongoDB — stores articles, summaries & metadata    |                  |
| **NLP**      | Hugging Face Transformers — summarization model    |                  |
| **Frontend** | React.js — responsive, interactive UI              |                  |
| **Hosting**  | Frontend: Vercel                                   | Backend: Railway |

---

## 🚀 Getting Started

### Prerequisites

* Node.js & npm
* Python & pip
* MongoDB (local or Atlas)

### Run Locally

```bash
# Clone the repository
git clone https://github.com/yourusername/news-summarization-app.git
cd news-summarization-app
```

### Backend Setup

```bash
cd backend
pip install -r requirements.txt
python app.py
```

### Frontend Setup

```bash
cd frontend
npm install
npm start
```

The app will be available at: `http://localhost:3000`

---

## 📈 Development Process

### 🔹 Backend

* Flask REST API endpoints:

  * `/articles` — fetch paginated articles
  * `/articles/<id>` — fetch metadata + summary
* NLP: Uses a transformer model to generate high-quality summaries
* MongoDB: Stores raw articles, summaries & metadata

### 🔹 Frontend

* React components:

  * **ArticleList** — list of articles with pagination & Load More
  * **SearchBar** — filters articles by keyword
  * **SummaryPage** — shows summary & details of a single article
* Axios for API requests
* External CSS for clean, readable design

### 🔹 Hosting & Deployment

* **Frontend:** Vercel
* **Backend:** Railway

---

## 💡 Challenges & Solutions

**Challenge:** Efficiently handling large datasets
**Solution:** Backend pagination + frontend "Load More" button

**Challenge:** Accurate & concise summaries
**Solution:** Pre-trained transformer NLP model

**Challenge:** Fast search queries
**Solution:** Indexed MongoDB fields for speedy lookups

---

## 🚀 Future Enhancements

✨ User accounts & personalized news feed
✨ Real-time news updates with WebSockets
✨ Social sharing of article summaries

---

## 📌 Why I Built This

I wanted to create a practical application of NLP that addresses a real-world problem: information overload. This app allowed me to deepen my understanding of full-stack development, cloud deployment, and the power of AI-driven text summarization.

---




