from bs4 import BeautifulSoup
import requests
# import lxml
# with open('bs4-start/website.html', 'r') as file:
#     contents = file.read()
# soup = BeautifulSoup(contents, 'html.parser')


# for tag in soup.find_all(name='a'):
#     print(tag.get('href'))

# h3 = soup.find_all('h3', class_='heading')
# print(h3)
# name = soup.select_one(selector='p a')
# print(name)

# headings = soup.select(selector='.heading') # . for class, # for id
# print(headings)

# print(soup.prettify())
response = requests.get('https://news.ycombinator.com/news')
# print(response.text)

soup = BeautifulSoup(response.text, 'html.parser')

# article_tag = soup.select_one('.titleline a')  
# print(article_tag.getText())
# # article_link = article_tag.get('href')
# # print(article_link)
# # article_upvote = soup.select_one('.subtext .score').getText()
# # print(article_upvote)

# article_tag = soup.find(name='span', class_='titleline')  
# print(article_tag.getText())    

# articles_tag = soup.find_all(name='span', class_='titleline')
# for article in articles_tag:
#     print(article.getText())
#     print(article.find(name='a').get('href'))
#     # print(article.find(name='span', class_='score'))
#     print('\n')

article_upvote = [int(score.getText().split()[0]) for score in soup.find_all(name='span', class_='score')] 
print(article_upvote) 
articles_tag = soup.find_all(name='tr', class_='athing submission')
count = 0
for article in articles_tag:
    article_in = article.find(name='span', class_='titleline')
    print(article_in.getText())
    print(article_in.find(name='a').get('href'))
    if count <= len(article_upvote) - 1:
        print(article_upvote[count])
    print('\n')
    count += 1
