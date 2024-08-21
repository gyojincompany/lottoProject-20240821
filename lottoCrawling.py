# pip install requests
# pip install beautifulsoup4

import requests
from bs4 import BeautifulSoup
from datetime import datetime
import pandas as pd
from sqlalchemy import create_engine
import pymysql

def get_lottoNum(count):  # 로또추첨회차를 입력 받아서 당첨번호를 추출해주는 함수
    url = f"https://dhlottery.co.kr/gameResult.do?method=byWin&drwNo={count}"
    html = requests.get(url).text  # 위 주소의 html 소스코드를 가져와서 저장
    soup = BeautifulSoup(html, 'html.parser')
    date = soup.find('p', {'class': 'desc'}).text  # 로또 추첨일
    lottoDate = datetime.strptime(date, "(%Y년 %m월 %d일 추첨)")
    lottoNumber = soup.find('div', {'class': 'num win'}).find('p').text.strip().split('\n')
    lottoNumberList = []
    for num in lottoNumber:
        num = int(num)
        lottoNumberList.append(num)

    bonusNumber = soup.find('div', {'class': 'num bonus'}).find('p').text.strip()
    bonusNumber = int(bonusNumber)

    lottoData = {'lottoDate':lottoDate, 'lottoNumber':lottoNumberList, 'bonusNumber': bonusNumber}

    return lottoData

# print(get_lottoNum(1133))

def get_recent_lottocount():  # 최신 로또 회차 크롤링 함수
    url = "https://dhlottery.co.kr/common.do?method=main"
    html = requests.get(url).text  # 위 주소의 html 소스코드를 가져와서 저장
    soup = BeautifulSoup(html, 'html.parser')
    recent_count = soup.find('strong', {'id': 'lottoDrwNo'}).text.strip()  # 가장 최신 회차
    recent_count = int(recent_count)
    return recent_count

lottoNumList = []

for count in range(1, get_recent_lottocount()+1):
    lottoResult = get_lottoNum(count)
    lottoNumList.append({
        'count': count,  # 로또 추첨 회차
        'lottoDate': lottoResult['lottoDate'],  # 로또 추첨일
        'lottoNum1': lottoResult['lottoNumber'][0],  # 로또 당첨번호 중 첫번째 당첨번호
        'lottoNum2': lottoResult['lottoNumber'][1],  # 로또 당첨번호 중 첫번째 당첨번호
        'lottoNum3': lottoResult['lottoNumber'][2],  # 로또 당첨번호 중 첫번째 당첨번호
        'lottoNum4': lottoResult['lottoNumber'][3],  # 로또 당첨번호 중 첫번째 당첨번호
        'lottoNum5': lottoResult['lottoNumber'][4],  # 로또 당첨번호 중 첫번째 당첨번호
        'lottoNum6': lottoResult['lottoNumber'][5],  # 로또 당첨번호 중 첫번째 당첨번호
        'bonusNum': lottoResult['bonusNumber']  # 로또 버보너스 번호
    })

print(lottoNumList)
