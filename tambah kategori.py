import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

class Test_Tambah_Kategori(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    
    def test_success_tambah_kategori(self):
        browser = self.browser
        browser.maximize_window()

        browser.get("https://kasirdemo.belajarqa.com/") #url
        time.sleep(1)
        browser.find_element(By.ID,"email").send_keys("akunml24@gmail.com") #input email
        time.sleep(1)
        browser.find_element(By.ID,"password").send_keys("Akunml24") #input password
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div[1]/div/div/div/div[2]/div/button").click() #click login
        time.sleep(2)

        response_message = browser.find_element(By.XPATH,"/html/body/div[1]/div/div/div/div[2]/div/div[1]/div[1]/div").text #validasi
        self.assertIn('hai', response_message)

        browser.find_element(By.XPATH,"/html/body/div[1]/div/div/div[1]/div/a[5]/div").click() #klik kategori
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div[1]/div/div/div[2]/div[2]/div[2]/a").click() #klik tambah
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div[1]/div/div/div[2]/div[2]/div[2]/div[1]/div/input").send_keys("Elektronik/Gaming1") #input nama kategori
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div[1]/div/div/div[2]/div[2]/div[2]/div[2]/div/input").send_keys("Gaming Gear") #input deskripsi
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div[1]/div/div/div[2]/div[2]/div[2]/button").click() #klik simpan
        time.sleep(2)

        response_message = browser.find_element(By.XPATH,"/html/body/div[2]/ul[3]/li/div/div/div/div[1]").text #validasi
        response_message2 = browser.find_element(By.XPATH,"/html/body/div[2]/ul[3]/li/div/div/div/div[2]").text
        time.sleep(2)

        self.assertEqual(response_message, 'success')
        self.assertEqual(response_message2, 'item ditambahkan')
        time.sleep(2)

    
    def tearDown(self):
        self.browser.close()

if __name__ == '__main__':
    unittest.main()