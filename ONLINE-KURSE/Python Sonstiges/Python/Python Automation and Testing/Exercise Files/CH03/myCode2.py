from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# Selenium-Select-Klasse einfügen
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Firefox()
driver.get("http://127.0.0.1:5500/Exercise%20Files/html_code_03_02.html")

# wird Selenium-Konstr für Select aufgerufen. Als Param wird gefundene Selenium-Obj übergeben
select = Select(driver.find_element_by_name("numReturnSelect"))
select.select_by_index(4)  # Element des Selects-HTML über index auswählen
time.sleep(2)
# Element des Selects-HTML über text suchen
select.select_by_visible_text("200")
time.sleep(2)
# Element des Selects-HTML über den Wert auswählen
select.select_by_value("250")
time.sleep(2)

options = select.options  # Alle Optionen des Select-HTML-Elements printen
print(options)

submit_button = driver.find_element_by_name("continue")
submit_button.submit()
time.sleep(2)

input()

driver.close()
