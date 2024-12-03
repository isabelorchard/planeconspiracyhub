import requests
from bs4 import BeautifulSoup

def fetch_news():
url = "https://news.google.com/search?for=airplane+disappeared&hl=en-GB&gl=GB&ceid=GB%3Aen"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

    news_list = []
    for article in soup.find_all("a", class_="DY5T1d"):
        title = article.text
        link = "https://news.google.com" + article['href'][1:]
        news_list.append({"title": title, "link": link})

    return news_list