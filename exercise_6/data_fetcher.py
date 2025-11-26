# File: data_fetcher.py
import requests
import config

def fetch_flight_data():
    """
    Connects to the OpenSky API and fetches live flight data.
    Returns the 'states' list from the JSON response.
    """
    print(f"--- Connecting to API: {config.API_URL} ---")
    
    try:
        # Request data with geographical parameters
        response = requests.get(config.API_URL, params=config.params)
        
        # Check if the request was successful
        if response.status_code == 200:
            data = response.json()
            # The actual flight data is in the 'states' key
            states = data.get('states', [])
            print(f"[Success] Retrieved data for {len(states) if states else 0} flights.")
            return states
        else:
            print(f"[Error] API returned status code: {response.status_code}")
            return None

    except Exception as e:
        print(f"[Error] Connection failed: {e}")
        return None