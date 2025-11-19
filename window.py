import time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://www.facebook.com")
wait = WebDriverWait(driver, 10)
time.sleep(2)

original_window = driver.current_window_handle
print(original_window,type(original_window))

driver.switch_to.new_window('window')
wait.until(EC.number_of_windows_to_be(2))

driver.execute_script("window.open('http://www.google.com/');")
time.sleep(2)
wait.until(EC.number_of_windows_to_be(3))
all_windows = driver.window_handles
print(all_windows,type(all_windows))
for window in all_windows:
    if window != original_window:
        driver.switch_to.window(window)
        break
driver.quit()

# try with 2 different drivers