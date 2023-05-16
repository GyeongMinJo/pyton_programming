
from bs4 import BeautifulSoup

import requests

headers = {
    "User-Agent":"Dongyang Mirae Univ"
}

webpage = requests.get("https://n.news.naver.com/mnews/article/015/0004844821?sid=104",headers=headers)
print(webpage)

soup = BeautifulSoup(webpage.content,"html.parser")
print(soup)

news = soup.select_one('#dic_area').get_text().strip()
print(news)

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

from webdriver_manager.chrome import ChromeDriverManager

Service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=Service)

driver.get("https://www.naver.com")
time.sleep(2)
driver.find_element(By.XPATH,"/html/body/div[2]/div[2]/div[2]/div[1]/div[1]/ul[2]/li[2]/a").click()
time.sleep(30)
