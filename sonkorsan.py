from tkinter import messagebox
from selenium import webdriver




options = webdriver.ChromeOptions()
options.add_argument('--user-data-dir=C:\\Users\\ali\\AppData\\Local\\Google\\Chrome\\User Data')
driver = webdriver.Chrome(chrome_options=options)
driver.get("https://www.instagram.com")
driver.maximize_window()