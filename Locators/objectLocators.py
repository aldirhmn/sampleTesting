import random

class objectLocator():
    # Login Page
        field_email_id = 'email'
        field_password_id = 'password'
        button_login_xpath = '//button[@type=\'submit\']'
        validation_xpath = '//dd[normalize-space()=\'hai\']'

    # Penjualan Page
        button_menu_penjualan = "(//div[@class='css-ewi1jp'])[3]"
        button_tambah_penjualan = "(//a[normalize-space()='tambah'])[1]"
        field_cari_produk = "(//input[@placeholder='cari produk'])"
        button_cari_produk = "(//div[@class='chakra-input__right-addon css-7nrq'])[2]"
        randomNumber = random.randint(3, 7)
        field_pilih_produk = "(//tr[@role='row'])["+str(randomNumber)+"]"
        field_jumlah_barang = "(//td[@role='gridcell'])[4] /input"
        total_jumlah_bayar = "//div[@class='css-0'][2] /h2"
        field_jumlah_harga = "//input[@placeholder='...jumlah bayar']"
        button_bayar = "//button[normalize-space()='Bayar']"

        transaksi_sukses = "(//header[normalize-space()='transaksi sukses'])[1]"
        popup_total = "//div[contains(@class,'chakra')]//h2[2]"
        popup_bayar = "//div[contains(@class,'chakra')]//h2[4]"
        button_tutup = "(//button[normalize-space()='tutup'])[1]"
