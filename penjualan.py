import unittest
from selenium import webdriver
import os
import HtmlTestRunner
from Penjualan.penjualanPage import penjualanPage
from login import Test_login
class Test_penjualan(unittest.TestCase):

    @classmethod
    def setUp(cls):
        projectDir1 = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        cls.driver = webdriver.Chrome(executable_path=projectDir1+'/drivers/chromedriver.exe')
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_success_penjualan(self):
        driver = self.driver

        Test_login.test_a_success_login()

        penjualan = penjualanPage(driver)
        penjualan.click_menu_penjualan()
        penjualan.add_penjualan()

    @classmethod
    def tearDown(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Selesai!")


if __name__=="__main__":
    projectDir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=projectDir+'/Report'))