# XNL-21BCE7712-LLM-4 : Documentation for Financial Chatbot Project

Project Overview
This project involves the development of a real-time Financial Assistant Chatbot that can answer queries related to financial topics such as stock prices, cryptocurrency prices, and more. The chatbot integrates data from live financial data APIs (e.g., Alpha Vantage for stocks and CoinGecko for cryptocurrencies) to provide real-time information and respond accurately to user inquiries.

1. Technologies and Tools Used
   
Backend:
Flask: Python web framework to handle HTTP requests and serve HTML templates.
spaCy: Natural language processing (NLP) library used for cleaning and processing user queries.
Requests: For making API calls to Alpha Vantage and CoinGecko to fetch real-time financial data.

Frontend:
HTML/CSS: Used to build the user interface and style the chatbot.
jQuery: For sending AJAX requests to the server to fetch chatbot responses dynamically.

APIs:
Alpha Vantage API: Provides stock market data.
CoinGecko API: Provides cryptocurrency prices.
Deployment: The app can be deployed on any cloud service (e.g., AWS, Heroku) as long as Flask is supported.

2. Key Features
   
a. Real-Time Data Retrieval:
The chatbot can fetch live stock prices (using the Alpha Vantage API) and cryptocurrency prices (using the CoinGecko API).
b. Natural Language Processing (NLP):
spaCy is used to process and clean user queries, making it easier to extract relevant financial information.
c.Interactive Chat Interface:
Users interact with the chatbot via a simple text interface. They can ask about stock prices or cryptocurrency prices, and the chatbot responds in real time.

3. Frontend Design
   
Styling:
The chatbot is styled with a background image that fills the screen, and the text is displayed over a semi-transparent chat box for readability.
The user interface includes a responsive chat container with input fields and buttons for sending messages.
Responsive Design:
The chat window adjusts to different screen sizes (including mobile devices) using responsive CSS techniques. It ensures the chatbot remains usable on smaller screens by scaling down components as needed.
User Input:
Users can type their queries in a text input field, and submit them via the "Send" button. The chatbot responds dynamically with real-time information about the stock or cryptocurrency prices.

4. Backend Logic and Functionality

a. Flask Routes:
/ - Serves the main index.html page.
/chat - Processes the user’s query, extracts relevant financial data (stock price or cryptocurrency price), and responds with the requested information.
b. Data Retrieval:
Stock Data:
When the user asks about a stock's price (e.g., "What is the stock price of Tesla?"), the backend uses the Alpha Vantage API to fetch real-time stock price data.
Crypto Data:
For cryptocurrency queries (e.g., "What is the price of Bitcoin?"), the backend uses the CoinGecko API to fetch live cryptocurrency prices.
c. Error Handling:
If the stock or crypto symbol is not found or an API call fails, the backend returns a message informing the user about the error.
d. Query Processing with spaCy:
The user's input is cleaned using spaCy to remove special characters and convert the query into a simpler format. This helps in extracting key entities (company or cryptocurrency name).
e. API Response Formatting:
After retrieving the data from the APIs, the backend formats it into a user-friendly response, which is then sent back to the frontend for display.

5. Code Summary

HTML (Frontend):
The HTML contains the structure of the chatbot, including:
A chat box where messages are displayed.
A user input section with a text field and a send button.
CSS (Styling):
The CSS includes styles for the chat container, messages, and input fields. The page background is set to an image, and the chat container is styled with a semi-transparent black background.
JavaScript (Frontend Interaction):
The JavaScript (via jQuery) handles user interaction:
When the user types a message and clicks the "Send" button, an AJAX POST request is made to the /chat endpoint, sending the user's query.
The bot's response is appended to the chat box, and the input field is cleared.
Python (Backend - Flask):
Flask serves the chatbot page and processes user input.
The chatbot interacts with Alpha Vantage and CoinGecko APIs to fetch live financial data.
The backend uses spaCy for query normalization and NLP processing.

6. How It Works

Frontend Interaction:
The user types a query (e.g., "What is the stock price of Apple?") in the input field.
Upon clicking the "Send" button, the query is sent to the Flask backend using an AJAX request.
The backend processes the query, fetches the necessary data, and sends back a response (e.g., the stock price of Apple).
Backend Data Processing:
The backend processes the user's query, checking for stock-related or crypto-related keywords.
It then fetches real-time data from the corresponding API (Alpha Vantage or CoinGecko).
The data is formatted and returned to the frontend, where it is displayed in the chat window.
System Architecture Flow-
<img width="362" alt="image" src="https://github.com/user-attachments/assets/3f7148b7-95bb-41b2-b6d8-212c804e62da" />

7. Potential Improvements

Expanding API Integrations:
Integrate more financial data sources, such as stock news, earnings reports, or company financials.
Add additional functionality, such as fetching stock performance over a range of time (daily, weekly, monthly).
Enhanced NLP:
Use more advanced NLP techniques to better understand user queries, including handling misspellings, synonyms, and more complex sentence structures.
Multi-Modal Data:
Consider displaying additional information in the form of graphs or charts (using libraries like Plotly or Chart.js) to visualize financial data.
User Accounts and Personalization:
Integrate banking APIs (e.g., Plaid) to allow users to track their personal finances, portfolio, and investments.
