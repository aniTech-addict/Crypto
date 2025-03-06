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

# Extract key details
crypto_data = []
for coin in data:
    crypto_data.append({
        "Name": coin["name"],
        "Symbol": coin["symbol"].upper(),
        "Price (USD)": coin["current_price"],
        "Market Cap": coin["market_cap"],
        "24h Volume": coin["total_volume"]
    })

# Convert to Pandas DataFrame
df = pd.DataFrame(crypto_data)

# Display table
print(df)

df.to_csv("crypto_prices.csv", index=False)
print("Data saved to crypto_prices.csv ")

# Read the saved CSV file
df = pd.read_csv("crypto_prices.csv")

# Sort cryptocurrencies by price (descending)
df_sorted = df.sort_values(by="Price (USD)", ascending=False)

print(df_sorted)
