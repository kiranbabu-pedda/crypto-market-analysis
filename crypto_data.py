import requests
import pandas as pd
import time
import os

def fetch_crypto_data():
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        "vs_currency": "usd",
        "order": "market_cap_desc",
        "per_page": 50,
        "page": 1,
        "sparkline": "false"
    }
    response = requests.get(url, params=params)
    data = response.json()
    return data

def process_data(data):
    crypto_list = []
    for coin in data:
        crypto_info = {
            "Name": coin["name"],
            "Symbol": coin["symbol"],
            "Price (USD)": coin["current_price"],
            "Market Cap (USD)": coin["market_cap"],
            "24h Volume (USD)": coin["total_volume"],
            "24h Change (%)": coin["price_change_percentage_24h"]
        }
        crypto_list.append(crypto_info)
    df = pd.DataFrame(crypto_list)
    return df

def analyze_data(df):
    top_5 = df.nlargest(5, 'Market Cap (USD)')
    avg_price = df["Price (USD)"].mean()
    highest_change = df.loc[df["24h Change (%)"].idxmax()]
    lowest_change = df.loc[df["24h Change (%)"].idxmin()]
    print("Top 5 Cryptocurrencies by Market Cap:")
    print(top_5)
    print(f"Average Price of Top 50 Cryptocurrencies: ${avg_price:.2f}")
    print("Highest 24h Change:", highest_change)
    print("Lowest 24h Change:", lowest_change)

def save_to_excel(df):
    if not os.path.exists("crypto_data.xlsx"):
        df.to_excel("crypto_data.xlsx", sheet_name="Live Crypto Data", index=False)
    else:
        with pd.ExcelWriter("crypto_data.xlsx", engine="openpyxl", mode="a", if_sheet_exists='overlay') as writer:
            df.to_excel(writer, sheet_name="Live Crypto Data", index=False)

def main():
    while True:
        data = fetch_crypto_data()
        df = process_data(data)
        analyze_data(df)
        save_to_excel(df)
        time.sleep(300)

if __name__ == "__main__":
    main()
