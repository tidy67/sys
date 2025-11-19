# from selenium import webdriver
# import time
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
#
#
# driver = webdriver.Chrome()
#
# driver.get("https://www.facebook.com/")
# time.sleep(10)
#
# ac_button = driver.find_element(By.XPATH,"//*[@id='u_0_0_IR']")
# ac_button.click()
# time.sleep(36000)

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("https://www.facebook.com")

wait = WebDriverWait(driver, 3000)

# Try to find a more reliable selector than dynamic ID
create_account_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT,'Create new account')))
create_account_button.click()

# registration_form = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='reg']")))
# "//form[@id='reg"
# registration_form.click()

registration_form = wait.until(EC.presence_of_element_located((By.NAME,'reg')))

fname = wait.until(EC.presence_of_element_located((By.NAME,'firstname')))
lname = wait.until(EC.presence_of_element_located((By.NAME,'lastname')))
mobile = wait.until(EC.presence_of_element_located((By.NAME,'reg_email__')))
password = wait.until(EC.presence_of_element_located((By.NAME,'reg_passwd__')))

fname.send_keys('Yourname')
lname.send_keys('Yoursurname')
mobile.send_keys('9087567545')
password.send_keys('PASSWORD@123')

day = wait.until(EC.presence_of_element_located((By.ID,'day')))
month = wait.until(EC.presence_of_element_located((By.ID,'month')))
year = wait.until(EC.presence_of_element_located((By.ID,'year')))

day.send_keys('28')
month.send_keys('sept')
year.send_keys('2003')

gender_male = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@value='2']")))
gender_female = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@value='1']")))
gender_custome = wait.until(EC.presence_of_element_located((By.XPATH,"//input[@value='-1']")))

gender_female.click()
time.sleep(3)

sign_up_button = wait.until(EC.presence_of_element_located((By.NAME,'websubmit')))
sign_up_button.click()

confirmation_message_wait = WebDriverWait(driver,120)
confirmation_message = confirmation_message_wait.until(
    EC.presence_of_element_located((By.XPATH,"//div[contains(text(),'confirmation')]")))
print("user created successfully!")

time.sleep(10)

