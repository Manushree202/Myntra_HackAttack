import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_fashion_blogs(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    articles = soup.find_all('article')
    data = []
    for article in articles:
        title = article.find('h2').text
        content = article.find('p').text
        data.append({'title': title, 'content': content})
    
    return pd.DataFrame(data)

url = 'https://examplefashionblog.com'
df = scrape_fashion_blogs(url)
df.to_csv('fashion_blogs.csv', index=False)
