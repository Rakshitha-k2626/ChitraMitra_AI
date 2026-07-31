# 🎬 ChitraMitra AI
### Your AI Movie Friend

An intelligent **Movie Recommendation System** built using **Machine Learning**, **Natural Language Processing (NLP)**, and **Python**. ChitraMitra AI recommends movies based on content similarity by analyzing genres, keywords, cast, directors, and movie overviews.

---

## 📌 Project Overview

With thousands of movies available across streaming platforms, finding the perfect movie can be overwhelming.

**ChitraMitra AI** solves this problem by recommending movies that are similar in content to the user's selected movie. The system uses **TF-IDF Vectorization** and **Cosine Similarity** to identify and recommend the most relevant movies.

---

## ✨ Features

- 🎬 Intelligent Movie Recommendation
- 🤖 Machine Learning-Based Recommendation Engine
- 📊 Exploratory Data Analysis (EDA)
- 🧹 Data Cleaning & Feature Engineering
- 📈 Interactive Visualizations
- 🔍 Search Movies by Title
- ⭐ Top 10 Similar Movie Recommendations
- 🎯 Content-Based Recommendation System
- 🌐 Flask Web Interface (Optional)
- 📱 Responsive UI Design

---

# 🧠 Machine Learning Workflow

```
TMDB Dataset
      │
      ▼
Data Cleaning
      │
      ▼
Feature Engineering
      │
      ▼
TF-IDF Vectorization
      │
      ▼
Cosine Similarity
      │
      ▼
Movie Recommendation
```

---

# 📂 Dataset

This project uses the **TMDB 5000 Movie Dataset**, consisting of:

- tmdb_5000_movies.csv
- tmdb_5000_credits.csv

Dataset contains:

- Movie Title
- Genres
- Keywords
- Cast
- Crew
- Overview
- Popularity
- Vote Average
- Vote Count
- Runtime
- Release Date
- Original Language

---

# 🛠️ Technologies Used

## Programming Language

- Python

## Libraries

- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- Flask
- Pickle

## Machine Learning

- TF-IDF Vectorization
- Cosine Similarity

## Development Environment

- Google Colab
- Visual Studio Code

---

# 📊 Exploratory Data Analysis

The notebook includes:

- Movie Language Distribution
- Rating Distribution
- Runtime Distribution
- Top Rated Movies
- Most Popular Movies
- Release Year Trend
- Genre Analysis
- Correlation Analysis

---

# ⚙️ Machine Learning Model

The recommendation engine follows these steps:

1. Merge TMDB Movies and Credits datasets.
2. Remove missing and duplicate values.
3. Extract important movie information:
   - Genres
   - Keywords
   - Cast
   - Director
   - Overview
4. Create a combined feature called **Tags**.
5. Convert text into numerical vectors using **TF-IDF Vectorization**.
6. Compute similarity using **Cosine Similarity**.
7. Recommend the Top 10 most similar movies.

---

# 📁 Project Structure

```
ChitraMitra-AI/
│
├── app.py
├── README.md
├── requirements.txt
├── ChitraMitra_AI.ipynb
├── cleaned_tmdb_dataset.csv
├── tmdb_5000_movies.csv
├── tmdb_5000_credits.csv
│
├── templates/
│     └── index.html
│
├── static/
│     ├── css/
│     │      style.css
│     ├── js/
│     │      script.js
│     └── images/
│
└── assets/
      ├── banner.png
      ├── workflow.png
      └── screenshots/
```

---

# 🚀 Installation

Clone the repository

```bash
git clone https://github.com/yourusername/ChitraMitra-AI.git
```

Move into the project folder

```bash
cd ChitraMitra-AI
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the Flask application

```bash
python app.py
```

---

# 📷 Project Screenshots

## Home Page

> Add screenshot here

---

## Recommendation Output

> Add screenshot here

---

## EDA Dashboard

> Add screenshot here

---

# 📈 Sample Recommendation

Input Movie

```
Interstellar
```

Output

```
The Martian

Gravity

Arrival

Moon

Ad Astra

Contact

Sunshine

Passengers

Oblivion

Europa Report
```

---

# 💡 Applications

- Netflix Recommendation Systems
- Amazon Prime Video
- Disney+
- OTT Platforms
- Content Recommendation
- Entertainment Analytics
- Movie Discovery Platforms

---

# 🔮 Future Scope

- TMDB API Integration
- Movie Posters
- Trailer Integration
- User Login System
- Personalized Recommendations
- Hybrid Recommendation System
- Deep Learning Recommendation Models
- Streamlit Deployment
- Cloud Deployment

---

# 📚 Learning Outcomes

Through this project, I gained hands-on experience in:

- Data Cleaning
- Feature Engineering
- Exploratory Data Analysis
- Natural Language Processing
- Machine Learning
- Recommendation Systems
- TF-IDF Vectorization
- Cosine Similarity
- Python Programming
- Flask Web Development
- Git & GitHub

---

# 👩‍💻 Developed By

**Rakshitha K.**

B.E. Computer Science & Design

Passionate about Artificial Intelligence, Machine Learning, Data Science, UI/UX Design, and Intelligent Software Systems.

---


## 📄 License

This project is developed for educational and portfolio purposes.
