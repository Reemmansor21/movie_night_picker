import requests 
import pandas as pd 
import os 
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("TMDB_API_KEY")
url = "https://api.themoviedb.org/3/movie/popular"

params = {
    "api_key": api_key,
    "language": "en-US"
}

response = requests.get(url, params=params)

data = response.json()
print(data["results"][0])

movies = pd.DataFrame(data["results"])

print(movies[["title", "vote_average", "popularity", "release_date"]].head())

genre_url = "https://api.themoviedb.org/3/genre/movie/list"

genre_response = requests.get(genre_url, params=params)
genre_data = genre_response.json()

print(genre_data["genres"])

genre_name = input("Enter a movie genre: ")

genre_id = None

for genre in genre_data["genres"]:
    if genre["name"].lower() == genre_name.lower():
        genre_id = genre["id"]
        break

print("Selected genre ID:", genre_id)

min_rating = float(input("Enter minimum rating (0-10): "))

print("Minimum rating:", min_rating)

max_runtime = int(input("Enter maximum movie runtime in minutes: "))

print("Maximum runtime:", max_runtime, "minutes")

discover_url = "https://api.themoviedb.org/3/discover/movie"

discover_params = {
    "api_key": api_key,
    "with_genres": genre_id,
    "vote_average.gte": min_rating,
    "vote_count.gte": 500,
    "with_runtime.lte": max_runtime,
    "sort_by": "vote_average.desc"
}

discover_response = requests.get(discover_url, params=discover_params)
discover_data = discover_response.json()


results = discover_data["results"]

movies_df = pd.DataFrame(results)

print(movies_df[["title", "vote_average", "release_date"]].head(10))

top_movies = movies_df.head(5).copy()

runtimes = []

for movie_id in top_movies["id"]:
    details_url = f"https://api.themoviedb.org/3/movie/{movie_id}"
    details_response = requests.get(details_url, params={"api_key": api_key})
    details_data = details_response.json()
    runtimes.append(details_data["runtime"])

top_movies["runtime"] = runtimes

top_movies = top_movies[top_movies["runtime"] <= max_runtime]

top_movies = top_movies.reset_index(drop=True)

print(top_movies[["title", "vote_average", "runtime", "release_date"]])

