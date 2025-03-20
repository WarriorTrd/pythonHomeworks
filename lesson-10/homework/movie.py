import requests
import random

API_key = "how can i get my api key"  

def get_genre_id(genre_name):
    url = f"https://api.themoviedb.org/3/genre/movie/list?api_key={API_key}&language=en-US"
    response = requests.get(url)
    
    if response.status_code == 200:
        genres = response.json()["genres"]
        for g in genres:
            if g["name"].lower() == genre_name.lower():
                return g["id"]
        print("Sorry, I couldn't find that genre.")
    else:
        print("Oops! Something went wrong.")
    return None

def get_movies(genre_id):
    url = f"https://api.themoviedb.org/3/discover/movie?api_key={API_KEY}&with_genres={genre_id}"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()["results"]
    return []

def recommend_movie():
    genre_name = input("Enter a movie genre (Action, comedy, drama): ")
    genre_id = get_genre_id(genre_name)

    if genre_id:
        movies = get_movies(genre_id)
        if movies:
            movie = random.choice(movies)
            print("Here's a movie for you:")
            print(f"title: {movie['title']}")
            print(f"release Date: {movie['release_date']}")
            print(f"rating: {movie['vote_average']}/10")
            print(f"overview: {movie['overview']}\n")
        else:
            print("No movies found in this genre.")

recommend_movie()
