# Importing required libraries
import requests
from bs4 import BeautifulSoup
import time

# Define an optimized web scraper class
class OptimizedScraper:
    
    # Initialize the scraper with base URL and optional headers
    def __init__(self, base_url, headers=None):
        self.base_url = base_url  # Set base URL
        self.session = requests.Session()  # Create a session for persistent connections
        
        # If headers are provided, use them; otherwise, set a default user-agent header
        if headers:
            self.headers = headers
        else:
            self.headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
            }
    
    # Method to fetch content from a given URL
    def fetch_content(self, url):
        try:
            # Make a GET request to the URL using the provided headers
            response = self.session.get(url, headers=self.headers)
            response.raise_for_status()  # Raise an error if the response contains an HTTP error status code
            return response.content  # Return the content of the response
        except requests.HTTPError as http_err:  # Handle HTTP errors
            print(f'HTTP error occurred: {http_err}')
            return None
        except Exception as err:  # Handle other possible exceptions
            print(f'Other error occurred: {err}')
            return None

    # Method to parse the fetched content and extract required data
    def parse_content(self, content):
        # Parse the content using BeautifulSoup
        soup = BeautifulSoup(content, 'html.parser')
        
        # Example: Extract text from all divs with class 'specific-class'
        data_divs = soup.find_all('div', class_='specific-class')
        data = [div.text for div in data_divs]
        
        return data

    # Method to scrape data from a specific endpoint of the base URL
    def scrape(self, endpoint):
        # Construct the full URL
        full_url = self.base_url + endpoint
        # Fetch content from the URL
        content = self.fetch_content(full_url)
        
        # If content was fetched successfully, parse and return the data; otherwise, return an empty list
        if content:
            return self.parse_content(content)
        else:
            return []

# Main execution starts here
if __name__ == "__main__":
    # Create an instance of the OptimizedScraper class with a base URL
    scraper = OptimizedScraper(base_url='https://example.com')

    # List of endpoints to scrape
    endpoints_to_scrape = ['/page1', '/page2', '/page3']  # Just an example
    
    # Loop through each endpoint, scrape data, and print the results
    for endpoint in endpoints_to_scrape:
        data = scraper.scrape(endpoint)
        print(data)
        
        # Introduce a delay between requests to avoid overwhelming the server
        time.sleep(2)
