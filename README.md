Cryptocurrency Data Analysis

This repository contains Python code for fetching live cryptocurrency data from the CoinGecko API, performing basic analysis on the data, and saving it to an Excel file for further review. The code automatically updates every 5 minutes and stores the data in an Excel sheet.

Features:
- Live Data Fetching: Fetches live data on the top 50 cryptocurrencies by market capitalization.
- Data Processing: Organizes data into a structured table containing:
  - Cryptocurrency Name
  - Symbol (e.g., BTC, ETH)
  - Current Price (in USD)
  - Market Cap (in USD)
  - 24-hour Volume (in USD)
  - 24-hour Price Change (%)
- Basic Analysis: Analyzes the data to find:
  - Top 5 cryptocurrencies by market cap
  - Average price of the top 50 cryptocurrencies
  - Cryptocurrency with the highest and lowest 24-hour price change.
- Excel Export: Saves the processed data to an Excel file that updates automatically.
- Automated Updates: The script runs in an infinite loop, fetching data every 5 minutes and saving it to an Excel file.

Technologies Used:
- Python: The primary programming language used.
- Pandas: For data processing and manipulation.
- Requests: To fetch data from the CoinGecko API.
- Openpyxl: For saving the data into an Excel file.
- CoinGecko API: The source of the cryptocurrency data.

Installation:
To run this script locally, you need Python installed on your system along with a few libraries. You can install them using `pip`.
1. Clone the repository or download the Python script to your local machine.
2. Install the required Python libraries:
   pip install requests pandas openpyxl
3. Run the Python script:
   python crypto_data.py
This will start fetching cryptocurrency data every 5 minutes and save it to an Excel file named `crypto_data.xlsx`.

Script Overview:
crypto_data.py
- Fetching Data: The script uses the CoinGecko API to fetch the top 50 cryptocurrencies by market capitalization.
- Data Processing: It extracts relevant details like the name, symbol, current price, market cap, volume, and 24-hour price change.
- Analysis: It performs basic analysis on the data:
  - Lists the top 5 cryptocurrencies by market cap.
  - Calculates the average price of the top 50 cryptocurrencies.
  - Identifies the cryptocurrency with the highest and lowest 24-hour price change.
- Excel Export: After processing the data, it saves the data to an Excel file (`crypto_data.xlsx`), which updates every 5 minutes.

Usage:
After running the script, the data will be saved in an Excel file. The file is updated every 5 minutes, and you can open it to see the latest cryptocurrency data.

License:
This project is licensed under the MIT License - see the LICENSE file for details.

Contributing:
Feel free to fork this repository and submit a pull request if you would like to contribute. Please open an issue if you encounter any bugs or have suggestions for improvement.

Acknowledgments:
- Thanks to CoinGecko (https://www.coingecko.com/) for providing free cryptocurrency data via their API.
- Thanks to the open-source community for creating useful Python libraries like Pandas, Requests, and Openpyxl.
