import chromedriver_autoinstaller
chromedriver_autoinstaller.install()  
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://www.wikipedia.org/")
search_box = driver.find_element(By.NAME, "search")
search_box.send_keys("Selenium (software)")
search_box.send_keys(Keys.RETURN)
time.sleep(10)
first_paragraph = driver.find_element(By.CSS_SELECTOR, "p").text
print("First Paragraph:", first_paragraph)
driver.quit()