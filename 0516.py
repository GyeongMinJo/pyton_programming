
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
from selenium.webdriver.chrome.options import Options

from webdriver_manager.chrome import ChromeDriverManager

chrome_options = Options()
chrome_options.add_experimental_option("detach",True)
chrome_options.add_experimental_option("excludeSwitches",["enable-logging"])


Service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=Service,options=chrome_options)
'''
driver.get("https://www.naver.com")
time.sleep(2)
driver.find_element(By.XPATH,"/html/body/div[2]/div[2]/div[2]/div[1]/div[1]/ul[2]/li[2]/a").click()
time.sleep(2)
#newstitle = driver.find_element(By.XPATH,"/html/body/div[2]/div/section[1]/div[2]/div/div[1]/div[2]/div/div/div[3]/ul[1]/li[1]/a").text
#print(newstitle)

driver.get("https://m.land.naver.com/search")
time.sleep(1)
driver.find_element(By.XPATH,"/html/body/div[1]/div/div[10]/div[2]/header/div[2]/form/div/input").click()
time.sleep(1)
driver.find_element(By.XPATH,"/html/body/div[1]/div/div[10]/div[2]/header/div[2]/form/div/input").send_keys("우성꿈동산")
time.sleep(1)
driver.find_element(By.XPATH,"/html/body/div[1]/div/div[10]/div[2]/header/div[2]/form/div/button[2]/i").click()
time.sleep(2)
rentprice = driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[5]/div/section/div/div/div[1]/div[2]/div/div/dl[2]/dd").text
print(rentprice)
'''
lst=[]
lst1=[]
dic={}
driver.get("https://finance.naver.com/")
time.sleep(1)
for i in range(10) :
 subject = driver.find_element(By.XPATH,f"/html/body/div[3]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/table/tbody/tr[{i+1}]/th/a").text
 sbprice = driver.find_element(By.XPATH,f"/html/body/div[3]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/table/tbody/tr[{i+1}]/td[1]").text
 lst.append(subject)
 lst1.append(sbprice)

dic=dict(zip(lst,lst1))

print(dic)
