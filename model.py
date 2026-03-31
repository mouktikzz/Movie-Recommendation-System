import pandas as pd
from sklearn.decomposition import TruncatedSVD

def load_data():
    ratings = pd.read_csv("data/ratings.csv")
    movies = pd.read_csv("data/movies.csv")
    data = pd.merge(ratings, movies, on="movieId")
    return data

def create_matrix(data):
    user_item = data.pivot_table(index='userId', columns='title', values='rating').fillna(0)
    """
        user Batman Interstellar Avengers
          1    5        0          3
          2    3        2          0
    """
    return user_item
#     user_item =
# [
#  [5, 0, 0, 3],   # User 1
#  [4, 5, 0, 0],   # User 2
#  [0, 4, 5, 0]    # User 3
# ]


def train_model(user_item):
    svd = TruncatedSVD(n_components=50)
    matrix = svd.fit_transform(user_item)
    #     [
        #  [2.1, 0.5],   # User 1 Interpretaion: Action (high), Not much drama
        #  [1.8, 1.2],   # User 2
        #  [0.9, 2.0]    # User 3
    # ]
    
    # Reconstruct matrix (predict missing ratings)
    reconstructed = svd.inverse_transform(matrix)  
#     [
#  [5.0, 4.7, 4.9, 3.0],
#  [4.2, 5.0, 4.3, 2.8],
#  [3.8, 4.1, 5.0, 2.5]
# ]

    return reconstructed

def recommend_svd(user_id, user_item, reconstructed, n=5):
    
    # Convert to index
    user_index = user_id - 1

    # Get predicted ratings for this user
    user_ratings = reconstructed[user_index] # [5, 0, 0, 4] -> [5.0, 4.7, 3.2, 4.0]

    # Get movies already watched
    user_movies = set(user_item.columns[user_item.iloc[user_index] > 0])

    # Create (movie, predicted_rating) list
    movie_scores = list(zip(user_item.columns, user_ratings))
#     [
#  ("Batman", 5.0),
#  ("Interstellar", 4.7),
#  ("Inception", 4.9)
# ]

    # Remove already watched movies
    movie_scores = [m for m in movie_scores if m[0] not in user_movies]

    # Sort by predicted rating
    movie_scores = sorted(movie_scores, key=lambda x: x[1], reverse=True)

    # Return top N movies
    return [(movie, round(float(rating), 1)) for movie, rating in movie_scores[:n]]
    
