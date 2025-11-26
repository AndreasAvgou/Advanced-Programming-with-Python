# File: main.py
import data_fetcher
import data_storage
import analyzer

def main():
    print("=== Flight Data Analysis System (OpenSky API) ===")

    # 1. Read Data (Fetch from API)
    flight_data = data_fetcher.fetch_flight_data()

    if flight_data:
        # 2. Save Data
        data_storage.save_to_json(flight_data)
        data_storage.save_to_csv(flight_data)

        # 3. Analyze Data
        analyzer.find_fastest_flight(flight_data)

        # 4. Visualize Data
        print("\nGenerating map plot...")
        analyzer.plot_flight_positions(flight_data)
    else:
        print("Analysis aborted due to missing data.")

if __name__ == "__main__":
    main()