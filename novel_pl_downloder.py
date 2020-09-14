from bs4 import BeautifulSoup
from selenium import webdriver
import requests
import time
path = r'C:\\Users\\chakh\\Desktop\\novel pl (novel downloder)\\chromedriver.exe'
driver1 = webdriver.Chrome(executable_path=path)

driver1.get("https://www.novels.pl")


time.sleep(60)

link = []
url = 'https://www.novels.pl/novel/LOAR/131/Chapter-131--Deepseated-Strength-of-the-Hell-Sect.html'
n = 1550
for i in range(131, n):
    source = requests.get(url).text
    soup = BeautifulSoup(source, 'html')

    dl = soup.find('a', class_='_download')
    link.append(dl['href'])
    print(i)
    if i == n-1:
        break
    nextl = soup.find('li', class_='next').a
    url = "https://www.novels.pl"+nextl['href']


for i in link:
    driver1.execute_script("window.open('"+str(i) + "');")
    time.sleep(6)
