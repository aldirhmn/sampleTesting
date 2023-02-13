import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

class Test_login(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    
    def test_a_success_login(self):
        browser = self.browser
        browser.maximize_window()

        browser.get("https://kasirdemo.belajarqa.com/")
        time.sleep(1)
        browser.find_element(By.ID,"email").send_keys("akunml24@gmail.com")
        time.sleep(1)
        browser.find_element(By.ID,"password").send_keys("Akunml24")
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div[1]/div/div/div/div[2]/div/button").click()
        time.sleep(2)

        response_message = browser.find_element(By.XPATH,"/html/body/div[1]/div/div/div/div[2]/div/div[1]/div[1]/div").text
        self.assertIn('hai', response_message)

    def test_b_failed_login_empty_email(self):
        browser = self.browser
        browser.maximize_window()

        browser.get("https://kasirdemo.belajarqa.com/")
        time.sleep(1)
        browser.find_element(By.ID,"email").send_keys("")
        time.sleep(1)
        browser.find_element(By.ID,"password").send_keys("Akunml24")
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div[1]/div/div/div/div[2]/div/button").click()
        time.sleep(2)

        response_message = browser.find_element(By.XPATH,"/html/body/div[1]/div/div/div/div[2]/div/div[1]").text
        self.assertEqual(response_message, '"email" is not allowed to be empty')
    
    def test_c_failed_login_with_email_invalid(self):
        browser = self.browser
        browser.maximize_window()

        browser.get("https://kasirdemo.belajarqa.com/")
        time.sleep(1)
        browser.find_element(By.ID,"email").send_keys("akunml24")
        time.sleep(1)
        browser.find_element(By.ID,"password").send_keys("Akunml24")
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div[1]/div/div/div/div[2]/div/button").click()
        time.sleep(2)

        response_message = browser.find_element(By.XPATH,"/html/body/div[1]/div/div/div/div[2]/div/div[1]").text
        self.assertEqual(response_message,'"email" must be a valid email')
    
    def test_d_failed_login_with_empty_password(self):
        browser = self.browser
        browser.maximize_window()

        browser.get("https://kasirdemo.belajarqa.com/")
        time.sleep(1)
        browser.find_element(By.ID,"email").send_keys("akunml24@gmail.com")
        time.sleep(1)
        browser.find_element(By.ID,"password").send_keys()
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div[1]/div/div/div/div[2]/div/button").click()
        time.sleep(2)

        response_message = browser.find_element(By.XPATH,"/html/body/div[1]/div/div/div/div[2]/div/div[1]").text
        self.assertEqual(response_message,'"password" is not allowed to be empty')

    
    def tearDown(self):
        self.browser.close()

if __name__=="__main__":
    unittest.main()