import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
import random
import string

class Test_regis(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    
    def test_a_success_regis(self):
        namatoko_random = ''.join(random.choice(string.ascii_letters) for _ in range(16)) #random toko name
        email_random = ''.join(random.choice(string.ascii_letters) for _ in range(16)) + '@gmail.com' #random gmail
        password_register = ''.join(random.choice(string.ascii_letters) for _ in range(15)) #random password
        
        browser = self.browser
        browser.maximize_window()

        browser.get("https://kasirdemo.belajarqa.com/") #url
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div[1]/div/div/div/div[2]/div/div[3]/a").click() #click daftar
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div[1]/div/div/div/div[2]/div/div[1]/input").send_keys(namatoko_random) #input random nama toko
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div[1]/div/div/div/div[2]/div/div[2]/input").send_keys(email_random) #input random email
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div[1]/div/div/div/div[2]/div/div[3]/div/input").send_keys(password_register) #input random password
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div[1]/div/div/div/div[2]/div/button").click() #click daftar
        time.sleep(3)

        response_message = browser.find_element(By.XPATH,"/html/body/div[2]/ul[3]/li/div/div/div/div[1]").text #validasi
        time.sleep(1)
        response_message2 = browser.find_element(By.XPATH,"/html/body/div[2]/ul[3]/li/div/div/div/div[2]").text #validasi

        self.assertEqual(response_message,"Toko berhasil didaftarkan") #validasi
        time.sleep(2)
        self.assertEqual(response_message2,"anda dapat menggunakan login sekarang") #validasi
        time.sleep(2)

    def test_b_failed_regis_with_empty_nama_toko(self):
        email_random = ''.join(random.choice(string.ascii_letters) for _ in range(16)) + '@gmail.com'
        password_register = ''.join(random.choice(string.ascii_letters) for _ in range(15))
        browser = self.browser
        browser.maximize_window()

        browser.get("https://kasirdemo.belajarqa.com/")
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div[1]/div/div/div/div[2]/div/div[3]/a").click()
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div[1]/div/div/div/div[2]/div/div[1]/input").send_keys("")
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div[1]/div/div/div/div[2]/div/div[2]/input").send_keys(email_random)
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div[1]/div/div/div/div[2]/div/div[3]/div/input").send_keys(password_register)
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div[1]/div/div/div/div[2]/div/button").click()
        time.sleep(1)
        response_message = browser.find_element(By.XPATH,"/html/body/div[1]/div/div/div/div[2]/div/div[1]").text
        time.sleep(1)
        self.assertEqual(response_message, '"name" is not allowed to be empty')
        time.sleep(1)
    
    def test_c_failed_regis_with_email_empty(self):
        namatoko_random = ''.join(random.choice(string.ascii_letters) for _ in range(16))
        password_register = ''.join(random.choice(string.ascii_letters) for _ in range(15))
        
        browser = self.browser
        browser.maximize_window()

        browser.get("https://kasirdemo.belajarqa.com/")
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div[1]/div/div/div/div[2]/div/div[3]/a").click()
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div[1]/div/div/div/div[2]/div/div[1]/input").send_keys(namatoko_random)
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div[1]/div/div/div/div[2]/div/div[2]/input").send_keys()
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div[1]/div/div/div/div[2]/div/div[3]/div/input").send_keys(password_register)
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div[1]/div/div/div/div[2]/div/button").click()
        time.sleep(3)
        response_message = browser.find_element(By.XPATH,"/html/body/div[1]/div/div/div/div[2]/div/div[1]").text
        time.sleep(1)

        self.assertEqual(response_message,'"email" is not allowed to be empty')
        time.sleep(2)
    
    def test_d_failed_regis_with_email_empty(self):
        namatoko_random = ''.join(random.choice(string.ascii_letters) for _ in range(16))
        email_random = ''.join(random.choice(string.ascii_letters) for _ in range(16)) + '@gmail.com'
        
        browser = self.browser
        browser.maximize_window()

        browser.get("https://kasirdemo.belajarqa.com/")
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div[1]/div/div/div/div[2]/div/div[3]/a").click()
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div[1]/div/div/div/div[2]/div/div[1]/input").send_keys(namatoko_random)
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div[1]/div/div/div/div[2]/div/div[2]/input").send_keys(email_random)
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div[1]/div/div/div/div[2]/div/div[3]/div/input").send_keys()
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div[1]/div/div/div/div[2]/div/button").click()
        time.sleep(3)
        response_message = browser.find_element(By.XPATH,"/html/body/div[1]/div/div/div/div[2]/div/div[1]").text
        time.sleep(1)

        self.assertEqual(response_message,'"password" is not allowed to be empty')
        time.sleep(2)
    
    def test_e_failed_regis_with_email_invalid(self):
        namatoko_random = ''.join(random.choice(string.ascii_letters) for _ in range(16))
        email_random = ''.join(random.choice(string.ascii_letters) for _ in range(16))
        password_register = ''.join(random.choice(string.ascii_letters) for _ in range(15))
        
        browser = self.browser
        browser.maximize_window()

        browser.get("https://kasirdemo.belajarqa.com/")
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div[1]/div/div/div/div[2]/div/div[3]/a").click()
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div[1]/div/div/div/div[2]/div/div[1]/input").send_keys(namatoko_random)
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div[1]/div/div/div/div[2]/div/div[2]/input").send_keys(email_random)
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div[1]/div/div/div/div[2]/div/div[3]/div/input").send_keys(password_register)
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div[1]/div/div/div/div[2]/div/button").click()
        time.sleep(3)
        response_message = browser.find_element(By.XPATH,"/html/body/div[1]/div/div/div/div[2]/div/div[1]").text
        time.sleep(1)

        self.assertEqual(response_message,'"email" must be a valid email')
        time.sleep(2)
    
def tearDown(self):
    self.browser.close()

if __name__ == "__main__":
    unittest.main()
        