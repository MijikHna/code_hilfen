require "selenium-webdriver"
require "rspec"

#TEST: Sign up for blog
describe "Blog application" do #Rspec Core für die Formatierung
    describe "signup to the blog application" do 
        it "confirm tha a user can successfully signup" do
            # mit it Ziel des Test beschreiben
            timestamp = Time.now.to_i #Zeit auslesen, damit der Name immer eindeutig ist
            driver = Selenium::WebDriver.for :firefox
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