from selenium import webdriver

username = input("Enter Github username:-\n")
password = input("Enter password:-\n")

browser = webdriver.Firefox()
browser.get('https://github.com/login')
usernameField = browser.find_element_by_id("login_field")
passwordField = browser.find_element_by_id("password")
signInField = browser.find_element_by_name("commit")

usernameField.send_keys(username)
passwordField.send_keys(password)
signInField.submit()