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
import time

# open chrome driver
PATH = "C:\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://typefast.io")
time.sleep(2)

# find element to type into
typeBar = driver.find_element_by_class_name('word-input')

# finds and inserts words into input element function
wordsToInsert = ''


def wordInsertion():
    global wordsToInsert
    wordsToRemove = wordsToInsert
    wordsToInsert = ''

    # finds visible words and puts them into wordsString
    wordList = driver.find_elements_by_class_name('word')
    for word in wordList:
        wordsToInsert += word.text + " "

    # deletes the last words from the string
    try:
        wordsToRemove = wordsToRemove.split(' ')
        print('lastWords: ')
        print(wordsToRemove)
    except:
        pass

    for wordToRemove in wordsToRemove:
        wordsToInsert = wordsToInsert.replace(wordToRemove, '')

    # inserts them into the input element
    print('wordsString: ' + wordsToInsert)
    typeBar.send_keys(wordsToInsert)
    time.sleep(0.5)


for x in range(15):
    wordInsertion()

# sleeps before shutting down
time.sleep(10)
driver.quit()
