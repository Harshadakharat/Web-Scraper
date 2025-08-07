import requests
from bs4 import BeautifulSoup

def scrape_headlines(url):
    
    response = requests.get(url)
    
    
    if response.status_code != 200:
        print("Failed to retrieve the webpage")
        return

    
    soup = BeautifulSoup(response.text, 'html.parser')

    
    headlines = soup.find_all('h3')  

    print("News Headlines:\n")
    for index, headline in enumerate(headlines, start=1):
        text = headline.get_text(strip=True)
        if text:
            print(f"{index}. {text}")

scrape_headlines("https://www.bbc.com/news")