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
driver.get("http://127.0.0.1:8000/login/")
driver.find_element("id", "username").send_keys("Ancy")
time.sleep(3)
driver.find_element("id", "password").send_keys("Ancy@1234")
time.sleep(3)
driver.find_element("xpath", "/html/body/div/div/form/div/button").click()
time.sleep(3)
print("User Logged In")
driver.get("http://127.0.0.1:8000/testdrive/")
time.sleep(3)
venue_field = driver.find_element(By.NAME, "venue")
venue_field.send_keys("Kottayam")
car_model_field = Select(driver.find_element(By.NAME, "carmodel"))
car_model_field.select_by_visible_text("All new XL6")
date_field = driver.find_element(By.NAME, "testdate")
date_field.send_keys("2023-04-03")
time_field = driver.find_element(By.NAME, "testtime")
time_field.send_keys("10:00")
email_field = driver.find_element(By.NAME, "Email")
email_field.send_keys("alli@gmail.com")
contact_field = driver.find_element(By.NAME, "Contact")
contact_field.send_keys("1234567890")
driver.find_element("xpath", "/html/body/div[2]/div/div/div/div/div/form/div[4]/button").click()
time.sleep(3)
driver.quit()
print("testdrive test passed")