from flask import Flask, request, jsonify, render_template
import requests
import spacy
import re

nlp = spacy.load("en_core_web_sm")

# Alpha Vantage API Key
ALPHA_VANTAGE_API_KEY = '_Vc_wFm0Av85sCAMV7V2mjrqXTdQnkzm'


app = Flask(__name__)


COMPANY_SYMBOLS = {
    "apple": "AAPL",
    "tesla": "TSLA",
    "paypal": "PYPL",
    "microsoft": "MSFT",
    "google": "GOOGL",
    "amazon": "AMZN",
    "facebook": "META",
    "nvidia": "NVDA",
    "bitcoin": "BTC",
    "ethereum": "ETH"

}

def get_stock_price(stock_symbol):
    try:
        stock_symbol = stock_symbol.strip().upper() 
        url = f'https://www.alphavantage.co/query'
        params = {
            'function': 'TIME_SERIES_INTRADAY',
            'symbol': stock_symbol,
            'interval': '1min',
            'apikey': ALPHA_VANTAGE_API_KEY
        }
        response = requests.get(url, params=params)
        data = response.json()

        if 'Time Series (1min)' not in data:
            return f"No data found for {stock_symbol}. The symbol may be delisted or incorrect."

        latest_time = list(data['Time Series (1min)'].keys())[0]
        latest_data = data['Time Series (1min)'][latest_time]
        price = latest_data['4. close']

        return f"${float(price):,.2f}"
    except Exception as e:
        return f"Error retrieving data for {stock_symbol}: {e}"


def get_crypto_price(crypto_symbol):
    try:
        crypto_symbol = re.sub(r'\W+', '', crypto_symbol).lower()
        url = f'https://api.coingecko.com/api/v3/simple/price?ids={crypto_symbol}&vs_currencies=usd'
        response = requests.get(url)
        data = response.json()

        if crypto_symbol not in data:
            return f"No data found for {crypto_symbol}. The symbol may be incorrect."

        return f"${data[crypto_symbol]['usd']:,.2f}"
    except Exception as e:
        return f"Error retrieving data for {crypto_symbol}: {e}"

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/chat', methods=['POST'])
def chat():
    query = request.json.get("query", "").strip()
    query_cleaned = re.sub(r'\W+', ' ', query).strip()
    query_lower = query_cleaned.lower()


    if 'stock price' in query_lower:
        company_name = query_cleaned.split()[-1]  
        if company_name in COMPANY_SYMBOLS:
            stock_symbol = COMPANY_SYMBOLS[company_name]  
            price = get_stock_price(stock_symbol)
            return jsonify({"response": f"The stock price for {company_name.capitalize()} ({stock_symbol}) is {price}"})
        else:
            return jsonify({"response": f"Sorry, I couldn't find the stock symbol for {company_name}. Please use the ticker symbol."})


    elif 'crypto' in query_lower or 'bitcoin' in query_lower or 'ethereum' in query_lower:
        crypto_symbol = query_cleaned.split()[-1]  
        price = get_crypto_price(crypto_symbol)
        return jsonify({"response": f"The current price of {crypto_symbol} is {price}"})
    else:
        return jsonify({"response": "I can only assist with stock or cryptocurrency price inquiries."})

if __name__ == '__main__':
    app.run(debug=True)
