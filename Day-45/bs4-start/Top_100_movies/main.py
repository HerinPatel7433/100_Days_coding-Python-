from bs4 import BeautifulSoup
import requests

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
web_page = response.text
soup = BeautifulSoup(web_page, "html.parser")

movie_element = soup.select('h3.title')

movie_data = []
for movie in movie_element:
    title = movie.get_text().strip()
    if ")" in title:
        split_title = title.split(") ", 1)
    else:
        split_title = title.split(": ", 1)
    movie_data.append(split_title[1])

movie_data.reverse()

with open('Day-45\\bs4-start\\Top_100_movies\\movie.txt', 'w', encoding="utf-8") as file:
    for i, movie in enumerate(movie_data, start=1):
        file.write(f"{i}) {movie}\n")