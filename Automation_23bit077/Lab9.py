import chromedriver_autoinstaller
chromedriver_autoinstaller.install()  
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/checkboxes")
time.sleep(40)
checkboxes = driver.find_elements(By.CSS_SELECTOR, "input[type='checkbox']")
for cb in checkboxes:
    cb.click()
    print("Checked:", cb.is_selected()) 
driver.quit()