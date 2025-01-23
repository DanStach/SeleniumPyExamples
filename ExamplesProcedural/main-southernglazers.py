from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver import ActionChains
from selenium.webdriver.common.action_chains import ActionChains

import time

# ARRANGE
driver = webdriver.Chrome()
driver.implicitly_wait(2.0)

navUrlHome = 'https://www.southernglazers.com/'
expTitleHomePage = "Southern Glazer's"
expArtURL = 'https://www.southernglazers.com/careers/culture'

cssJoinTeam = '#navigation-2f1eadac33-cta-megaMenu-3' # css selector is fragile 
xpathJoinTeam = '//*[@title="Join the team"]'
xpathCulture = '//*[@title="Culture"]'
xpathNewsTalking = '//div[@id="so-good-that-people-are-talking"]'
xpathNewsFeatured = '//h2[contains(text(), "Featured News")]'
xpathBtnCloseOneTrust =  '//*[@id="onetrust-close-btn-container"]'


# ACT
# navigate to site
driver.get(navUrlHome)
title = driver.title

# ASSERT
# Check title text
assert title == expTitleHomePage , "Issue: Title mismatch. Exp: " + expTitleHomePage + " Found: " + title


# ACT 
# close onetrust
driver.find_element(By.XPATH, xpathBtnCloseOneTrust).click()

# find and click on culture page
drpdwnJoinTeam = driver.find_element(By.XPATH, xpathJoinTeam)
actions = ActionChains(driver)
actions.move_to_element(drpdwnJoinTeam).perform()
time.sleep(2) ## demo use only. I hate sleep functions 

linkCulture = driver.find_element(By.XPATH, xpathCulture)
linkCulture.click()
time.sleep(2) ## demo only: pause to  watch screen :)

# scroll down page ""
elNewsTalking =  driver.find_element(By.XPATH, xpathNewsTalking)
driver.execute_script("arguments[0].scrollIntoView();",elNewsTalking )
time.sleep(4) ## demo only: pause to  watch screen :)


# ASSERT 
print(driver.current_url)
assert driver.current_url == expArtURL, "ISSUE: unexpected URL Exp: " + expArtURL + " Found: " + driver.current_url

driver.quit()