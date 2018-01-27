import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver= webdriver.Firefox()
driver.get("http://mail.google.com")
emailid=driver.find_element_by_id("Email")
emailid.send_keys("username")
key=driver.find_element_by_id("Passwd")
key.send_keys("password")
signin=driver.find_element_by_id("signIn")
signin.click()
driver.close()