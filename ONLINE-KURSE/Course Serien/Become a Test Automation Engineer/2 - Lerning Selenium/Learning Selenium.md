### 0 - Introduction
#### 2. What you shold know:
1. Ruby = Tests in Selenium schreiben. 

#### 2 - Install Ruby on Linux
1. Ruby kann man mit: 1)Package Manager, 2) Installer, 3) Manager 4) Source
2. für Linux RVM-Manager benutzen. = RVM-Manager installieren → mit RVM-Command-Console Ruby installieren (rvm → rvm install 2.5.1 (Binary-Ruby wird installieren) → ruby -v .
* Manager RVM - Ruby Version Manager installieren: Ruby-DevkitX.X.X herunterladen und installieren 
    
        gpg --keyserver hkp://pool.sks-keyservers.net --recv-keys 409B6B1796C275462A1703113804BB82D39DC0E3 7D2BAF1CF37B13E2069D6956105BD0E739499BDB
        \curl -sSL https://get.rvm.io | bash  ODER \curl -sSL https://get.rvm.io | bash -s stable
        rvm - es werden ein Oprtion des RVM angezeigt
        rvm install 2.6.3 - eventuell davor die letzte Version googeln oder mit rvm-Optionen herausfienden (rvm list known)
        ruby -v

3. Für Windows → RubyInstaller benutzen (Tipp: Ruby with DevKit installieren)

#### 5 - Selenium overview:
1. Selenium 1.0 Remote Control speiste JS in Browser um Aktionen auszuführen.
2. WebDriver = benutzt Browser-Client statt JS-Einspeisung (hatte eigen API)
3. => Selenium 2.0 mit WebDriver  
4. Selenium 3.0: RC weg + Browser stellen selber Driver zur Verfügung
5. Vortiele:
1. unterstützt alle Sprachen, Platformen, Browser
2. hat viele Testing-Tools
3. arbeitet zusammen mit anderen Tools
4. Free + Community

### 1 - Selenium WebDriver
#### 1 - Using WebDriver
* Ziele:
    * schnell und einfach automatische Tests zu schreiben
    * verwalten standartisiere API
    * USER-Action emulieren
* Ideal für:
    * Test in mehreren Browsern
    * Driver-API benutzen um zu cutomisieren
* Funktionsweise: Test Skript -> WebDriver-API (Browsersession initalisiern usw.) -> Browser
* Unterstützte Sprachen: C, Java, Ruby, Python, JS
* jeder Browser hat eigenen Driver (in Browser-Sprache geschrieben)

#### 2 - Setting up WebDriver
* Tools installieren bevor Test:
    1. Selenium WebBrowser - Framework
    2. geckodriver - BrowserDriver für Firefox
* Tools installieren:
    * www.seleniumhq.org/download/ -> Selenium Client &WebDriver Language Bindings herunterladen (hier Ruby) -> man wird zu https://rubygems.org/../.. weitergeleitet:
        * Gems = ~ Library oder Plugin
        * RubyGems = Package Management Framework und jedes Gem muss zuerst installiert werden
            * kann mit `gem install` oder `bundle` installiert werden
        * `gem install` ist in Ruby per default installiert
        * `bundle install` Gems werden im Gemfile definiert. Alle im Gemfile spezifizierten Gems können dann mit `bundler` installiert  werden. Gut für geteilte Projekt.
    * `gemfile` erstellen und dasd Kommando herauskopieren `gem 'selenium-webdriver', '~> 3.142', '>= 3.142.3'` und in Gemfile hereinkopieren
    * `gem install bundler` - bundler installieren
    * `bundle install` - den Gem aus Gemfile installieren
    * geckodriver herunterladen von www.github.com/mozilla/geckodriver -> releases -> Driver für OS herunterladen. (in Ordner mit dem Kurc heruntergeladen)
#### 3 - Using the API
* Ruby (aus dem Kurs):
    1. Ruby API Documentation benutzen
    2. `test3.rb`:
    ```ruby
    require "selenium-webdriver"  #Driver importieren
    #Driver benutzen
    driver = Selenium::WebDriver.for :firefox # Immer 1. Schritt: Instanz vom Driver erstellen, mann kann noch Resolutin usw. setzen -> in Docu nach Klasse Drive schauen
    driver.navigate.to "http://google.com" 

    element = driver.find_element(name: "q")
    element.click
    element.send_keys "Hello WebDriver!"
    element.submit

    driver.quit #Driver-Sitzung schließen
    ```
    3. unter https://seleniumhq.github.io die richtige API-Doku erforschen
* Python (selbst):
    

#### 4 - Write a test
* 3 Schritte:
    1. Entschieden, welcher Code automatisiert werden soll
    2. Szenarien ausschreiben und Schritte für Tests ausschreiben
        * welche Inputs/Outputs
        * (Return-)Werte der Szenarien
    3. Webelemente herausfidnen, die für Tests benötigt werden.
* Bsp: `test4.rb
```ruby
require "selenium-webdriver"

#TEST: Sign up for blog
driver = Selenium::WebDriver.for :firefox
driver.navigate.to "https://selenium-blog.herokuapp.com/signup"

#Actions
username_field = driver.find_element(id: "user_username")
username_field.send_keys("user")
email_field = driver.find_element(id: "user_email")
email_field.send_keys("email@test.com")
password_field = driver.find_element(id: "user_password")
password_field.send_keys("password")
submit_button = driver.find_element(id: "submit")
submit_button.click

#Assertions

drive.quite
```
* mit Webtools heraufinden, welche Elemente im Test angesprochen werden d.h Name, ID, Class usw.

#### 5 - Add structure to tests
* um Assertion zu Schreiben => RSpec-Librarys für Ruby benutzen
    1. RSpec Expectations - API um erwartete Werte zu vergelichen -> muss als Gem installiert werden (https://rubygems.org/gems/rspec den Gem-Eintrag kopieren und in `Gemfile` kopieren) 
    2. RSpec Core => stellt behavior-driven-development-form zur Verfügung + stellt formatierten Output
* Bsp 5: 
```ruby
require "selenium-webdriver"
require "rspec"

#TEST: Sign up for blog
descibe "Blog application" do #Rspec Core für die Formatierung
    describe "signup to the blog application" do 
        it "confirm tha a user can successfully signup" do # mit it Ziel des Test beschreiben
        
            driver = Selenium::WebDriver.for :firefox
            driver.navigate.to "https://selenium-blog.herokuapp.com/signup"

            #Actions
            username_field = driver.find_element(id: "user_username")
            username_field.send_keys("user")
            email_field = driver.find_element(id: "user_email")
            email_field.send_keys("email@test.com")
            password_field = driver.find_element(id: "user_password")
            password_field.send_keys("password")
            submit_button = driver.find_element(id: "submit")
            submit_button.click

            #Assertions
            banner = driver.find_element(id: "flash_success")
            banner_test = banner.text
            expect(banner_test).to eq("Welcome to the alpha blog user") 

            drive.quite
        end
    end 
end 
```
#### 6 - Running tests
* `rspec test5.rb` - Test im Terminal ausführen
* zuerst Mozilla-Driver einrichten (geckodriver) = in PATH aufnehmen:

```bash
export PATH=$PATH:"/media/kirill/Windows_D/Programmieren/ONLINE-KURSE/Become a Test Automation Engineer/2 - Lerning Selenium/Uebung/Ch1/1"
```
* Nach dem Test wird Fehler erscheinen, liegt daran, dass es schon so einen User gibt. => test korriegiren

```ruby
require "selenium-webdriver"
require "rspec"

#TEST: Sign up for blog
descibe "Blog application" do #Rspec Core für die Formatierung
    describe "signup to the blog application" do 
        it "confirm tha a user can successfully signup" do # mit it Ziel des Test beschreiben
            timestamp = Time.now.to_i #Zeit auslesen, damit der Name immer eindeutig ist
            driver = Selenium::WebDriver.for :firefox
            driver.navigate.to "https://selenium-blog.herokuapp.com/signup"

            #Actions
            username_field = driver.find_element(id: "user_username")
            username_field.send_keys("user#timestamp") #timestamp dem usernamen hinzufügen
            email_field = driver.find_element(id: "user_email")
            email_field.send_keys("email#timestamp@test.com") #timestamp der email hinzufügen
            password_field = driver.find_element(id: "user_password")
            password_field.send_keys("password")
            submit_button = driver.find_element(id: "submit")
            submit_button.click

            #Assertions
            banner = driver.find_element(id: "flash_success")
            banner_test = banner.text
            expect(banner_test).to eq("Welcome to the alpha blog user") 

            drive.quite
        end 
    end 
end 
```

#### 7 - All about the divers
* auf www.seleniumhq.org/downloads gibt es verschiede Driver für verschiedene Browser
### Python-Beispiel:
* `sudo pip3 install -U selenium`
* geckodriver muss nicht nicht in `PATH` sein, falls geckodriver in dem gleichen Ordner wie die .py-Datei
Bsp: test6.py (!!! ohne Wrapping und Assertions)
```python
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
```

#### Wichtige Seiten:
* https://www.seleniumhq.org/download/
* https://rubygems.org/gems/selenium-webdriver - Ruby Selenium-Driver
* https://seleniumhq.github.io/selenium/docs/api/rb/index.html - Ruby Selenium-Driver-Doku
* https://pypi.org/project/selenium/ - Python Selenium-Driver
* https://seleniumhq.github.io/selenium/docs/api/py/index.html - Python Selenium-Driver-Doku 
> 
* https://github.com/mozilla/geckodriver - Mozilla Gecko-Driver

### 2 - Selenium Grid
#### 1 - Grid benefits
* Selenium Grid - Remote Proxy Server um test per Remote zu laufen
* Läuft tests über mehrere Server
* = Test auf verschiedenen Browsern, Platformen und Geräten laufen
* aus zwei Komponenten:
    1. Hub - Zentraler Server für Grid
        + dort weden die Tests ausgeführt
        * Hub läuft auf einer Maschine und ist mit verschiedene Nodes verbunden
    2. Node = Server, die beim Hub registriert sind
        * erhalten Tests von Hub dort laufen die Tests
* Ablauf:
    1. Test wird auf Hub zum ausführen gesetzt
    2. Hub sucht passende Nodes für Tests
    3. Hub sendet Test-Skript zu richtigen Node
    * Tests werden auf dem ersten richtig passenden Node gefunden
    * Tests laufen also parallel
* Hub und Nodes müssen aufgesetzt werden
#### 2 - Setting up the hub
* man muss `Selenium Standalone Server` installieren. von www.seleniumhq.org/downloads herunterladen. Ist jar-Datei
* `java -jar selenium-server-standalone-x.x.x.jar -role hub` - S-A-Server wird als Hub ausgeführt
* Browser öffnen und `localhost:4444\console` - den Hub testen. Registrierte Nodes werden hier angezeigt
* im Hub kann man dann die Optionen für Node-Tests einstellen
* Parameter können in der Konsole oder in Config-Datei gesetzte werden
#### 3 - Configure nodes
* `java -jar selenium-server-standalone-3.7.1.jar -role node -hub http://localhost:4444/grid/register` - neuen Server als Node registrieren
* zum Configuration-Tab gehen = Einstellungen ansehen
* weitere Einstellungen kann man über Terminal beim Start oder über Konfigurationsdatei konfigurieren
#### 4 - Running tests
* man muss Remote-Driver benutzen
* Bsp 7:
```ruby
require "selenium-webdriver"
require "rspec"

#TEST: Sign up for blog
describe "Blog application" do #Rspec Core für die Formatierung
    describe "signup to the blog application" do 
        it "confirm tha a user can successfully signup" do
            # mit it Ziel des Test beschreiben
            timestamp = Time.now.to_i #Zeit auslesen, damit der Name immer eindeutig ist
            driver = Selenium::WebDriver.for : remote, desired_capabilities: :firefox # Instanz eines Remote-Webdrivers erstellen; desired_capabilit = mit welchen Eigenschaften Remote-Driver gestartet werden soll, kann sein Browser, Browserversion und Plattform
            driver.navigate.to "https://selenium-blog.herokuapp.com/signup"

            #Actions
            username_field = driver.find_element(id: "user_username")
            username_field.send_keys("user#{timestamp}") #timestamp dem usernamen hinzufügen
            email_field = driver.find_element(id: "user_email")
            email_field.send_keys("email#{timestamp}@test.com") #timestamp der email hinzufügen
            password_field = driver.find_element(id: "user_password")
            password_field.send_keys("password")
            submit_button = driver.find_element(id: "submit")
            submit_button.click

            #Assertions
            banner = driver.find_element(id: "flash_success")
            banner_text = banner.text
            expect(banner_text).to eq("Welcome to the alpha blog user#{timestamp}") 

            driver.quit    
        end 
    end
end 
```
* Test im Terminal laufen:
```bash
rspec test7.rb
```
* <- so ist es abgelaufen:
    1. Test wurde in Hub initialisiert.
    2. Test wurde an den Node gesendet und von da ausgeführt
* <- man kann im Terminal in dem Node/Hub liefen ansehen, was abgelaufen ist
* man muss überlegen, wo man Hub und Nodes erstellt
    1. auf realen Machinen
    2. in Virtuellen Maschinen (AWS usw.)
#### 5 - Pros and cons
* Pros:
    1. man kann gut scallieren, Tests parallelisieren
    2. Zentrales Management
* Pros:
    1. Hub und Node verwaltung = Zusätzliche Arbeit
        1. Debugs und Warning enablen
        2. Skripts zum managen erstellen
    2. Test laufen kann Performance herunterdrehen, einige Browserfenster werden eventuell nicht geschlossen
        1. Browserfenster explizit killen
        2. Nodes bzw. ganzen Server neustarten

### 3 - Writing Effective Tests
#### 1 - Clean test code with variables
* sich wiederholende Aufgaben zu Funktionen/Variablen machen
```ruby
timestamp = Time.now.to_i
username = "user #{timestamp}"
email = "user#{timestamp}@test.com"
password = "password"
```
#### 2 - Clean test code with functions
* sich wiederholende Aufgaben in Funtionen auslager = wird reusable
```ruby
require "selenium-webdriver"
require "rspec"

timestamp = Time.now.to_i
username = "user #{timestamp}"
email = "user#{timestamp}@test.com"
password = "password"

def enter_username(username)
    username_field = @driver.find_element(id: "user_name")
    username_field = @dirver.send_keys(username)
end

def enter_email(email)
    email_field = driver.find_element(id: "user_email")
    email_field.send_keys("email#{timestamp}@test.com") #timestamp der email hinzufügen
end

def enter_password(password)
    password_field = @driver.find_element(id: "user_password")
    password_field.send_keys("password")
end

def submit_form()
    submit_button = @driver.find_element(id: "submit")
    submit_button.click
end

def get_banner_text()
    banner = @driver.find_element(id: "flash_success")
    banner.text
end

#! da driver eine Variable innerhalb von it ist => kann von obigen Funktionen nicht erreicht werde. => driver eine Instanz-Variable machen = globale Var => ein @ vor jedem driver

#TEST: Sign up for blog
describe "Blog application" do #Rspec Core für die Formatierung
    describe "signup to the blog application" do 
        it "confirm tha a user can successfully signup" do
            # mit it Ziel des Test beschreiben
            timestamp = Time.now.to_i #Zeit auslesen, damit der Name immer eindeutig ist
            @driver = Selenium::WebDriver.for : remote, desired_capabilities: :firefox # Instanz eines Remote-Webdrivers erstellen; desired_capabilit = mit welchen Eigenschaften Remote-Driver gestartet werden soll, kann sein Browser, Browserversion und Plattform
            @driver.navigate.to "https://selenium-blog.herokuapp.com/signup"

            #Actions
            enter_username(username)
            enter_email(email)
            enter_password(password)
            submit_form()

            #Assertions
            banner_text = get_banner_text()
            expect(banner_text).to eq("Welcome to the alpha blog user#{timestamp}") 

            @driver.quit    
        end 
    end
end 
```
#### 3 - Page object pattern
* gutes Design Pattern für Selenium Tests ist **Page Object Pattern*:
    1. setzt Klassen für jede Seite der Application
    2. jede Klasse hat eigene Selektoren und Test-Method
* Ziel:
    * Test und Code trennen
    * bessere Verwaltbarkeit
* Verwendung am Beispiel:
    * es gibt zweiten auf denen Test gemacht werden 1) Sign-up-page und 2) User page
    * also jeder dieser Seiten bekommt eigene Klasse
*Bps: signup_page.rb
```ruby
class SignupPage

# css selectoren - Konstanten = CSS-Selektoren
USERNAME_FIELD = {id: "user_name"}
EMAIL_FIELD = {id: "user_email"}
PASSWORD_FIELD = {id: "user_password"}
SUBMIT_BUTTON = {id: "submit"}

attr_reader :driver # WebDriver-Instanz erlauben, im/für Test erstellt werden um in der Klasse benutzt zu werden

# class method

def initialize(driver) # ~ genehmigt driver für attr_reader
    @driver = driver
end

def enter_username(username)
    username_field = @driver.find_element(USERNAME_FIELD)
    username_field = @dirver.send_keys(username)
end

def enter_email(email)
    password_field = @driver.find_element(EMAIL_FIELD)
    password_field.send_keys("password")
end

def enter_password(password)
    password_field = @driver.find_element(PASSWORD_FIELD)
    password_field.send_keys("password")
end

def submit_form()
    submit_button = @driver.find_element(SUBMIT_BUTTON)
    submit_button.click
end

end # class End
```
* users_page.rb
```ruby
class UsersPage

# css selectoren
SUCESS_BANNER = {id: "flash_success"}

attr_reader :driver

# class methods
def initialize(driver) # <- ist Konstuktor in Ruby
    @driver = driver
end
def get_banner_text()
    banner = @driver.find_element(SUCESS_BANNER)
    banner.text # ist return 
end

end
```
* test8.rb
```ruby
require "selenium-webdriver"
require "rspec"
require_relative "signup_page.rb"
require_relative "user_page.rb"

timestamp = Time.now.to_i
username = "user #{timestamp}"
email = "user#{timestamp}@test.com"
password = "password"

#! da driver eine Variable innerhalb von it ist => kann von obigen Funktionen nicht erreicht werde. => driver eine Instanz-Variable machen = globale Var => ein @ vor jedem driver

#TEST: Sign up for blog
describe "Blog application" do #Rspec Core für die Formatierung
    describe "signup to the blog application" do 
        it "confirm tha a user can successfully signup" do
            # mit it Ziel des Test beschreiben
            timestamp = Time.now.to_i #Zeit auslesen, damit der Name immer eindeutig ist
            @driver = Selenium::WebDriver.for :firefox # Instanz eines Remote-Webdrivers erstellen; desired_capabilit = mit welchen Eigenschaften Remote-Driver gestartet werden soll, kann sein Browser, Browserversion und Plattform
            @driver.navigate.to "https://selenium-blog.herokuapp.com/signup"

            # Signup benutzen:
            signup = SignupPage.new(@driver)
            #Actions
            signup.enter_username(username)
            signup.enter_email(email)
            signup.enter_password(password)
            signup.submit_form()

            users=UsersPage(@driver)
            banner_text= users.get_banner_text()
            expect(banner_text).to eq("Welcome to the alpha blog user#{timestamp}") 

            @driver.quit    
        end 
    end
end 
```

#### 4 - Test suite organization
1. Klasse ist nur für ihre Sachen zuständig
2. Test in Gruppen (Subsuits) unterteilen
3. Tests mit README dokumentieren 
#### 5 - The test pyramid
* UI-Tests = Selenium-Tests
### - Additional
* github.com/SeleniumHQ = Selenium Wiki