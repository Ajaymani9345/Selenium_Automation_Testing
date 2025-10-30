import chromedriver_autoinstaller
chromedriver_autoinstaller.install()  # Automatically downloads and sets up ChromeDriver

from selenium import webdriver
import os
import time
# Create screenshots folder if it doesn't exist
os.makedirs("screenshots", exist_ok=True)

driver = webdriver.Chrome()
driver.get("https://www.google.com")

# ✅ Correct path with extension and valid folder
driver.save_screenshot("screenshots/google.png")
time.sleep(40)
print("Screenshot saved!")

driver.quit()