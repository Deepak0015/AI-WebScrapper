# AI Web Scraper and Content Extractor

## Overview
This project is an **AI-powered web scraper** that extracts content from a given URL, processes it, and allows users to parse specific information using an AI model API. The application is built using **Python, Selenium, BeautifulSoup, and Streamlit** for a user-friendly interface.

## Features
- **Web Scraping:** Extracts web page content using Selenium and BeautifulSoup.
- **Content Cleaning:** Removes unnecessary elements like scripts and styles.
- **Content Chunking:** Splits long web page content into manageable chunks for processing.
- **AI-Powered Extraction:** Uses **Claude 3.5 Haiku API** to extract relevant information based on user descriptions.
- **Streamlit UI:** Provides an easy-to-use web interface for scraping and querying data.

---

## Installation

### Prerequisites
Ensure you have the following installed:
- **Python 3.x**
- **Firefox & GeckoDriver** (for Selenium WebDriver)
- **Pip Packages** (install using the command below)

### Install Dependencies
```bash
pip install -r requirements.txt
```
(*Ensure `requirements.txt` includes:* `selenium`, `beautifulsoup4`, `requests`, `streamlit`)

---

## Usage

### 1. Start the Streamlit App
Run the following command:
```bash
streamlit run streamlitapp.py
```
This will launch the **AI Web Scraper** in your browser.

### 2. Scrape a Website
- Enter the **URL** of the webpage to scrape.
- Click **Scrape Website** to extract content.
- View cleaned content in the expandable section.

### 3. Extract Information Using AI
- Enter a **description** of the information you want to extract.
- Click **Parse Content** to get AI-extracted results.

---

## Project Structure
```
├── prompt.py          # AI model integration with Claude 3.5 Haiku API
├── scrap.py           # Web scraping logic using Selenium & BeautifulSoup
├── streamlitapp.py    # Streamlit web app for user interface
├── requirements.txt   # List of required Python dependencies
└── README.md          # Project documentation
```

---

## Files Breakdown

### `scrap.py` (Web Scraper)
- Uses **Selenium** to load web pages in headless mode.
- Extracts and cleans the **main content** using **BeautifulSoup**.
- Splits long content into smaller **chunks** (default size: 6000 characters).

### `prompt.py` (AI Processing)
- Sends extracted **content chunks** and **user queries** to the Claude 3.5 Haiku API.
- Returns relevant extracted information based on user descriptions.

### `streamlitapp.py` (User Interface)
- Provides a **Streamlit**-based UI for users.
- Allows input of URLs and queries.
- Displays extracted results in a structured format.

---

## How It Works
1. **Scrape a website** → Extract & clean webpage content.
2. **Store the content** (ensuring that the same page is not processed multiple times).
3. **Ask AI for specific details** → AI extracts relevant info **only once** for each unique URL.
4. **New website = New processing**, preventing redundant requests.

---

## Future Improvements
- Add support for **multiple scraping sources** (PDFs, JSON, etc.).
- Improve AI query optimization for **faster responses**.
- Implement a **local LLM model** (optional) to avoid API dependency.

---

## Contributing
Feel free to submit **pull requests** or open **issues** to improve the project.

---

## License
This project is **open-source** under the **MIT License**.
