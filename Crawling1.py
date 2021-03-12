import requests
from bs4 import BeautifulSoup

url = 'https://wikidocs.net/85737'
response = requests.get(url)

#응답코드
print(response.status_code)

#코드
print(response.text)