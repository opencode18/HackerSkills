from selenium import webdriver
from selenium.webdriver.common.keys import Keys


username = "notmyusername"
password = "notmypassword"

driver = webdriver.Chrome()
driver.get("http://www.facebook.com")

username_box = driver.find_element_by_id("email");
password_box = driver.find_element_by_id("pass");

username_box.send_keys(username)
password_box.send_keys(password)

login = driver.find_element_by_id('loginbutton')
login.click()
