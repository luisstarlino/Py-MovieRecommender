import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

class HybridRecommender:
    def __init__(self):
        self.movies = pd.DataFrame({
            "title": ["Matrix", "Titanic", "Toy Story", "Avatar", "The Godfather"],
            "genre": ["Sci-Fi", "Romance", "Animation", "Sci-Fi", "Drama"],
            "popularity": [95, 90, 80, 92, 85],
            "score": [0.9, 0.88, 0.85, 0.87, 0.95]
        })

    def get_recommendations(self, genre, popularity):
        df = self.movies.copy()
        df = df[df["genre"].str.contains(genre, case=False)]
        df = df[df["popularity"] >= popularity]
        df = df.sort_values("score", ascending=False)
        return df.head(5)
