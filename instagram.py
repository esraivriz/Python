import time
from instagramUserInfo import username, password
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
class Instagram:
       # toplu yoruma almak ıcın ıstedıgın yerı sec ctrl+k+c
       # toplu yorumdan kaldırmak icin istedigin yeri sec ctrl+k+u
    def __init__(self, username, password):
        browserProfile = webdriver.ChromeOptions()
        browserProfile.add_experimental_option('prefs', {'intl.accept_languages' : 'en,en_US'})
        self.browser = webdriver.Chrome('chromedriver.exe', chrome_options = self.browserProfile)
        self.username = username
        self.password = password
    def sign_in(self):
        self.browser.get('https://www.instagram.com/accounts/login/')
        time.sleep(2)
        email = self.browser.find_element(
            By.XPATH, "//*[@id='loginForm']/div/div[1]/div/label/input")
        password = self.browser.find_element(
            By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
        time.sleep(3)
        email.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.ENTER)
        time.sleep(5)
        # self.browser.find_element(
        #     By.XPATH, '//*[@id="mount_0_0_8M"]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/div').click()
    def getFollowers(self):
        self.browser.get(f"https://instagram.com/{self.username}/followers")
        time.sleep(5)
        followerList = self.browser.find_elements(
            By.XPATH, "//span[@class='_aacl _aaco _aacw _aacx _aad7 _aade']")
        follower_count = len(followerList)
        action = webdriver.ActionChains(self.browser)
        action.key_down(Keys.TAB).key_up(Keys.TAB).perform()
        action.key_down(Keys.TAB).key_up(Keys.TAB).perform()

        while True:
            action.key_down(Keys.END).key_up(Keys.END).perform()
            time.sleep(1)
            new_count = len(self.browser.find_elements(
                By.XPATH, "//span[@class='_aacl _aaco _aacw _aacx _aad7 _aade']"))
            time.sleep(2)
            if follower_count != new_count:
                follower_count = new_count
                print(f'second count : {new_count}')
                time.sleep(2)
            else:
                break
            updatedList = self.browser.find_elements(
                By.XPATH, "//span[@class='_aacl _aaco _aacw _aacx _aad7 _aade']")
        for i in updatedList:
            print(f"https://instagram.com/{i.text}/")

    def followUser(self,username):
        self.browser.get("https:www.instagram.com/"+ username)
        time.sleep(2)

    def followUserList(self,usernameList):
        for user in usernameList:
            self.browser.get("https:www.instagram.com/"+user)        
   

        followButton = self.browser.find_element(By.TAG_NAME, "button")
        print(followButton.text)

        if followButton.text != "Following":
            followButton.click()
            time.sleep(2)

        else:
            print("Zaten takiptesin")
            print(followButton.text)

    
instagrm = Instagram(username, password)
instagrm.sign_in()
#instagrm.getFollowers()

instagrm.followUser("kod_evreni","caramellhobi")
# list = ["kod_evreni",""]








