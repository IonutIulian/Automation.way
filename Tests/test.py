import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://formy-project.herokuapp.com/form")
driver.find_element(By.XPATH,"//input[@placeholder='Enter first name']").send_keys("Anton")
driver.find_element(By.XPATH,"//input[@placeholder='Enter last name']").send_keys("Pann")
driver.find_element(By.XPATH,"//div[@class='form-group']/div/input").send_keys("first name prin navigare")
driver.find_element(By.XPATH,"//form//input[@placeholder='Enter last name']").send_keys("last name prin navigare")
driver.find_elements(By.XPATH,"//input[@class='form-control']")[2].send_keys("test job")
#driver.find_element(By.XPATH,"//input[@id='first-names'] | //input[@id='last-nam']").send_keys("element cu | ")
time.sleep(4)