from flask import Flask, render_template, request
import pandas as pd
import numpy as np
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)

# -----------------------------------------
# Load Dataset
# -----------------------------------------

movies = pd.read_csv("tmdb_5000_movies.csv")
credits = pd.read_csv("tmdb_5000_credits.csv")

# Merge datasets
movies = movies.merge(credits, on="title")

# Load preprocessed dataset (generated from notebook)
try:
    new_df = pd.read_csv("cleaned_tmdb_dataset.csv")
except:
    new_df = movies[['movie_id', 'title', 'overview']].copy()
    new_df['overview'] = new_df['overview'].fillna("")
    new_df['tags'] = new_df['overview']

# -----------------------------------------
# TF-IDF Model
# -----------------------------------------

tfidf = TfidfVectorizer(stop_words="english")
tfidf_matrix = tfidf.fit_transform(new_df["tags"])

cosine_sim = cosine_similarity(tfidf_matrix)

indices = pd.Series(new_df.index, index=new_df["title"]).drop_duplicates()

# -----------------------------------------
# Recommendation Function
# -----------------------------------------

def recommend(movie_name):

    if movie_name not in indices:
        return []

    idx = indices[movie_name]

    similarity_scores = list(enumerate(cosine_sim[idx]))

    similarity_scores = sorted(
        similarity_scores,
        key=lambda x: x[1],
        reverse=True
    )[1:11]

    movie_indices = [i[0] for i in similarity_scores]

    recommendations = []

    for i in movie_indices:

        recommendations.append({
            "title": new_df.iloc[i]["title"]
        })

    return recommendations

# -----------------------------------------
# Routes
# -----------------------------------------

@app.route("/", methods=["GET", "POST"])
def home():

    recommendations = []

    selected_movie = ""

    if request.method == "POST":

        selected_movie = request.form.get("movie")

        recommendations = recommend(selected_movie)

    movie_list = sorted(new_df["title"].unique())

    return render_template(
        "index.html",
        movies=movie_list,
        recommendations=recommendations,
        selected_movie=selected_movie
    )

@app.route("/about")
def about():

    return render_template("about.html")

@app.route("/dataset")
def dataset():

    return render_template("dataset.html")

# -----------------------------------------
# Run App
# -----------------------------------------

if __name__ == "__main__":
    app.run(debug=True)
