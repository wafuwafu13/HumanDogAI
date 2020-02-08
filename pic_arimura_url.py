import requests
import re
import uuid
from bs4 import BeautifulSoup

url = "https://matome.naver.jp/odai/2139002448252226701?&page="

for num in range(35):
    r = requests.get(url + str(num))
    soup = BeautifulSoup(r.text, 'lxml')
    imgs = soup.find_all('img')
    print(imgs)
    for img in imgs:
        r = requests.get(img['src'])
        with open(str('./arimura/')+str(uuid.uuid4())+str('.jpeg'),'wb') as file:
                file.write(r.content)