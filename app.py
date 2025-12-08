# app.py
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from time import sleep

class Test_Estimation:

  
    def booting_function(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("https://retail.logimaxindia.com/test_etail_v3/admin/index.php/admin/login")
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        

    def test_Estimation(self, booting_function):
        self.driver.find_element(By.NAME, "username").send_keys("developer")
        self.driver.find_element(By.NAME, "password").send_keys("Dev#source@etail")
        sleep(3)
        self.driver.find_element(By.XPATH, '//button[@id="submit_login"]').click()
        print("Login was Successfully")

test = Test_Estimation()
test.booting_function()       

test.test_Estimation(test)  

