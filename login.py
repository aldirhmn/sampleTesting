import unittest
from selenium import webdriver
import os
from LoginPage.loginPage import loginPage
import HtmlTestRunner
from Penjualan.penjualanPage import penjualanPage

class Test_login(unittest.TestCase):

    @classmethod
    def setUp(cls):
        projectDir1 = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        cls.driver = webdriver.Chrome(executable_path=projectDir1+'/drivers/chromedriver.exe')
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
        
    def test_a_success_login(self):
        driver = self.driver
        driver.maximize_window()
        driver.get("https://kasirdemo.belajarqa.com/") #url

        login = loginPage(driver)
        login.input_email("akunml24@gmail.com")
        login.input_password("Akunml24")
        login.click_login()
        login.validation_after()
        #
        # penjualan = penjualanPage(driver)
        # penjualan.click_menu_penjualan()
        # penjualan.add_penjualan()

    def test_a_failed_login(self):
        driver = self.driver
        driver.maximize_window()
        driver.get("https://kasirdemo.belajarqa.com/")

        emailList = ["", "email", "emailsalah@email.salah"]
        passwordList = ["", "aldi", "Akunml24"]

        login = loginPage(driver)
        for a in emailList:
            for b in passwordList:
                login.input_email(a)
                login.input_password(b)
                login.click_login()
                login.clear_text()
    @classmethod
    def tearDown(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Selesai!")

if __name__=="__main__":
    projectDir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=projectDir+'/Report/'))