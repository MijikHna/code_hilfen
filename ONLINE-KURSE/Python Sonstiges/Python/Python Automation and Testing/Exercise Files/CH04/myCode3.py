from selenium import webdriver

driver = webdriver.Firefox()

# sagen wie viel gewartet wird, bis Skript weiter ausgeführt wird. Wenn danach das Element nicht geladen wird, wird Exception geworfen
driver.implicitly_wait(10)

# es wird 10 sek. gewartet, bis die Seite geladen
driver.get("http://www.python.org")
# es wird 10 sek. gewartet bis das Element gefunden wird
myDynamicElement = driver.find_element_by_id("start_shell")

driver.close()
