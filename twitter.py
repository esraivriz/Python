
from twitterUserInfo import username, password
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
class Twitter:
    def __init__(self, username, password):
        self.browserProfile = webdriver.ChromeOptions()
        self.browserProfile.add_experimental_option(
            "prefs", {"intl.accept_languages": "en,en_US"}
        )
        self.browser = webdriver.Chrome(
            "chromedriver.exe", chrome_options=self.browserProfile
        )
        self.username = username
        self.password = password

    def signIn(self):
        self.browser.get("https://twitter.com/i/flow/login")
        time.sleep(2)
        usernameInput = self.browser.find_element(By.CSS_SELECTOR, '[name="text"]')
        usernameInput.send_keys(username, Keys.ENTER)
        time.sleep(5)
        passwordInput = self.browser.find_element(By.CSS_SELECTOR, '[name="password"]')
        passwordInput.send_keys(password, Keys.ENTER)




    def search(self, hastag):
        searchInput =self.browser.find_element(By.CSS_SELECTOR, '[data-testid="SearchBox_Search_Input"]')
        searchInput.send_keys(hastag)
        time.sleep(2)
        searchInput.send_keys(Keys.ENTER)
        time.sleep(2)

       





        twitter = Twitter(username, password)
        twitter.signIn()
        time.sleep(5)
