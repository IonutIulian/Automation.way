import time
from selenium.webdriver.support.select import Select
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.maximize_window()

# Choose 3 items of each selector type from the following categories:
#  Id
#  Link text
#  Partial link text
#  Name
#  Tag*
#  Class name*
#  Css (1 after id, 1 after class, 1 after attribute=partial_value)


# Find element by ID.

driver.get("https://the-internet.herokuapp.com/login")
time.sleep(2)
driver.find_element(By.ID, "username").send_keys("tomsmith")
driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
time.sleep(3)
driver.find_element(By.CLASS_NAME,"radius").click()


# Find element by LINK TEXT

driver.get("https://the-internet.herokuapp.com/")
time.sleep(1)
driver.find_element(By.LINK_TEXT, "Drag and Drop").click()
time.sleep(1)
driver.get("https://the-internet.herokuapp.com/")
driver.find_element(By.LINK_TEXT, "File Upload").click()
time.sleep(1)
driver.get("https://the-internet.herokuapp.com/")
driver.find_element(By.LINK_TEXT, "Floating Menu").click()
time.sleep(1)


# Find element by Partial Link Text

driver.get("https://the-internet.herokuapp.com/")
time.sleep(1)
driver.find_element(By.PARTIAL_LINK_TEXT, "Shifting ").click()
time.sleep(1)
driver.find_element(By.PARTIAL_LINK_TEXT,"Menu Element").click()
time.sleep(1)
driver.find_element(By.PARTIAL_LINK_TEXT,"Contact")
time.sleep(1)


# Find element by Name

driver.get("https://www.techlistic.com/p/selenium-practice-form.html")
time.sleep(1)
driver.find_element(By.NAME, "firstname").send_keys("Petrica")
time.sleep(1)
driver.find_element(By.NAME,"lastname").send_keys("Ungureanu")
time.sleep(1)
list = driver.find_elements(By.NAME,"continents")
for i in range(len(list)):
		print(list[i].text)
dropdown_menu = Select(driver.find_element(By.NAME,"continents"))
dropdown_menu.select_by_visible_text("Australia")
time.sleep(2)


# Find element By Tag

driver.get("https://the-internet.herokuapp.com/")
time.sleep(1)
driver.find_element(By.LINK_TEXT,"Dropdown").click()
time.sleep(1)
lista_tari = driver.find_elements(By.TAG_NAME,"select")
for i in range(len(lista_tari)):
		print(lista_tari[i].text)
dropdown_menu = Select(driver.find_element(By.TAG_NAME,"select"))
dropdown_menu.select_by_index(1)
time.sleep(2)
driver.get("https://the-internet.herokuapp.com/")
driver.find_element(By.PARTIAL_LINK_TEXT,"Controls").click()
time.sleep(2)
lista = driver.find_elements(By.TAG_NAME,"button")
for i in range(len(lista)):
		print(lista[i].text)
driver.find_elements(By.TAG_NAME,"button")[0].click()
time.sleep(5)


# Find element by Class

driver.get("https://phptravels.net/")

time.sleep(1)
driver.find_element(By.CLASS_NAME,"pe-1").click()
time.sleep(2)
driver.find_elements(By.CLASS_NAME,"dropdown-item")[5].click()
time.sleep(2)
driver.find_elements(By.CLASS_NAME,"form-control")[0].send_keys("mihai.tudorel@gmail.com")
driver.find_elements(By.CLASS_NAME,"form-control")[1].send_keys("tudorelcelmare")
driver.find_elements(By.CLASS_NAME,"btn-dark")[0].click()
time.sleep(3)

#Find element by CSS
# 1 after id, 1 after class, 1 after attribute=value

driver.get("https://phptravels.net/")
time.sleep(1)
driver.find_elements(By.CSS_SELECTOR,".waves-effect")[2].click() #class
time.sleep(1)
# id
driver.find_element(By.CSS_SELECTOR,"#round-trip").click()
time.sleep(2)
# atribute = value
driver.find_element(By.CSS_SELECTOR,"[name='depart']").clear()
driver.find_element(By.CSS_SELECTOR,"[name='depart']").send_keys("28-01-2023")
time.sleep(2)
driver.find_element(By.CSS_SELECTOR,"[name='returning']").clear()
driver.find_element(By.CSS_SELECTOR,"[name='returning']").send_keys("27-02-2023")
time.sleep(2)

# For xpath identify elements by the criteria below:
#  3 by value attribute
#  3 by element text
# 1 by partial text
# 1 by SAU, using pipe |
#  1 with *
#  1 where you take them as a list of xpath and in python 1 element arrives, so
# with (xpath)[1]
#  1 where you use parent::
# 1 in which to use the sibling before or after (your choice)
#  1 function like the one in the class by which I can choose by parameter with
# which element I want to interact with.

#Value Attribute

driver.get("https://the-internet.herokuapp.com/")
driver.find_element(By.LINK_TEXT,"Form Authentication").click()
driver.find_element(By.XPATH,"//input[@id='username']").send_keys("tomsmith")
driver.find_element(By.XPATH,"//input[@name='password']").send_keys("SuperSecretPassword!")
driver.find_element(By.XPATH,"//button[@type='submit']").click()
time.sleep(2)


# By element text and list of xpath

driver.get("https://formy-project.herokuapp.com/")
driver.find_elements(By.CLASS_NAME,"btn-lg")[0].click()
time.sleep(3)
driver.find_element(By.XPATH,"//input[@placeholder='Enter address']").send_keys("mail.text@gmail.com")
time.sleep(2)
driver.find_element(By.XPATH,"//button[@class='dismissButton']").click()
time.sleep(1)
driver.find_elements(By.XPATH,"//input[@type='text']")[2].send_keys("Crinilor no:112")
time.sleep(2)
driver.find_element(By.XPATH,"//input[@placeholder='City']").send_keys("Pascani")
time.sleep(2)

# by partial text

driver.get("https://the-internet.herokuapp.com/")
time.sleep(2)
driver.find_element(By.XPATH, "//a[contains(text(),'Controls')]").click()
time.sleep(2)

# using pipe |

driver.get("https://formy-project.herokuapp.com/autocomplete")
s = driver.find_element(By.XPATH, '//input[@id="street_number"] | //input[@id="route"]')
time.sleep(2)
s.clear()
s.send_keys("Hall Place")

# using * - means a substitute for all elements that comply with the rule
driver.get("https://the-internet.herokuapp.com/login")
driver.implicitly_wait(2)
driver.find_element(By.XPATH,"//*[@id='username']").send_keys("John")


## 1 in which to use the sibling before or after

driver.get("https://the-internet.herokuapp.com/notification_message_rendered")
driver.find_element(By.XPATH,"//div[@class= 'example']/p/br[4]/following-sibling::a").click()
time.sleep(2)

##  1 where you use parent::

driver.get("https://phptravels.net/")
driver.implicitly_wait(2)
driver.find_element(By.XPATH, "//strong[@class='m-0 text-dark']/parent::a").click()
time.sleep(2)

#  1 function like the one in the class by which I can choose by parameter with
# which element I want to interact with.

def input_by_id (id , input_value):
    driver.get("https://formy-project.herokuapp.com/autocomplete")
    input = driver.find_element(By.XPATH, f'//input[@id="{id}"]')
    input.clear()
    input.send_keys(input_value)

input_by_id("street_number", "capsunilor nr. 12")
input_by_id("route", "lavandei nr. 34")