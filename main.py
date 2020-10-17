# words = driver.find_element_by_xpath(
#     "/html/body/app-root/app-typer/div[1]/div[1]/div[1]/div").text
# screenWidth, screenHeight = pyautogui.size()
# time.sleep(3)
# print(screenHeight, screenWidth)

# from urllib.request import urlopen as uReq
# from bs4 import BeautifulSoup as soup

# theUrl = "https://typefast.io/"

# uClient = uReq(theUrl)
# html = uClient.read()
# uClient.close()
# page_soup = soup(html, "html.parser")

# # /html/body/app-root/app-typer/div[1]/div[1]/div[1]/div
# words = page_soup.findAll("div", {"class": "word"})
# print(len(words))
# print(page_soup)


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

PATH = "C:\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://typefast.io")
time.sleep(2)

# content = driver.page_source
typeBar = driver.find_element_by_class_name('word-input')

wordsString = ''
def listToString():
    wordsList = driver.find_elements_by_class_name('word')
    for word in wordsList:
        wordsString += word.text + " "

listToString()
print(wordsString)
typeBar.send_keys(wordsString)

# time.sleep(10)
# driver.quit()
