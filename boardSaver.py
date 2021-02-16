from logging import log
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

browser = webdriver.Firefox()

#init_url = ("https://www.pinterest.com/login")
#url = input("Please input a pinterest board url")

init_url = "https://www.pinterest.com/login/"
url = "https://www.pinterest.com/ninosc298/art-deco"


#print("login to your account")
#email = input("email:")
#password = input("password:")

def login():
    browser.get(init_url)
    time.sleep(1)
    log_email = browser.find_element_by_id("email")
    log_pw = browser.find_element_by_id("password")
    log_email.clear()
    log_pw.clear()
    log_email.send_keys("ninosc298@hotmail.com")
    log_pw.send_keys("Guilhas123#")
    log_pw.send_keys(u'\ue007')

login()
browser.get(url)




def scrollDown():
    lenOfPage = browser.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
    match=False
    while(match==False):
            lastCount = lenOfPage
            time.sleep(1)
            lenOfPage = browser.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
            if lastCount==lenOfPage:
                match=True

def getImgUrls():
    source_data = browser.page_source
    soup = BeautifulSoup(source_data, 'lxml')
    imgs = soup.find_all('img')
    for img in imgs:
        problem = img['src'].split('/')[3]
        url_clean = img['src'].replace(problem, 'originals')
        print(url_clean)

scrollDown()
getImgUrls()






















