from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
print("Login test case started")
options=webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches',['enable-logging'])
driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("http://127.0.0.1:8000/stafflogin")
# Login to the website
driver.find_element("name", "username").send_keys("Appu")
time.sleep(3)
driver.find_element("name", "password").send_keys("Appu@1234")
time.sleep(3)
driver.find_element("xpath", "/html/body/div/div/form/div/button").click()
time.sleep(3)
print("User Logged In")
driver.get("http://127.0.0.1:8000/apply_leave/")
time.sleep(3)
start_date_field = driver.find_element(By.NAME, "start_date")
start_date_field.send_keys("10-05-2023")
end_date_field = driver.find_element(By.NAME, "end_date")
end_date_field.send_keys("11-05-2023")
reason_field = driver.find_element(By.NAME, "reason")
reason_field.send_keys("Health issue")
driver.find_element("xpath", "/html/body/form/input[4]").click()
time.sleep(3)
driver.quit()
print("leave test passed")