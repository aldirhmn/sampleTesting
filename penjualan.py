import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

class Test_penjualan(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    
    def test_success_penjualan(self):
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

        browser.find_element(By.XPATH,"/html/body/div[1]/div/div/div[1]/div/a[3]/div").click() #click penjualan
        time.sleep(1)
        browser.find_element(By.XPATH,"//html/body/div[1]/div/div/div[2]/div[2]/div[2]/a").click() #click tambah
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div[1]/div/div/div[2]/div[2]/div/div[2]/div[2]/div[1]/div/div/div/input").send_keys("mouse logitech") #input dilabel search
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div[1]/div/div/div[2]/div[2]/div/div[2]/div[2]/div[1]/div/div/div/div").click() #search
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div[3]/div[4]/div/section/div/table/tbody/tr[1]").click() #choose/click produk mouse logitech
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div[1]/div/div/div[2]/div[2]/div/div[2]/div[2]/table/tbody/tr/td[4]/input").clear() #clear textfield jumlah produk
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div[1]/div/div/div[2]/div[2]/div/div[2]/div[2]/table/tbody/tr/td[4]/input").send_keys('2') #input jumlah produk
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div[1]/div/div/div[2]/div[2]/div/div[3]/div/div/div/input").send_keys("3000000") # input jumlah bayar
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div[1]/div/div/div[2]/div[2]/div/div[3]/div/div/button").click() #click bayar
        time.sleep(3)

        response_message_transaksi = browser.find_element(By.XPATH,"/html/body/div[4]/div[4]/div/section/header").text #validasi
        time.sleep(1)
        response_data1 = browser.find_element(By.XPATH,"/html/body/div[4]/div[4]/div/section/div/h2[1]").text
        time.sleep(1)
        response_data2 = browser.find_element(By.XPATH,"/html/body/div[4]/div[4]/div/section/div/h2[3]").text
        time.sleep(1)
        response_data3 = browser.find_element(By.XPATH,"/html/body/div[4]/div[4]/div/section/div/h2[5]").text
        time.sleep(1)

        self.assertEqual(response_message_transaksi,"transaksi sukses")
        time.sleep(1)
        self.assertIn('total :', response_data1)
        time.sleep(1)
        self.assertIn('bayar :', response_data2)
        time.sleep(1)
        self.assertIn('kembalian :', response_data3) #validasi
        time.sleep(1)

        browser.find_element(By.XPATH,"/html/body/div[4]/div[4]/div/section/footer/button").click() #click tutup
        time.sleep(2)
    
    def tearDown(self):
        self.browser.close()

if __name__ == '__main__':
    unittest.main()