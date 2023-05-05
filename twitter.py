
from twitterUserInfo import username, password
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

class Twitter:
        def __init__(self, username, password):
                self.browserProfile = webdriver.ChromeOptions()
                self.browserProfile.add_experimental_option('prefs', {'intl.accept_languages': 'en,en_US'})
                self.browser = webdriver.Chrome('chromedriver.exe', chrome_options=self.browserProfile)
                self.username = username
                self.password = password


        def signIn(self):
                self.browser.get("https://twitter.com/login")
                time.sleep(5)

                usernameInput = self.browser.find_element(By.CSS_SELECTOR, '[name="text"]')
                usernameInput.send_keys(self.username)
                
                time.sleep(5)
                passwordInput = self.browser.find_element(By.CSS_SELECTOR, '[name="password"]')
                passwordInput.send_keys(self.password)
                time.sleep(5)
                

              


twitter = Twitter(username, password)
#login
twitter.signIn()
