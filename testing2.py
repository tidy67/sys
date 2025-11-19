from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.google.com/")
driver.refresh()
driver.forward()
driver.get("https://www.facebook.com/")
driver.back()
driver.refresh()
driver.get("https://chatgpt.com/")
driver.back()
# driver.quit()
print(driver.page_source)
print(driver.current_url)
print(driver.title)



# single_search_txtbox = driver.find_element(By.XPATH, "//textarea")
# multi_search_txtbox = driver.find_elements(By.XPATH, "//textarea")
# print(type(single_search_txtbox))
# print(type(multi_search_txtbox))
# print(single_search_txtbox)
# print(multi_search_txtbox)

# multi_search_txtbox.send_keys('imcc') # error because list does not have send_keys attribute
# multi_search_txtbox.send_keys(Keys.ENTER)

#
# search_txtbox = driver.find_element(By.XPATH, "//textarea[@name='q']")
# print(type(search_txtbox))
# search_txtbox.send_keys('imcc')
# # search_txtbox.clear()
# search_txtbox.send_keys(Keys.ENTER)
