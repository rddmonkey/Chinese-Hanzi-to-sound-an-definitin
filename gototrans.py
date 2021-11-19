
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import webbrowser
import pyperclip as pc

'''print(f"Please input your Hanzi: ")
hanzi = input()'''

PATH = "C:\Program Files (x86)\chromedriver.exe"
options = Options()
options.add_argument(r"user-data-dir=C:\Users\Richd\AppData\Local\Google\Chrome\User Data")
driver = webdriver.Chrome(PATH, chrome_options=options)

driver.get(f"https://forvo.com/word/汉字/#zh")




