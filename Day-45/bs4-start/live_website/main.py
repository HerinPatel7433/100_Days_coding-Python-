from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news") 
web_page = response.text
soup = BeautifulSoup(web_page, "html.parser")

link_elements = soup.select('.titleline > a')
score_elements = soup.select('.score')

links_data = []
for link in link_elements:
    links_data.append({
        "Text": link.get_text(strip=True),
        "Link": link.get('href')
    })

scores_data = []
for scr in score_elements:
    scores_data.append(int(scr.get_text(strip=True).split()[0]))

largest_number = max(scores_data)
largest_index = scores_data.index(largest_number)

print(f"Title: {links_data[largest_index]['Text']}")
print(f"Link: {links_data[largest_index]['Link']}")
print(f"Score: {largest_number}")