from selenium import webdriver
from selenium.webdriver.common.keys import Keys

email = raw_input("Enter your Email ID\n")
password = raw_input("Enter your Password\n")

driver = webdriver.Firefox()
driver.get('https://www.facebook.com/')
assert "Facebook" in driver.title

emailField = driver.find_element_by_id('email')
passwordField = driver.find_element_by_id('pass')
submitField = driver.find_element_by_id('u_0_2')

emailField.send_keys(email)
passwordField.send_keys(password)

submitField.submit()

# driver.quit()
