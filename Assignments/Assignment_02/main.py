# File: main.py
import config
import data_loader
import analytics
import models
import visualizer

def main():
    print("=== Assignment 2: Music Data Analysis System ===")
    
    # Setup directories
    config.setup_directories()
    
    # --- TASK 1: Dataset Handling ---
    df = data_loader.load_and_clean_data(config.DATA_FILENAME)
    if df is None:
        return

    # --- TASK 2: Analytics ---
    analytics.get_genre_stats(df)
    analytics.get_top_artists_by_popularity(df)

    # --- TASK 3: OOP Architecture ---
    print("\n--- OOP Music Library Analysis ---")
    library = models.MusicLibrary()
    library.load_from_dataframe(df)
    
    # Find most energetic tracks using OOP
    energetic_tracks = library.get_most_energetic_tracks()
    print("Most Energetic Tracks:")
    for track in energetic_tracks:
        print(f" - {track} (Energy: {track.energy})")
        
    # Count by genre using OOP
    genre_counts = library.count_tracks_by_genre()
    print("\nTracks per Genre (OOP Calculated):", genre_counts)

    # --- TASK 4: Visualization ---
    print("\n--- Generating Plots ---")
    visualizer.plot_genre_distribution(df)
    visualizer.plot_energy_vs_popularity(df)
    
    print("\n=== Execution Complete ===")

if __name__ == "__main__":
    main()