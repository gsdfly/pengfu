import requests
from bs4 import BeautifulSoup
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",'content-type':'application/json'}

print(BeautifulSoup(requests.get('http://www.baidu.com',headers=headers).content,'html.parser').title)