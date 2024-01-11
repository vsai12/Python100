import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
resp = requests.get(URL)
resp.raise_for_status()

soup = BeautifulSoup(resp.text, "html.parser")
scrape_titles = soup.find_all(name="h3", class_="title")
scrape_titles.reverse()

with open("movies.txt", "w") as file:
    for title in scrape_titles:
        file.write(f"{title.get_text()}\n")



