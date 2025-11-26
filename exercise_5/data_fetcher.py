# File: data_fetcher.py
import requests
import pandas as pd
import time
from config import API_URL, VS_CURRENCY, DAYS

def fetch_crypto_data(coins):
    """
    Fetches historical price data for a list of cryptocurrencies 
    from the CoinGecko API.
    
    Args:
        coins (list): List of coin IDs (e.g., ['bitcoin', 'ethereum'])
        
    Returns:
        pd.DataFrame: A DataFrame with dates as index and coins as columns.
    """
    all_data = {}

    print(f"--- Fetching data for {len(coins)} cryptocurrencies ---")
    
    for coin in coins:
        try:
            # Construct the API endpoint
            endpoint = f"{API_URL}/coins/{coin}/market_chart"
            params = {'vs_currency': VS_CURRENCY, 'days': DAYS, 'interval': 'daily'}
            
            response = requests.get(endpoint, params=params)
            data = response.json()
            
            if 'prices' not in data:
                print(f"[Error] No data found for {coin}")
                continue

            # Extract prices (timestamp, price)
            prices = data['prices']
            
            # Create a temporary DataFrame for this coin
            df_coin = pd.DataFrame(prices, columns=['timestamp', coin])
            df_coin['timestamp'] = pd.to_datetime(df_coin['timestamp'], unit='ms')
            df_coin.set_index('timestamp', inplace=True)
            
            # Add to dictionary
            all_data[coin] = df_coin[coin]
            
            print(f"[Success] Fetched {coin}")
            
            # Respect API rate limits (wait 1 second)
            time.sleep(1)
            
        except Exception as e:
            print(f"[Error] Failed to fetch {coin}: {e}")

    # Combine all coins into one DataFrame
    if all_data:
        final_df = pd.concat(all_data.values(), axis=1)
        final_df.columns = all_data.keys()
        return final_df
    else:
        return None