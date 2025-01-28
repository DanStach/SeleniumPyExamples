from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
import time

# ARRANGE
driver = webdriver.Chrome()
expTitle = 'NCR Voyix'
expArtURL = 'https://www.ncrvoyix.com/restaurant/contact'

# ACT
# navigate to site
driver.get('https://www.ncrvoyix.com/')
driver.implicitly_wait(2.0)
title = driver.title

# ASSERT
# Check title text
assert title == expTitle , "Issue: Title mismatch. Exp: " + expTitle + " Found: " + title


# ACT 
# navigate to restaurant then restaurant type quick service
linkRestaurant = driver.find_element(By.XPATH, '//*[@class="navbar_link-text w-nav-link"]')
linkRestaurant.click()

drpdwnRest = driver.find_element(By.ID, 'w-dropdown-toggle-1')
actions = ActionChains(driver)
actions.move_to_element(drpdwnRest).perform()
time.sleep(3) ## demo only: pause to  watch screen :)

linkQuickService= driver.find_element(By.XPATH, '//div[@class="navbar_menu-dropdown w-dropdown"]//a[contains(text(),"Quick Service")]')
linkQuickService.click()
time.sleep(3) ## demo only: pause to  watch screen :)

# click "ask us how" button 
linkQuickService= driver.find_element(By.XPATH, '//a[contains(text(),"Ask us how")]')
linkQuickService.click()
time.sleep(3) ## demo only: pause to  watch screen :)

# start to fill out form
# do not complete or I will get marked as a bot...
txtFirstName = driver.find_element(By.XPATH, '//input[@id="FirstName"]')
txtLastName = driver.find_element(By.XPATH, '//input[@id="LastName"]')
txtFirstName.send_keys("DanDan")
txtLastName.send_keys("TheQaMan")
time.sleep(3) ## demo only: pause to  watch screen :)

# ASSERT 
print(driver.current_url)
assert driver.current_url == expArtURL, "ISSUE: unexpected URL Exp: " + expArtURL + " Found: " + driver.current_url

driver.quit()