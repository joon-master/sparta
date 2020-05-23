import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient
client = MongoClient('localhost',27017)
db = client.dbsparta

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&ymd=20200403&hh=23&rtm=N&pg=1',headers=headers)

soup = BeautifulSoup(data.text,'html.parser')

musics = soup.select('#body-content > div.newest-list > div > table > tbody > tr')

for music in musics:
    musicName = music.select_one('td.info > a')
    if musicName is not None:
        musicTitle = music.select_one('td.info > a.title.ellipsis').text
        musicArtist = music.select_one('td.info > a.artist.ellipsis').text
        musicRank = music.select_one('td.number').text[0:2]
        print(musicRank.strip(),musicTitle.strip(),musicArtist)
        doc = {
            'musicTitle' : musicTitle,
            'musicArtist' : musicArtist,
            'musicRank' : musicRank
        }
        db.jinyMusic.insert_one(doc)
#body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.number
#body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.info > a.artist.ellipsis
#body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.number
#body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.info > a.title.ellipsis
#body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.number