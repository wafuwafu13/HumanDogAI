import requests
import re
import uuid
from bs4 import BeautifulSoup

url = "https://matome.naver.jp/odai/2136758803928083601?page="

for num in range(10):
    try:
        r = requests.get(url + str(num))
        soup = BeautifulSoup(r.text, 'lxml')
        imgs = soup.find_all('img')
        for img in imgs:
            r = requests.get(img['src'])
            with open(str('./siraishi/')+str(uuid.uuid4())+str('.jpeg'),'wb') as file:
                    file.write(r.content)
    except OSError as e:
        pass