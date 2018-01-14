#python 2.7
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

username = raw_input("Enter your e-mail or phone\n")
password = raw_input("Enter your Facebook password\n")
driver = webdriver.Firefox()
driver.get('https://www.facebook.com/')
assert "Facebook" in driver.title
emailField = driver.find_element_by_id('email')
passwordField = driver.find_element_by_id('pass')
login = driver.find_element_by_id('u_0_2')

emailField.send_keys(username)
passwordField.send_keys(password)
login.submit()
print "Success!"