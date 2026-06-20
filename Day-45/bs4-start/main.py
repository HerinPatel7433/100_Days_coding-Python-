from bs4 import BeautifulSoup
# use import lxml if html parser does not work 

with open("Day-45\\bs4-start\\website.html") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")
print(soup.title)
print(soup.title.name)
print(soup.title.string)

all_anchor_tag = soup.find_all(name="a")

for tag in all_anchor_tag:
    print(tag.getText())
    print(tag.get("href"))

heading = soup.find(name="h1", id="name")
print(heading)

section_heading = soup.find(name="h3", class_="heading")
print(section_heading)