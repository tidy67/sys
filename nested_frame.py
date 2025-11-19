from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/nested_frames")
time.sleep(10)

driver.switch_to.frame("frame-top")
time.sleep(10)
print("Switched to top frame")

driver.switch_to.frame("frame-left")
time.sleep(10)
print("Switched to left frame")

left_frame = driver.find_element(By.TAG_NAME, "body")
print("left frame text", left_frame.text)

driver.switch_to.parent_frame()
print("Switched to parent frame")

driver.switch_to.frame("frame-middle")
print("Switched to middle frame")

middle_frame = driver.find_element(By.TAG_NAME, "body")
print("middle frame text", middle_frame.text)

driver.switch_to.parent_frame()
print("Switched to parent frame")

driver.switch_to.default_content()
time.sleep(10)

driver.switch_to.frame("frame-bottom")
bottom_frame = driver.find_element(By.TAG_NAME, "body")
print("bottom frame text", bottom_frame.text)

driver.quit()
