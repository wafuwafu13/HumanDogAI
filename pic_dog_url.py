import requests
import re
import uuid
from bs4 import BeautifulSoup

url = "https://ailovei.com/?p=17237&page="

for num in range(5):
    r = requests.get(url + str(num))
    soup = BeautifulSoup(r.text, 'lxml')
    imgs = soup.find_all('img')
    print(imgs)
    for img in imgs:
        r = requests.get(img['src'])
        with open(str('./dog/')+str(uuid.uuid4())+str('.jpeg'),'wb') as file:
                file.write(r.content)