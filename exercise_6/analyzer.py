# File: analyzer.py
import matplotlib.pyplot as plt

def find_fastest_flight(flight_data):
    """
    Identifies the flight with the highest velocity.
    """
    if not flight_data: return

    max_speed = 0
    fastest_plane = None

    for flight in flight_data:
        # Index 9 is velocity (m/s). Sometimes it's None.
        velocity = flight[9]
        if velocity and velocity > max_speed:
            max_speed = velocity
            fastest_plane = flight

    if fastest_plane:
        callsign = fastest_plane[1].strip()
        print(f"\n--- Fastest Flight ---")
        print(f"Callsign: {callsign if callsign else 'Unknown'}")
        print(f"Country:  {fastest_plane[2]}")
        print(f"Velocity: {max_speed} m/s")

def plot_flight_positions(flight_data):
    """
    Creates a scatter plot of flight positions (Longitude vs Latitude).
    """
    if not flight_data: return

    longitudes = []
    latitudes = []

    for flight in flight_data:
        lon = flight[5]
        lat = flight[6]
        
        if lon and lat:
            longitudes.append(lon)
            latitudes.append(lat)

    plt.figure(figsize=(10, 6))
    plt.scatter(longitudes, latitudes, c='blue', alpha=0.5, s=10)
    plt.title('Live Flight Positions')
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    plt.grid(True)
    plt.show()