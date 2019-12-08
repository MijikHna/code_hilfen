from selenium import webdriver
from selenium.webdriver import ActionChains
import time

driver = webdriver.Firefox()
driver.get("http://jqueryui.com/droppable")
driver.switch_to.frame(0)  # auf der Seite zum Frame[0] gehen

# Klasse um Actions zu automatisieren  (hover, drag, drop usw.)
action_chains = ActionChains(driver)
# Action wird zu Chain hinzugefügt, und wenn perform() die Chain wird ausgeführt

# 1.
source = driver.find_element_by_id("draggable")
target = driver.find_element_by_id("droppable")

# 2.
action_chains.drag_and_drop_by_offset(source, 100, 100).perform()
time.sleep(2)

# 1.
action_chains.drag_and_drop(source, target).perform()
time.sleep(2)

driver.close()
