
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import webbrowser
import pyperclip as pc

hanzi = "负面"

PATH = "C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(PATH)

driver.get(f"https://forvo.com/word/{hanzi}/#zh")

driver.find_element_by_class_name("download").click()

