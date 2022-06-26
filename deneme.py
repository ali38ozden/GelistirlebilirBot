from tkinter import *
from tkinter import messagebox
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import random

def basla():
    global driver
    options = webdriver.ChromeOptions()
    options.add_argument('--user-data-dir=C:\\Users\\ali\\AppData\\Local\\Google\\Chrome\\User Data')
    driver = webdriver.Chrome(chrome_options=options)
    driver.switch_to.new_window("windows")
    driver.get("https://www.instagram.com")
    driver.maximize_window()
basla()