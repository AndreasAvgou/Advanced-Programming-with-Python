# File: models.py

class Track:
    """
    Task 3.1: Track Class representing a music track.
    """
    def __init__(self, track_id, artist, title, genre, energy, popularity):
        self.track_id = track_id
        self.artist = artist
        # Title is not in the provided csv snippet, using genre/id as placeholder or assuming column existence
        # Adjusted to match the dataset provided: track_id, artist, genre, tempo, energy, popularity, release_year
        self.genre = genre
        self.energy = energy
        self.popularity = popularity

    def __str__(self):
        return f"Track({self.track_id} | {self.artist} | {self.genre} | Pop: {self.popularity})"

class MusicLibrary:
    """
    Task 3.2: Music Library Management System.
    Manages a collection of tracks.
    """
    def __init__(self):
        self.tracks = []

    def load_from_dataframe(self, df):
        """
        Populates the library from a Pandas DataFrame.
        """
        for _, row in df.iterrows():
            # Create Track object
            track = Track(
                row['track_id'], 
                row['artist'], 
                f"Track_{row['track_id']}", # Placeholder title 
                row['genre'], 
                row['energy'], 
                row['popularity']
            )
            self.tracks.append(track)

    def get_most_energetic_tracks(self, top_n=3):
        """
        Returns the top N tracks with the highest energy.
        """
        sorted_tracks = sorted(self.tracks, key=lambda x: x.energy, reverse=True)
        return sorted_tracks[:top_n]

    def count_tracks_by_genre(self):
        """
        Returns a dictionary with count of tracks per genre.
        """
        counts = {}
        for track in self.tracks:
            counts[track.genre] = counts.get(track.genre, 0) + 1
        return counts