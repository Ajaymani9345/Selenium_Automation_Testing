import chromedriver_autoinstaller
chromedriver_autoinstaller.install()  # Automatically downloads and sets up ChromeDriver

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/login")

# Enter credentials
driver.find_element(By.ID, "username").send_keys("tomsmith")
driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")

# ✅ Correct locator for login button
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

# Get and print the login message
message = driver.find_element(By.ID, "flash").text
time.sleep(20)
print("Message:", message)

driver.quit()