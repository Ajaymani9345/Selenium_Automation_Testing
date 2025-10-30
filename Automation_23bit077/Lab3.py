import chromedriver_autoinstaller
chromedriver_autoinstaller.install()  
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/dropdown")

# Select "Option 2" from the dropdown
dropdown = Select(driver.find_element(By.ID, "dropdown"))
dropdown.select_by_visible_text("Option 2")

time.sleep(20)

print("Selected:", dropdown.first_selected_option.text)

driver.quit()