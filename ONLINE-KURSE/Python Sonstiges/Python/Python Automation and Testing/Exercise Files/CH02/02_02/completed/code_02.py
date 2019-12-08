from selenium import webdriver
driver = webdriver.Firefox()
driver.get("http://127.0.0.1:5500/Ex_Files_Python_Automation_Testing/Exercise%20Files/CH02/html_code_02.html")
login_form = driver.find_element_by_id('loginForm')
print("My login form element is:")
print(login_form)
driver.close()
