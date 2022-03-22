#Library
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

#Menjalankan Web Browser

driver = webdriver.Chrome(ChromeDriverManager().install())
#Fullscreen Window
driver.maximize_window()
#Membuka website gmaps
driver.get("https://www.google.com/maps/@-2.44565,117.8888,4z")
time.sleep(3)

#Interaksi otomatis
#tujuan dan asal
tujuan = "UGM, Bulaksumur, Caturtunggal, Kabupaten Sleman, Daerah Istimewa Yogyakarta"
asal = "Stasiun Yogyakarta, Jl. Ps. Kembang No.77, Sosromenduran, Gedong Tengen, Kota Yogyakarta, Daerah Istimewa Yogyakarta 55271"

driver.find_element_by_xpath("/html/body/div[3]/div[9]/div[3]/div[1]/div[1]/div[1]/div[2]/form/div/div[3]/div/input[1]").send_keys(tujuan)
# search
try:
    element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/div[9]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/button"))
    )
finally:
    driver.find_element_by_xpath("/html/body/div[3]/div[9]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/button").click()
    #click card location
    #direction
    try:
        element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/div[9]/div[8]/div/div[1]/div/div/div[4]/div[1]/button/span/img"))
        )
    finally:
        time.sleep(3)
        driver.find_element_by_xpath("/html/body/div[3]/div[9]/div[8]/div/div[1]/div/div/div[4]/div[1]/button/span/img").click()
        # starting point
        time.sleep(3)
        driver.find_element_by_xpath("/html/body/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[1]/div[2]/div[1]/div/input").send_keys(asal)
        # search
        time.sleep(3)
        driver.find_element_by_xpath("/html/body/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[1]/div[2]/button[1]").click()

        driver.implicitly_wait(20) # gives an implicit wait for 20 seconds
        # ambil nama jalan rute
        jalan_pertama = driver.find_element_by_xpath("/html/body/div[3]/div[9]/div[8]/div/div[1]/div/div/div[4]/div[1]/div/div[1]/div[2]/h1[1]/span")
        jalan_kedua = driver.find_element_by_xpath("/html/body/div[3]/div[9]/div[8]/div/div[1]/div/div/div[4]/div[2]/div/div[1]/div[2]/h1[1]/span")
        try:
            element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/div[9]/div[8]/div/div[1]/div/div/div[4]/div[3]/div/div[1]/div[2]/h1[1]/span"))
            )
        finally:
            jalan_ketiga = driver.find_element_by_xpath("/html/body/div[3]/div[9]/div[8]/div/div[1]/div/div/div[4]/div[3]/div/div[1]/div[2]/h1[1]/span")

            string_pertama = jalan_pertama.text
            string_kedua = jalan_kedua.text
            string_ketiga = jalan_ketiga.text

            time.sleep(3)

            print("Jalannya adalah : \n")
            # Jl. Cik Di Tiro
            print(string_pertama)
            assert 'Jl. Cik Di Tiro' in string_pertama
            # berubah
            # Jl. Jend. Sudirman
            print(string_kedua)
            assert 'Jl. Jend. Sudirman' in string_kedua
            # berubah
            # Jl. DR. Sardjito
            print(string_ketiga)
            assert 'Jl. DR. Sardjito' in string_ketiga
            time.sleep(5)
            driver.close()


