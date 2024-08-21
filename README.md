# Stock News Feed :zap: (This is a project from FreeCodeCamp)

## Overview

This project is a Stock News Feed application that aggregates financial news from various sources, uses Machine Learning to identify organizations mentioned in the news, and displays their stock information in real-time graphs. The application is built using Python and utilizes popular libraries such as SpaCy for Natural Language Processing (NLP), yFinance for stock data, and Streamlit for the user interface.

## Features

- **News Aggregation**: Pulls financial news from multiple RSS feeds.
- **Natural Language Processing (NLP)**: Uses SpaCy to extract organization names from the news headlines.
- **Real-Time Stock Data**: Retrieves stock information such as current price, day high/low, forward PE, and dividend yield using yFinance.
- **Interactive UI**: Displays the extracted stock data in an interactive table and provides expandable sections for viewing the latest financial news.
- **Customizable RSS Feeds**: Users can input their own RSS feed links to fetch and analyze news from different sources.

## Technologies Used

- **Python**: Core programming language used for the entire project.
- **SpaCy**: NLP library used to extract organization names from the news headlines.
- **BeautifulSoup**: Used to parse and extract data from RSS feeds.
- **yFinance**: Python library used to retrieve stock market data.
- **Streamlit**: Framework used to build the interactive web interface.
- **Pandas**: For data manipulation and analysis.
- **Requests**: To make HTTP requests for fetching RSS feed data.

## Installation and Setup

### Prerequisites
- **Python 3.x** installed on your machine.
- Install the necessary Python libraries by running:

    ```bash
    pip install -r requirements.txt
    ```

### Running the Application

1. **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/stock-news-feed.git
    cd stock-news-feed
    ```

2. **Run the Streamlit application**:
    ```bash
    streamlit run app.py
    ```
3. **Access the application**:
    Open your web browser and go to `http://localhost:8501` to view the application.

## How It Works

1. **Extract News Headlines**: The application fetches news headlines from the provided RSS feed links using `requests` and `BeautifulSoup`.
2. **Entity Recognition**: The extracted headlines are processed using SpaCy to identify company names mentioned in the news.
3. **Stock Data Retrieval**: For each identified company, the application fetches real-time stock data from yFinance.
4. **Display**: The data is presented in an interactive table, and users can expand sections to view the full news headlines.

## Customization

- **RSS Feeds**: Users can add their own RSS feed links directly in the application to fetch news from different sources.
- **Data Columns**: The columns displayed in the stock information table can be modified by adjusting the `stock_info_dict` dictionary in the `generate_stock_info` function.
