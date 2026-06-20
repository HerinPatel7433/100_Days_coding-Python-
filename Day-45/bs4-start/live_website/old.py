from bs4 import BeautifulSoup
import requests

# use this to get the data from the website.
response = requests.get("https://news.ycombinator.com/news") 

# use this to get the html text from the website.
web_page = response.text

# use to convert raw html text int structured , searchable tree of python object.
soup = BeautifulSoup(web_page, "html.parser")

link_element = soup.select('.titleline > a')
score = soup.select('.score')

# old code using two separate for loops 
# for _ in link_element:
#     link_text = _.get_text(strip=True)
#     link_href = _.get('href')
    
#     print(f"Text: {link_text}")
#     print(f"Link: {link_href}")

# for _ in score:
#     score_text = _.getText(strip=True)
    
#     print(score_text)


soup = BeautifulSoup(web_page, "html.parser")

link_element = soup.select('.titleline > a')
score = soup.select('.score')

# Use zip() to iterate through both lists at the same time
for link, scr in zip(link_element, score):
    link_text = link.get_text(strip=True)
    link_href = link.get('href')
    score_text = scr.get_text(strip=True)
    
    print(f"Text: {link_text}")
    print(f"Link: {link_href}")
    print(f"Score: {score_text}")
    print("-" * 40) 