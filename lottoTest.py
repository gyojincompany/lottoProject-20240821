# pip install requests
# pip install beautifulsoup4

import requests
from bs4 import BeautifulSoup
from datetime import datetime

url = "https://dhlottery.co.kr/gameResult.do?method=byWin&drwNo=1133"

html = requests.get(url).text  # 위 주소의 html 소스코드를 가져와서 저장

# print(html)

soup = BeautifulSoup(html, 'html.parser')
date = soup.find('p', {'class':'desc'}).text  # 로또 추첨일
print(date)
lottoDate = datetime.strptime(date, "(%Y년 %m월 %d일 추첨)")
print(lottoDate)

lottoNumber = soup.find('div',{'class':'num win'}).find('p').text.strip().split('\n')
print(lottoNumber)

lottoNumberList = []
for num in lottoNumber:
    num = int(num)
    lottoNumberList.append(num)

print(lottoNumberList)

bonusNumber = soup.find('div', {'class':'num bonus'}).find('p').text.strip()
bonusNumber = int(bonusNumber)
print(bonusNumber)

