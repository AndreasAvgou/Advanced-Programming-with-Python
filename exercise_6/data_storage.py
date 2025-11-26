# File: data_storage.py
import json
import csv
import config

def save_to_json(data):
    """
    Saves the list of flight data to a JSON file.
    """
    if not data:
        print("[Warning] No data to save.")
        return

    try:
        with open(config.OUTPUT_FILE, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)
        print(f"[Success] Data saved to '{config.OUTPUT_FILE}'")
    except Exception as e:
        print(f"[Error] Failed to save JSON: {e}")

def save_to_csv(data, filename="flights.csv"):
    """
    Optional: Saves specific fields (Callsign, Country, Velocity) to CSV.
    """
    if not data: return

    try:
        with open(filename, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(["Callsign", "Country", "Longitude", "Latitude", "Velocity"])
            
            for flight in data:
                # flight index mapping: 1=Callsign, 2=Country, 5=Lon, 6=Lat, 9=Velocity
                writer.writerow([flight[1], flight[2], flight[5], flight[6], flight[9]])
        
        print(f"[Success] Data saved to '{filename}'")
    except Exception as e:
        print(f"[Error] Failed to save CSV: {e}")