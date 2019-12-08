### 1 - What is Autoamtion Testing and Python-Selenium Framework
#### 1 - What is automated tesing?
* Test Pyramide:
    1. Unit tests - viele + fast alle Codeteile
    2. Service/API Layer tests - Code der Input nimmt und produziert Output
    3. User interface tests - 
* Python hat Bibliothen zum testen:
    1. Unit tests -> unittest, pytest, nose
    2. UI tests -> selenium + python
#### 2 - Python-Selenium bindings
* Selenium automatisiert Browsers, für UI Automation
* Installation:
    1. https://selenium-python.readthedocs.io/
    2. `sudo pip3 install selenium`
    3. für Firefox geckodriver installieren <- in PATH aufnehmen
* Bsp 1:
```python
from selenium import webdriver;
browser= webdriver.Firefox();
browser.get('http://www.seleniumhq.org');
```


#### 3 - A simple code example
Bsp 2:
``` python
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox()
driver.get("http://www.python.org")

elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
time.sleep(8)

driver.close()
```
#### 4 - Cross-browser support
* BrowserDriver z.B FirefoxBroser(geckodriver):
    * BrowserDriver binary muss extra heruntergeladen werden (geckodriver)
    * BrowserDriver muss in PATH sein
    * `driver = webdriver.Firefox()` oder `driver = webdriver.Chrome()` oder `driver = webdriver.Edge()`- Instanz von FirefoxDriver erstellen
### 2 - Parsing the HTML DOM Structure
**Es wurde der Live Server von VS Code benutzt**
#### 1 - What is the HTML DOM structure
* Baumdiagram von HTML-Elementen
#### 2 - Locating elements by ID
* **!!!** id ist Casesensitive
```python
from selenium import webdriver

driver = webdrive.Firefox()
driver.get("http://127.0.0.1:5500/Exercise%20Files/html_code_02.html")

login_form = driver.find_element_by_id("loginForm")
print("My login form element ist: "+str(login_form))

driver.close()
```
#### 3 - Locating elements by name
* = HTML-Element bei ihrem Attribute name=".." lokalisieren. Oft bei <input>-Tags in Formularen
* falls mehrere Elemente den gleichen Wert bei name haben, wird nur das erste returnt. 
```python
from selenium import webdriver

driver = webdrive.Firefox()
driver.get("http://127.0.0.1:5500/Exercise%20Files/html_code_02.html")

username = driver.find_element_by_name("username")
print("My input element ist: "+str(username))

driver.close()
```
#### 4 - Locating elements by XPath
* XPath = XML Path Language 
* mit XPath kann man sich durch Nodes (HTML-Elemente) navigieren (= sich durch DOM navigieren). Damit kann man eins oder mehrere Elemente auswählen
* werden benutzt, wenn class und id nicht möglich sind
* Pfad kann als absoluter oder als relativer Pfad zum DOM-Element definiiert
    * absolut = vom Root-Node
    * relative = vom ausgewählten Node
    * relative Pfade sind zu bevorzugen
```python
from selenium import webdriver

driver = webdriver.Firefox()
driver.get("http://127.0.0.1:5500/Exercise%20Files/html_code_02.html")

loginFormAbsolut = driver.find_element_by_xpath("/html/body/form[1]")
print("My input element ist: "+str(loginFormAbsolut))

loginFormRelative1 = driver.find_element_by_xpath("//form[1]")
print("My input element ist: "+str(loginFormRelative1))

loginFormRelative2 = driver.find_element_by_xpath("//form[@id='loginForm']")
print("My input element ist: "+str(loginFormRelative2))

driver.close()

```
* XPath nur im Notfall benutzen, wenn id und class nicht geht.
    * Wenn man XPath benutzt, dann relative Pfade bevorzugen.
#### 5 - Locating elements by class
* **!!!** es wird nur das [0]-te Element returnt.
```python
from selenium import webdriver

driver = webdriver.Firefox()
driver.get("http://127.0.0.1:5500/Exercise%20Files/html_code_02.html")

content = driver.find_element_by_class_name("content")
print("My class element ist: "+str(content))

driver.close()
```
* benutzen, wenn man Gruppe von Elementen holen möchten
* **!!!** es gibt noch weitere Locater z.B über CSS-Eigenschaft, Tag-Namen

#### Additional:
* zu XPath:
    1. `heading_xpath = driver.find_element_by_xpath("//*@id="mainContent"]/h2[1])` - `*` = können mehrere HTML-Elemente dazwischen liegen. Also naviegere bis id="mainContent", dann nimm erste <h2>

### 3 - Navigating through Pages

#### 1 - Page interaction
* Bsp 1:
```python
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox()
driver.get("http://python.org")

search = driver.find_element_by_name("q")
search.clear()  # Input-Feld leeren
search.send_keys("pycon")
search.send_keys(Keys.RETURN)

time.sleep(4)

driver.close()
``` 
#### 2 - Filling forms
* mit Formelementen hantieren
* Selenium hat viele Klassen um mit Elementen zu handieren
    * z.B Klasse Select um mit Select-Elementen der Form zu handieren
    * es gibt **Submit**-Method, dass für alle Selenium-Elemente der Form implementiert ist.
* Bsp 2 __html_code_03_02.html__:
```python
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select # Selenium-Select-Klasse einfügen
import time

driver = webdriver.Firefox()
driver.get("http://127.0.0.1:5500/Exercise%20Files/html_code_03_02.html")

select = Select(driver.find_element_by_name("numReturnSelect")) # wird Selenium-Konstr für Select aufgerufen. Als Param wird gefundene Selenium-Obj übergeben
select.select_by_index(4) # Element des Selects-HTML über index suchen
time.sleep(2)
select.select_by_visible_text("200") #Element des Selects-HTML über text suchen
time.sleep(2)
select.select_by_value("250") #Element des Selects-HTML über den Wert suchen
time.sleep(2)

options = select.options # Alle Optionen des Select-HTML-Elements printen
print(options)

submit_button = driver.find_element_by_name("continue")
submit_button.submit();
time.sleep(2)

driver.close()
```
#### 3 - Drag and drop elements
* Drag und Drop Funktionen der Seite testen
* in Selenium kann man drag/drop über:
    1. Elementnamen
    2. X-/Y-Offset machen
```python
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

```
### 4 - Waits
#### 1 - What are waits and why do we need them
* da viele Seite asynchrones Laden z.B Ajax benutzen
* wenn Element nicht gefunden wird => wird Exception geworfen und Test abgebrochen
* Waits = Zeit zwischen Aktions des Webdriver setzen
* zwei Typen:
    * explicit = stoppt Ausfühung des Tests, bis bestimmte Konditionen erreicht werden
    * implicit = fragt DOM für ausgewählte Zeit, ob ein Element jetzt erreicht werden kann
#### 2 - Explicit waits
* es gibt in Selenium verschiedene Kombinationen um explicite Waits zu erstellen:
    * Kombination aus WebDriver und ExpectedConditions
``` python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.get("http://www.python.org")

try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(By.ID, "start-shell"))  # Wenn Element mit id="start-shell" innerhalb von 10 Sekunden geladen wird/gefunden wird, wird der Test fotgesetzt, sonst wird Exception geworfen

finally:
    driver.quit()
```
#### 3 - Implicit waits
* pausieren für bestimmte Zeit vor jeder Aktion z.B. wenn schlechte Internet-Verbindung. Wenn der Element inzwischen nicht geladen wird, wird Exception geworfen. 
* Unterschied zu expliciten ist, das vor jedem Action gewartet wird.
* Wartezeit wird in sec. angegeben