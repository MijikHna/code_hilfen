from selenium import webdriver

driver = webdriver.Firefox()
driver.get("http://127.0.0.1:5500/Ex_Files_Python_Automation_Testing/Exercise%20Files/CH02/html_code_02.html")

loginFormAbsolut = driver.find_element_by_xpath("/html/body/form[1]")
print("My input element ist: "+str(loginFormAbsolut))

loginFormRelative1 = driver.find_element_by_xpath("//form[1]")
print("My input element ist: "+str(loginFormRelative1))

loginFormRelative2 = driver.find_element_by_xpath("//form[@id='loginForm']")
print("My input element ist: "+str(loginFormRelative2))

driver.close()
