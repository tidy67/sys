import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://google.com")
time.sleep(10)
driver.maximize_window()

searchtxtbox = driver.find_element(By.NAME, "q")
print(searchtxtbox.rect)

g_logo = driver.find_element(By.XPATH,"(//*[name()='svg'][@aria-label='Google'])[1]")
g_logo.screenshot("logo.png")
driver.save_screenshot("fullscreen.png")
# //*[@id="logo"]
# /html/body/ntp-app//div/ntp-logo//div

print(driver.get_cookies())
print(driver.get_cookie('NID'))
print(driver.get_cookie('AEC'))

driver.set_window_rect(100,200,300,400)
time.sleep(10)