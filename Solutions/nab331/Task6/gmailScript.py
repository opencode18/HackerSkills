from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

#Page going to google accounts by default

username = "notmyusername"
password = "notmypassword"

driver = webdriver.Chrome()
driver.get("http://www.gmail.com")

username_box = driver.find_element_by_id("identifierId")
username_box.send_keys(username)

Next = driver.find_elements_by_id("identifierNext")
Next[0].click()

sleep(1)

password_box = driver.find_element_by_name("password")
password_box.send_keys(password)

Next = driver.find_element_by_id("passwordNext")
Next.click()
