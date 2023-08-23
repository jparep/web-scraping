# Optimized Web Scraper

## Description
This project provides an optimized web scraping script designed to efficiently extract data from websites. It's built using Python and leverages the `requests` library for fetching web content and `BeautifulSoup` from the `bs4` library for parsing the HTML content.

## Features

- **Persistent Sessions**: Uses the `requests.Session()` to maintain a persistent connection to the website, which can speed up multiple requests.
- **Error Handling**: Gracefully handles potential HTTP errors or other exceptions during the scraping process.
- **User-Agent**: Sets a default user-agent to mimic a real browser, which can help bypass simple scrapers' restrictions. However, you can also provide custom headers if necessary.
- **Data Parsing**: Extracts specific data from fetched web content. In this example, the script extracts text from `div` elements with a class named `specific-class`.

## How to Use

1. **Initialization**: Create an instance of the `OptimizedScraper` class, providing the base URL of the website you want to scrape.
2. **Scraping**: Call the `scrape()` method with the specific endpoint of the base URL that you want to extract data from.
3. **Output**: The scraped data is printed to the console. In this example, the script scrapes and prints data from three endpoints (`/page1`, `/page2`, `/page3`) of the provided base URL.

## Dependencies

- `requests`: For fetching web content.
- `bs4 (BeautifulSoup)`: For parsing HTML content and extracting data.

## Note

Always ensure you have permission to scrape a website. Respect the terms of service and `robots.txt` of the site. Furthermore, the script introduces a delay between requests to avoid overwhelming the server.
