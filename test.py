import requests
import json
from bs4 import BeautifulSoup
import csv
import time

url = 'https://cpdocket.cp.cuyahogacounty.us'
payload = {}
headers = {}


proxies = {
    "https": "https://167.179.113.45:3128"
}


s = requests.Session()

response = s.get(url, proxies=proxies)
cookies = response.cookies
html = BeautifulSoup(response.content, 'html.parser')

print (html)