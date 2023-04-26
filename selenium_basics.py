from selenium import webdriver
import time
driver = webdriver.Chrome()
url = "https://www.amazon.com"
driver.get(url)
time.sleep(2)
driver.maximize_window()
driver.save_screenshot("amazon.com-homepage.png")
print(driver.title)

url = "https://www.trendyol.com"
driver.get(url)
print(driver.title)

if "Trendyol" in driver.title:
    driver.save_screenshot("trendyol.png")
time.sleep(2)
driver.back()
time.sleep(2)
# driver.forward() sayfayı ılerıkı sayfaya alır
driver.close()