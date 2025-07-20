import logging
import time

from selenium import webdriver


driver = webdriver.Chrome()

driver.get("http://demostore.supersqa.com")

time.sleep(3)
logging.info(driver.title)

driver.quit()