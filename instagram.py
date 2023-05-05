import time
from instagramUserInfo import username, password
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
class Instagram:
    def __init__(self, username, password):
        self.browserProfile = webdriver.ChromeOptions()
        self.browserProfile.add_experimental_option(
            'prefs', {'intl.accept_languages': 'en,en_US'})
        self.browser = webdriver.Chrome(
            'chromedriver.exe', chrome_options=self.browserProfile)
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
    def getFollowers(self, max):
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

        with open("followers.txt","w",encoding="UTF-8") as file:
            for item in updatedList:
                file.write(f"https://instagram.com/{item.text}/"+ "\n")

    def followUserList(self, username):
        if type(username) == str:
            self.browser.get("https://instagram.com/"+username)
            time.sleep(2)
            followButton = self.browser.find_element(By.TAG_NAME, "button")
            if followButton.text != "Following":
                followButton.click()
                time.sleep(2)
            else:
                print('Zaten Takiptesin')
            print(followButton.text)
        elif type(username) == list:
            for user in username:
                self.browser.get("https://instagram.com/"+user)
                time.sleep(3)
                followButton = self.browser.find_element(By.TAG_NAME, "button")
                if followButton.text != "Following":
                    time.sleep(3)
                    followButton.click()
                    time.sleep(3)
                else:
                    print('Zaten Takiptesin')
                print(followButton.text)
        else:
            print("String veya string list giriniz")
            SystemExit


    def unFollowUser(self,username):
        self.browser.get("https://instagram.com/"+username)
        time.sleep(2)

        followButton = self.browser.find_element(By.TAG_NAME, "button")
        if followButton.text == "Following":
            followButton.click()
            time.sleep(2)

            confirmButton = self.browser.find_element(By.XPATH,('//span[text()="Unfollow"]'))
            confirmButton.click()

        else :
            print("Zaten takip etmiyorsun")   





instagrm = Instagram(username, password)
instagrm.sign_in()
instagrm.getFollowers()
# instagrm.followUser("kod_evreni")
#instagrm.followUserList(11)
#instagrm.followUserList(["kod_evreni","mevlut_orcan","caramellhobi"])  list için ya köşeli parantez yapıcaz ya da list yazıp normal parantezde tanımlarız
#instagrm.unFollowUser('kod_evreni')
time.sleep(15)