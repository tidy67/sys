from selenium import webdriver
from selenium.webdriver.common.by import By
# import time
driver = webdriver.Chrome()
# webdriver.Chrome().get('https://www.google.com')
driver.get("https://www.google.com")
# current_url = driver.current_url
# print(current_url)
# title = driver.title
# print(title)
# print(driver.page_source)
# driver.fullscreen_window()
#
# driver.refresh()
# driver.maximize_window()
#
# driver.refresh()
# driver.minimize_window()
# driver.refresh()
# driver.forward()
# driver.back()
# driver.refresh()
# driver.execute_script("window.open('https://www.gemini.com');")
# time.sleep(2)
# driver.current_window_handle
# handle = driver.window_handles
# print(handle)
# driver.switch_to.window(handle[1])
# driver.switch_to.new_window('tab')
# driver.refresh()
# driver.switch_to.window(handle[0])
# driver.switch_to.new_window('window')

# alert = driver.switch_to.alert
# print(alert.text)
# alert.accept()
# alert.dismiss()

element = driver.find_element(
    By.ID,'APjFqb'
)
print(element)

element1 = driver.find_element(
    By.NAME, 'q'
)
print(element1)

element2 = driver.find_element(
    By.XPATH, "//textarea[@id='APjFqb']"
)
print(element2)

element3 = driver.find_element(
    By.XPATH, "//div[@class='o3j99 LLD4me yr19Zb LS8OJ']"
)
print(element3)

mult_ele = driver.find_elements(
    By.XPATH,
)

#
# driver.close()
# driver.quit()