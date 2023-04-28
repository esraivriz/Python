from githubUserInfo import username, password
from selenium import webdriver
import time
from selenium.webdriver.common.by import By


class Github:
    def __init__(self, username, password):
     self.browser = webdriver.Chrome()
     self.username = username
     self.password = password
     self.followers = []

    def signIn(self):
        self.browser.get("https://github.com/login")
        time.sleep(2)

        self.browser.find_element(By.XPATH, "//input[@id='login_field']").send_keys(self.username)
        self.browser.find_element(By.XPATH, "//input[@id='password']").send_keys(self.password)

        time.sleep(2)

        self.browser.find_element(By.XPATH, "//*[@value='Sign in']").click()

    def getFollowers(self):
          self.browser.get("https://github.com/esraivriz?tab=followers")
          time.sleep(1000)


github = Github(username, password)
github.signIn()  

    


    

    
    
                                          