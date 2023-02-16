import time
from selenium.webdriver.common.by import By
from Locators.objectLocators import objectLocator

class penjualanPage():

    def __init__(self, driver):
        self.driver = driver

    def click_menu_penjualan(self):
        self.driver.find_element(By.XPATH, objectLocator.button_menu_penjualan).click() #click penjualan
        time.sleep(1)

    def add_penjualan(self):
        self.driver.find_element(By.XPATH,objectLocator.button_tambah_penjualan).click() #click tambah
        self.driver.find_element(By.XPATH,objectLocator.field_cari_produk).send_keys("mouse logitech") #input dilabel search
        self.driver.find_element(By.XPATH,objectLocator.button_cari_produk).click() #search
        self.driver.find_element(By.XPATH,objectLocator.field_pilih_produk).click() #choose/click produk mouse logitech
        self.driver.find_element(By.XPATH,objectLocator.field_jumlah_barang).clear() #clear textfield jumlah produk
        self.driver.find_element(By.XPATH,objectLocator.field_jumlah_barang).send_keys('2') #input jumlah produk
        jumBayar = self.driver.find_element(By.XPATH,objectLocator.total_jumlah_bayar).text
        self.driver.find_element(By.XPATH,objectLocator.field_jumlah_harga).send_keys(jumBayar) # input jumlah bayar
        self.driver.find_element(By.XPATH,objectLocator.button_bayar).click() #click bayar

        response_message_transaksi = self.driver.find_element(By.XPATH,objectLocator.transaksi_sukses).text #validasi
        response_data1 = self.driver.find_element(By.XPATH,objectLocator.popup_total).text
        response_data2 = self.driver.find_element(By.XPATH,objectLocator.popup_bayar).text

        assert response_message_transaksi == 'transaksi sukses'
        assert jumBayar == response_data1
        assert jumBayar == response_data2

        self.driver.find_element(By.XPATH,objectLocator.button_tutup).click() #click tutup
        time.sleep(2)