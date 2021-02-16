from logging import log
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
import requests
import os
from bs4 import BeautifulSoup

#opts = Options()
#opts.headless = True
#browser = webdriver.Firefox(options=opts)

profile = webdriver.FirefoxProfile()
profile.set_preference("browser.cache.disk.enable", False)
profile.set_preference("browser.cache.memory.enable", False)
profile.set_preference("browser.cache.offline.enable", False)
profile.set_preference("network.http.use-cache", False)
profile.set_preference("general.useragent.override", "Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 selenium.py")

browser = webdriver.Firefox(profile)
browser.delete_all_cookies()

init_url = "https://www.pinterest.com/login"
url = input("Please input a pinterest board url: ")

#init_url = "https://www.pinterest.com/login/"
#url = "https://www.pinterest.com/ninosc298/art-deco"


print("login to your account")
email = input("email: ")
password = input("password: ")

def login():
    browser.get(init_url)
    time.sleep(1)
    log_email = browser.find_element_by_id("email")
    log_pw = browser.find_element_by_id("password")
    log_email.clear()
    log_pw.clear()
    log_email.send_keys(email)
    log_pw.send_keys(password)
    log_pw.send_keys(u'\ue007')

login()

if(browser.current_url == init_url):
    login()
else:
    browser.get(url)




def scrollDown():
    lenOfPage = browser.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
    match=False
    while(match==False):
            lastCount = lenOfPage
            time.sleep(2)
            lenOfPage = browser.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
            if lastCount==lenOfPage:
                match=True

def getImgUrls(url, folder):
    try:
        os.mkdir(os.path.join(os.getcwd(), folder))
    except:
        pass
    os.chdir(os.path.join(os.getcwd(), folder))

    source_data = browser.page_source
    soup = BeautifulSoup(source_data, 'lxml')
    imgs = soup.find_all('img')
    for img in imgs:
        name = img['alt'][:128]
        problem = img['src'].split('/')[3]
        url_clean = img['src'].replace(problem, 'originals')
        with open(name.replace(' ', '_').replace('/','_').replace('.','_') + '.jpg', 'wb') as f:
            img = requests.get(url_clean)
            f.write(img.content)
            print('Writing: ',name)



scrollDown()
folder = input("name the folder: ")
getImgUrls(url, folder)






















