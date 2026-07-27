from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

PROMISED_DOWN = 1000
PROMISED_UP = 1000
Y_EMAIL = "herinpatelza6747@gmail.com"
Y_PASSWORD = "kdCll98XmswRbebQ"
Y_LOGIN_URL = "https://app.100daysofpython.dev/services/y/login"

class InternetSpeedTwitterBot:
    def __init__(self, driver_path=None):
        self.chrome_option = webdriver.ChromeOptions()
        self.chrome_option.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=self.chrome_option)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        
        time.sleep(3)
        
        continue_button = self.driver.find_element(By.XPATH, value='//*[@id="onetrust-accept-btn-handler"]')
        continue_button.click()
        
        time.sleep(3)
        
        go = self.driver.find_element(By.XPATH, value='//*[@id="root"]/div/div[1]/div/div[2]/div[2]/div[2]/div/div/div[2]/div[2]/button')
        go.click()
        
        time.sleep(60)
        
        self.down = self.driver.find_element(By.XPATH, value='//*[@id="root"]/div/div[1]/div/div[2]/div[2]/div[2]/div/div/div/div[2]/div[2]/div[1]/div[1]/div/h3').text
        self.up = self.driver.find_element(By.XPATH, value='//*[@id="root"]/div/div[1]/div/div[2]/div[2]/div[2]/div/div/div/div[2]/div[2]/div[1]/div[2]/div/h3').text

        print(f"Download Speed = {self.down}")
        print(f"Upload Speed = {self.up}")

    def tweet_at_provider(self):
        self.driver.get(Y_LOGIN_URL)
        time.sleep(2)

        self.driver.find_element(By.NAME, value="email").send_keys(Y_EMAIL)
        password = self.driver.find_element(By.NAME, value="password")
        password.send_keys(Y_PASSWORD)
        password.send_keys(Keys.ENTER)

        time.sleep(3)
        tweet_compose = self.driver.find_element(By.CSS_SELECTOR, value='div[aria-label="Post text"]')
        tweet = f"Hey Internet Provider, why is my speed {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?!"
        tweet_compose.send_keys(tweet)

        time.sleep(2)
        tweet_button = self.driver.find_element(By.CSS_SELECTOR, value='.x-compose-form button')
        tweet_button.click()

        time.sleep(2)
        self.driver.quit()


bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider()