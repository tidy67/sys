import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://google.com")

print(driver.current_window_handle)
print(driver.window_handles)
time.sleep(5)

driver.save_screenshot("screenshot.png")
print("ss done")

driver.fullscreen_window()
time.sleep(5)
driver.maximize_window()
time.sleep(5)
driver.minimize_window()
time.sleep(5)
driver.set_window_size(1920, 1080)
time.sleep(5)
print(driver.get_window_size())
print(driver.get_window_position())
time.sleep(5)
driver.set_window_position(6, 6)
time.sleep(5)