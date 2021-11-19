
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import webbrowser
import pyperclip as pc

'''print(f"Please input your Hanzi: ")
hanzi = input()'''

PATH = "C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(PATH)
def zhtoeng(hanzi):
    '''webbrowser.open(f"https://forvo.com/word/{hanzi}/#zh")'''
    driver.get(f"https://www.mdbg.net/chinese/dictionary?page=worddict&wdrst=0&wdqb={hanzi}")

    sound = driver.find_element_by_class_name("hanzi").text
    pinyin = driver.find_element_by_class_name("pinyin").text
    definition = driver.find_element_by_class_name("defs").text
    return (pinyin,definition,sound)

#print(zhtoeng("表扬"))


