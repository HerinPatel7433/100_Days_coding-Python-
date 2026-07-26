from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import csv

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)

# Youtubes first ever "viedo me at zoo".
video_url = "https://www.youtube.com/watch?v=jNQXAC9IVRw" 
driver.get(video_url)
driver.maximize_window()

print("Bypassing video player...")
driver.execute_script("window.scrollBy(0, 600);")
time.sleep(3) 

print("Starting infinite scroll...")
last_height = driver.execute_script("return document.documentElement.scrollHeight")

while True:
    driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
    time.sleep(3) 
    
    new_height = driver.execute_script("return document.documentElement.scrollHeight")
    
    if new_height == last_height:
        print("Reached the bottom of the comments!")
        break
        
    last_height = new_height

print("Extracting data...")
authors = driver.find_elements(By.CSS_SELECTOR, "#author-text")
comments = driver.find_elements(By.CSS_SELECTOR, "#content-text")

filename = 'youtube_comments.csv'
with open(filename, 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Username', 'Comment'])
    
    for author, comment in zip(authors, comments):
        writer.writerow([author.text.strip(), comment.text.strip()])

driver.quit()
print(f"Success! Saved {len(comments)} comments to {filename}.")