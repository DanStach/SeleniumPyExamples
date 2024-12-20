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
expTitle = 'Online Payroll Services | HR Payroll Software | Paycom'
expArtURL = 'https://www.paycom.com/resources/blog/pre-employment-testing-good-bad/'

# ACT
# navigate to site
driver.get('https://www.paycom.com/')
driver.implicitly_wait(2.0)
title = driver.title

# ASSERT
# Check title text
assert title == expTitle , "Issue: Title mismatch. Exp: " + expTitle + " Found: " + title


# ACT 
# hover over resources and click "all resources" 
drpdwnResources = driver.find_element(By.ID, 'resourcesDropdown')
actions = ActionChains(driver)
actions.move_to_element(drpdwnResources).perform()
time.sleep(3) ## demo only: pause to  watch screen :)

linkAllRes = driver.find_element(By.XPATH, '//*[@id="navbarSupportedContent"]//a[text()="All Resources"]')
linkAllRes.click()
time.sleep(3) ## demo only: pause to  watch screen :)

WebDriverWait(driver, 8).until(
    EC.presence_of_element_located((By.XPATH,'//*[@id="search-form-input"]'))
)
time.sleep(3) ## demo only: pause to  watch screen :)


# search for "test"
txtSearchBox = driver.find_element(By.XPATH, '//*[@id="search-form-input"]')
buttonSearch = driver.find_element(By.XPATH, '//*[@id="search-form"]/button/i')
txtSearchBox.send_keys("test")
time.sleep(3) ## pause to watch screen :)
buttonSearch.click()

# look for article "Pre-employment Testing"
WebDriverWait(driver, 8).until(
    EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, 'Pre-employment Testing: Good or Bad?'))
)
elArticlePreEmployment = driver.find_element(By.PARTIAL_LINK_TEXT, 'Pre-employment Testing: Good or Bad?')
elArticlePreEmployment.click()
time.sleep(3) ## pause to watch screen :)

# ASSERT 
print(driver.current_url)
assert driver.current_url == expArtURL, "ISSUE: unexpected URL Exp: " + expArtURL + " Found: " + driver.current_url

driver.quit()