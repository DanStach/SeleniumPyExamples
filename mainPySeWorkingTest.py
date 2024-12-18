from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

# very simple test to ensure everything is working
option = webdriver.ChromeOptions()
driver = webdriver.Chrome(options = option)

driver.get('https://www.google.com/')

time.sleep(5)
driver.quit()
