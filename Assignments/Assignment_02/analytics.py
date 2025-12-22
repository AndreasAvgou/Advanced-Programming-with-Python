# File: analytics.py
import pandas as pd

def get_genre_stats(df):
    """
    Task 2.1: Calculate average tempo and energy per genre.
    """
    print("\n--- Genre Statistics ---")
    genre_stats = df.groupby('genre')[['tempo', 'energy', 'popularity']].mean()
    print(genre_stats)
    return genre_stats

def get_top_artists_by_popularity(df, top_n=5):
    """
    Task 2.2: Identify top artists based on average popularity.
    """
    print(f"\n--- Top {top_n} Artists by Popularity ---")
    top_artists = df.groupby('artist')['popularity'].mean().sort_values(ascending=False).head(top_n)
    print(top_artists)
    return top_artists

def get_tracks_by_year(df, year):
    """
    Returns tracks released after a specific year.
    """
    return df[df['release_year'] > year]