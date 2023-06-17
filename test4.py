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
driver.get("http://127.0.0.1:8000/admin/login/?next=/admin/")
# Login to the website
driver.find_element("name", "username").send_keys("admin")
time.sleep(3)
driver.find_element("name", "password").send_keys("admin")
time.sleep(3)
driver.find_element("xpath", "/html/body/div/div[2]/div/div[1]/div/form/div[3]").click()
time.sleep(3)
print("admin Logged In")
driver.get("http://127.0.0.1:8000/admin/carapp/bank/add/")
time.sleep(3)
bankname_field = driver.find_element(By.NAME, "name")
bankname_field.send_keys("HDFC")
interest_rate_field = driver.find_element(By.NAME, "interest_rate")
interest_rate_field.send_keys("7.3")
driver.find_element("xpath", "/html/body/div/div[3]/div/div[1]/div/form/div/div/input[1]").click()
time.sleep(3)
driver.quit()
print("emi test passed")
print("test passed")