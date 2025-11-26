# File: config.py

# OpenSky Network API Endpoint (Public)
API_URL = "https://opensky-network.org/api/states/all"

# Bounding Box for the area (min_lat, min_lon, max_lat, max_lon)
# Example: Greece & surrounding area
# You can remove these params to fetch global data (but it's heavy)
params = {
    'lamin': 34.0,  # Min Latitude
    'lomin': 19.0,  # Min Longitude
    'lamax': 42.0,  # Max Latitude
    'lomax': 29.0   # Max Longitude
}

# Output filename
OUTPUT_FILE = "flight_data.json"