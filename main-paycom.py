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
option = webdriver.ChromeOptions()
driver = webdriver.Chrome(options = option)

expTitle = 'Online Payroll Services | HR Payroll Software | Paycom'

# ACT
driver.get('https://www.paycom.com/')
driver.implicitly_wait(2.0)
title = driver.title

#
assert title == expTitle



# hover over resources and click all resources %
drpdwnResources = driver.find_element(By.ID, 'resourcesDropdown')
actions = ActionChains(driver)
actions.move_to_element(drpdwnResources).perform()

time.sleep(3) ## pause to watch screen :)

linkAllRes = driver.find_element(By.XPATH, '//*[@id="navbarSupportedContent"]//a[text()="All Resources"]')
linkAllRes.click()

time.sleep(3) ## pause to watch screen :)

WebDriverWait(driver, 8).until(
    EC.presence_of_element_located((By.XPATH,'//*[@id="search-form-input"]'))
)

time.sleep(3) ## pause to watch screen :)


txtSearchBox = driver.find_element(By.XPATH, '//*[@id="search-form-input"]')
buttonSearch = driver.find_element(By.XPATH, '//*[@id="search-form"]/button')

txtSearchBox.send_keys("test")
time.sleep(3) ## pause to watch screen :)
buttonSearch.click()


WebDriverWait(driver, 8).until(
    EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, 'Pre-employment Testing: Good or Bad?'))
)

driver.find_element(By.PARTIAL_LINK_TEXT, 'Pre-employment Testing: Good or Bad?').click()


time.sleep(6) ## pause to watch screen :)


driver.quit()