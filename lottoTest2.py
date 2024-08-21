import requests
from bs4 import BeautifulSoup
from datetime import datetime

url = "https://dhlottery.co.kr/common.do?method=main"

html = requests.get(url).text  # 위 주소의 html 소스코드를 가져와서 저장

print(html)

soup = BeautifulSoup(html, 'html.parser')
recent_count = soup.find('strong', {'id':'lottoDrwNo'}).text.strip()  # 가장 최신 회차
recent_count = int(recent_count)
print(recent_count)