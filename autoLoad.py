from selenium import webdriver
import time

# Inisialisasi browser Selenium
driver = webdriver.Chrome()

# Fungsi untuk merefresh halaman
def refresh_page(url, refresh_interval):
    while True:
        driver.get(url)
        time.sleep(refresh_interval)

# URL halaman web yang ingin direfresh
url = "https://www.loket.com/"

# Interval waktu antara setiap refresh (dalam detik)
refresh_interval = 1

# Memulai proses refresh
refresh_page(url, refresh_interval)
