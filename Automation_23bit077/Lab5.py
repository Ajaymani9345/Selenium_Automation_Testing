import chromedriver_autoinstaller
chromedriver_autoinstaller.install()  
from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get("https://www.google.com")
driver.save_screenshot("google.png")
time.sleep(20)
print("Screenshot saved!")

driver.quit()