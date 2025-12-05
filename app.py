# app.py
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from time import sleep

class Test_Estimation:

  
    def booting_function(self):
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        self.driver.get("https://retail.logimaxindia.com/test_etail_v3/admin/index.php/admin/login")
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        

    def test_Estimation(self, booting_function):
        self.driver.find_element(By.NAME, "username").send_keys("developer")
        self.driver.find_element(By.NAME, "password").send_keys("Dev#source@etail")
        sleep(3)
        self.driver.find_element(By.XPATH, '//button[@id="submit_login"]').click()

test = Test_Estimation()
test.booting_function()       
test.test_Estimation(test)  