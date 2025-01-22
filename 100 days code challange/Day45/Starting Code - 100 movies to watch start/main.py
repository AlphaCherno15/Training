import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response = requests.get(URL)
soup = BeautifulSoup(response.text, 'html.parser')

movies = soup.find_all(name='h3', class_='title')
movie_titles = [movie.getText() for movie in movies]

with open('movies.txt', 'w') as file:
    for movie in movie_titles[::-1]: #using [::-1] to reverse the list by slicing
        try:
            file.write(f"{movie}\n")
        except UnicodeEncodeError:
            new = movie.replace('â\x80\x93', "")
            file.write(f"{new}\n")
            # print(f"Couldn't write {new} to file")
            continue
# print(movie_titles)