from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/iframe")
time.sleep(10)

driver.switch_to.frame("mce_0_ifr")
time.sleep(10)
print("Switched to iframe")


iframe_body = driver.find_element(By.TAG_NAME, "body")
time.sleep(2)
iframe_body.send_keys("India")
time.sleep(10)
driver.switch_to.default_content()
time.sleep(2)

main_header = driver.find_element(By.TAG_NAME, "h3")
print("Main Document Header", main_header.text)

driver.quit()
