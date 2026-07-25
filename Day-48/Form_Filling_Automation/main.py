from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://appbrewery.github.io/fake-newsletter-signup/")

first_name = driver.find_element(By.NAME, value="fName")
first_name.send_keys("Herin")

last_name = driver.find_element(By.NAME, value="lName")
last_name.send_keys("Patel")

email = driver.find_element(By.NAME, value="email")
email.send_keys("Hp@gmail.com")

submit_button = driver.find_element(By.CSS_SELECTOR, value=".btn-block")
submit_button.send_keys(Keys.ENTER)