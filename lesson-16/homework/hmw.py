import pandas as pd
import sqlite3

# Part 1: Reading Files

def read_sqlite():
    conn = sqlite3.connect("chinook.db")
    df = pd.read_sql("SELECT * FROM customers", conn)
    conn.close()
    print("First 10 rows of customers table:")
    print(df.head(10))

def read_json():
    df = pd.read_json("iris.json")
    print("Shape of iris dataset:", df.shape)
    print("Column names:", df.columns.tolist())
    return df

def read_excel():
    df = pd.read_excel("titanic.xlsx")
    print("First 5 rows of Titanic dataset:")
    print(df.head())
    return df

def read_parquet():
    df = pd.read_parquet("flights.parquet")
    print("Flights dataset info:")
    print(df.info())
    return df

def read_csv():
    df = pd.read_csv("movie.csv")
    print("Random sample of 10 movies:")
    print(df.sample(10))
    return df

# Part 2: Exploring DataFrames

def explore_iris(df):
    df.columns = df.columns.str.lower()
    print("Renamed columns:", df.columns.tolist())
    print("Selected columns:")
    print(df[["sepallength", "sepalwidth"]].head())

def explore_titanic(df):
    print("Passengers older than 30:")
    print(df[df["age"] > 30].head())
    print("Number of males and females:")
    print(df["sex"].value_counts())

def explore_flights(df):
    print("Origin, Destination, and Carrier columns:")
    print(df[["origin", "dest", "carrier"]].head())
    print("Number of unique destinations:", df["dest"].nunique())

def explore_movies(df):
    df = df[df["duration"] > 120].sort_values(by="director_facebook_likes", ascending=False)
    print("Movies longer than 120 minutes sorted by director Facebook likes:")
    print(df.head())

# Part 3: Challenges and Explorations

def analyze_iris(df):
    print("Iris dataset statistics:")
    print(df.describe())

def analyze_titanic(df):
    print("Titanic age stats:")
    print("Min:", df["age"].min())
    print("Max:", df["age"].max())
    print("Sum:", df["age"].sum())

def analyze_movies(df):
    print("Director with highest total Facebook likes:")
    print(df.groupby("director_name")["director_facebook_likes"].sum().idxmax())
    print("Top 5 longest movies:")
    print(df.nlargest(5, "duration")[["title", "director_name"]])

def clean_flights(df):
    print("Checking for missing values:")
    print(df.isnull().sum())
    df.fillna(df.mean(), inplace=True)
    print("Missing values filled with column mean.")

if __name__ == "__main__":
    df_sqlite = read_sqlite()
    df_iris = read_json()
    df_titanic = read_excel()
    df_flights = read_parquet()
    df_movies = read_csv()
    
    explore_iris(df_iris)
    explore_titanic(df_titanic)
    explore_flights(df_flights)
    explore_movies(df_movies)
    
    analyze_iris(df_iris)
    analyze_titanic(df_titanic)
    analyze_movies(df_movies)
    clean_flights(df_flights)