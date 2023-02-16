from selenium.webdriver.common.by import By
import time
import os

from Locators.objectLocators import objectLocator

class loginPage():

    def __init__(self, driver):
        self.driver = driver
        self.projectDir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    def input_email(self, email):
        self.driver.save_screenshot(self.projectDir+'/Screenshot/1.png')
        self.driver.find_element(By.ID, objectLocator.field_email_id).send_keys(email)
        time.sleep(1)
    def input_password(self, password):
        self.driver.find_element(By.ID, objectLocator.field_password_id).send_keys(password)
        time.sleep(1)
    def click_login(self):
        self.driver.find_element(By.XPATH, objectLocator.button_login_xpath).click()
        time.sleep(3)
        self.driver.save_screenshot(self.projectDir+'/Screenshot/2.png')
    def validation_after(self):    
        response_message = self.driver.find_element(By.XPATH, objectLocator.validation_xpath).text
        assert response_message == 'hai'
    def clear_text(self):
        self.driver.find_element(By.ID, objectLocator.field_email_id).clear()
        self.driver.find_element(By.ID, objectLocator.field_password_id).clear()