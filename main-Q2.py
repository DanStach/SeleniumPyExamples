from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver import ActionChains
from selenium.webdriver.common.action_chains import ActionChains

import time

# ARRANGE
driver = webdriver.Chrome()
driver.implicitly_wait(2.0)
driver.set_window_size(1500,800)

navUrlHome = 'https://www.q2.com/'
expTitleHomePage = "Digital Banking Solutions for Banks and Credit Unions | Q2"
expArtURL = ''

cssMainCompany = '#primary-menu > ul > li.hs-menu-item.hs-menu-depth-1.hs-item-has-children.open > div.hs-menu-item-text > span' # css selector is fragile 
xpathCompanyWork = '//*[@data-menu-label="Company"]' # xpath is stable and simple
xpathCompanyWorkNews = '//*[@data-menu-label="News"]' # xpath is stable and simple
xpathNewsQ2inNews = '//*[@data-menu-label="Q2 in the News"]'

xpathBtnCloseOneTrust =  '//*[@id="onetrust-close-btn-container"]'


# ACT
# navigate to site
driver.get(navUrlHome)
title = driver.title

# ASSERT
# Check title text
assert title == expTitleHomePage , "Issue: Title mismatch. Exp: " + expTitleHomePage + " Found: " + title


# ACT 
# find and click on Company - News - Q2 in news
drpdwnCompany = driver.find_element(By.XPATH, xpathCompanyWork)
actions = ActionChains(driver)
actions.move_to_element(drpdwnCompany).perform()
drpdwnCompany.click()
time.sleep(2) ## sleeps are bad... but good for demos  

sidebarNews = driver.find_element(By.XPATH, xpathCompanyWorkNews)
sidebarNews.click()
time.sleep(2) ## sleeps are bad... but good for demos 

sidebarQ2inNews = driver.find_element(By.XPATH, xpathNewsQ2inNews)
sidebarQ2inNews.click()
time.sleep(2) ## sleeps are bad... but good for demos 


# search for austin
txtSearchBox = driver.find_element(By.XPATH, '//input[@class="search-form__input"]')
buttonSearch = driver.find_element(By.XPATH, '//button[@class="search-form__submit"]')
txtSearchBox.send_keys("austin")
time.sleep(3) ## pause to watch screen :)
buttonSearch.click()
time.sleep(3) ## pause to watch screen :)



# ASSERT 
print(driver.current_url)
assert driver.current_url == expArtURL, "ISSUE: unexpected URL Exp: " + expArtURL + " Found: " + driver.current_url

driver.quit()