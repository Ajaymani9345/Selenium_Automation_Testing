import chromedriver_autoinstaller
chromedriver_autoinstaller.install()  # Automatically downloads and sets up ChromeDriver

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
# Launch browser and open Google
driver = webdriver.Chrome()
driver.get("https://www.google.com")

# Enter search query
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Python Selenium")
search_box.send_keys(Keys.RETURN)

time.sleep(70)
WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CSS_SELECTOR, "h3"))
)

# Get and print first 5 result titles
results = driver.find_elements(By.CSS_SELECTOR, "h3")[:5]
for r in results:
    print(r.text)

driver.quit()