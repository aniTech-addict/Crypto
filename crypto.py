import requests
import pandas as pd

# CoinGecko API endpoint for getting cryptocurrency market data
url = "https://api.coingecko.com/api/v3/coins/markets"
params = {
    "vs_currency": "usd",  # Convert prices to USD
    "order": "market_cap_desc",  # Sort by market cap
    "per_page": 10,  # Get top 10 cryptocurrencies
    "page": 1,
    "sparkline": "false"  # No sparkline data needed
}

# Fetch data from API
response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()  # Convert response to Python dictionary
    print("Data fetched successfully!")
else:
    print("Error fetching data:", response.status_code)
