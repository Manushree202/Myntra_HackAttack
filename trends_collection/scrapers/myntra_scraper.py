import requests
from bs4 import BeautifulSoup

def scrape_myntra_trends(url):
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Failed to load page {url}")

    soup = BeautifulSoup(response.content, 'html.parser')
    
    trends = []
    for item in soup.select('.myntra-trend-title'):  # Adjust the selector as needed
        trends.append(item.get_text(strip=True))
    
    return trends
