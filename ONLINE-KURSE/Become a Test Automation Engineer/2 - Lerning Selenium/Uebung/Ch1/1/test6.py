from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time

browser = webdriver.Firefox()

browser.get("https://selenium-blog.herokuapp.com/signup")

timeStamp = time.time()
print(str(timeStamp))
print("user" + str(timeStamp))

usernameField = browser.find_element_by_id("user_username")
usernameField.send_keys("user" + str(timeStamp))

email_field = browser.find_element_by_id("user_email")
# timestamp der email hinzufügen
email_field.send_keys("email"+str(timeStamp)+"@test.com")
password_field = browser.find_element_by_id("user_password")
password_field.send_keys("password")

submit_button = browser.find_element_by_id("submit")
submit_button.send_keys(Keys.RETURN)

browser.quit()
