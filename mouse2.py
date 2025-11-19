from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
driver.set_page_load_timeout(60)
driver.maximize_window()

driver.get("https://imcc.mespune.in/")
wait = WebDriverWait(driver, 15)
actions = ActionChains(driver)

header = wait.until(
    EC.presence_of_element_located((
        By.XPATH,"//h2[contains(normalize-space(.),'Prominent Recruiters')]"
    )
))
# logos = wait.until(
#     EC.presence_of_all_elements_located((By.XPATH,"//h2[contains(normalize-space(.),'Prominent Recruiters')]/following::img"))
# )

logos = driver.find_elements(By.XPATH,"//h2[contains(normalize-space(.),'Prominent Recruiters')]/following::img")
# ))
print("Total Logos found:", len(logos))

if len(logos) >= 3:
    third_logo = wait.until(EC.visibility_of(logos[2]))
    time.sleep(2)
    actions.click_and_hold(third_logo).move_by_offset(-100,0).release().perform()

    print("Dragged 3rd logo 100px to the left.")
    time.sleep(2)
else:
    print("less than 3 logos found")

driver.quit()
