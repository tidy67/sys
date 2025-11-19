from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/javascript_alerts")

# confirm_button = driver.find_element(By.XPATH, "//button[text()='Click for JS Confirm']")
confirm_button = driver.find_element(By.XPATH, "//*[@id='content']/div/ul/li[2]/button")
time.sleep(2)
confirm_button.click()
time.sleep(2)



alert = driver.switch_to.alert
print("Alert text : ", alert.text)
# alert.accept()
alert.dismiss()
time.sleep(2)
# print("Alert text : ", alert.text)

result = driver.find_element(By.ID, "result")
print("Page result after dismissing alert :",result.text)

driver.quit()

