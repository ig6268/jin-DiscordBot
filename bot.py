from bs4 import BeautifulSoup
from selenium import webdriver

from uuid import uuid4
from urllib.request import urlopen, Request

import asyncio
import discord
import requests
import json
import time
import urllib
import asyncio
import random

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument("disable-gpu")

#각 서버의 셀레니움 경로를 지정해주시길 바랍니다.
#서버 이전후, 사용시 주석태그를 설정 및 제거 해주시고 사용 하셔야 셀레니움 작동합니다.

#진범 서버
driver = webdriver.Chrome('/Users/PARK/chromedriver',chrome_options=options)

driver.implicitly_wait(3)

client = discord.Client()

# 1-6에서 생성된 토큰을 이곳에 입력해주세요.
token = '########################################'

# 봇이 구동되었을 때 동작되는 코드입니다.
@client.event
async def on_ready():
    print("Logged in as ") #화면에 봇의 아이디, 닉네임이 출력됩니다.
    print(client.user.name)
    print(client.user.id)
    print("===========")
    # 디스코드에는 현재 본인이 어떤 게임을 플레이하는지 보여주는 기능이 있습니다.
    # 이 기능을 사용하여 봇의 상태를 간단하게 출력해줄 수 있습니다.
    await client.change_presence(game=discord.Game(name="명령어 안내 : !도움", type=1))

# 봇이 새로운 메시지를 수신했을때 동작되는 코드입니다.
@client.event
async def on_message(message):
    if message.author.bot: #만약 메시지를 보낸사람이 봇일 경우에는
        return None #동작하지 않고 무시합니다.

    id = message.author.id #id라는 변수에는 메시지를 보낸사람의 ID를 담습니다.
    channel = message.channel #channel이라는 변수에는 메시지를 받은 채널의 ID를 담습니다.

    if message.content.startswith('!초대'): #만약 해당 메시지가 '!커맨드' 로 시작하는 경우에는
        in_link = 'https://discordapp.com/oauth2/authorize?client_id=477733283195781130&scope=bot'

        embed = discord.Embed(title='', colour=discord.Colour.green())
        embed.add_field(name='봇 초대링크', value=in_link, inline=False)
        embed.add_field(name='문의 or 건의사항', value='디스코드 : jin#6300\n 카카오톡 : https://open.kakao.com/o/sERaQgl', inline=False)
        await client.send_message(message.channel, embed=embed)

    if message.content.startswith('!안녕'):
        await client.send_message(message.channel, "안녕하세요~")

    if message.content.startswith('!도움'):

        embed = discord.Embed(title='BOT 명령어 모음', colour=discord.Colour.blue())
        embed.add_field(name='!사진 - 검색어\n!유튜브 - 검색어\n!날씨 - 지역명\n!실검\n!영화\n!링크 (바로가기 링크를 제공해드립니다.)\n!주사위\n!랜덤 (최소값) (최대값)\n!pubgdb - 아이템이름\n!배그 - 닉네임\n!상세전적 - 닉네임(상세정보)\n!지도 - 맵이름\n!롤 - 소환사명\n!인기챔프\n!메이플 - 닉네임\n!던파 - 서버 닉네임\n!로스트아크 - 닉네임', value='기능이 제공중입니다.', inline=False)
        #embed.add_field(name='!유튜브 - 검색어', value='유튜브 영상을 가져와줍니다.', inline=False)
        #embed.add_field(name='!날씨 - 지역명', value='날씨 정보를 알려줍니다.', inline=False)
        #embed.add_field(name='!배그db - 아이템이름', value='아이템 정보를 알려줍니다.', inline=False)
        #embed.add_field(name='!배그 - 닉네임', value='(닉네임)전적을 보여줍니다.', inline=False)
        #embed.add_field(name='!배그지도 - 맵이름(에란겔,미라마,사녹)', value='맵의 차량젠 위치를 보여줍니다.', inline=False)
        #embed.add_field(name='!던파 - 서버 + 닉네임', value='캐릭터 이미지,능력치를 보여줍니다.', inline=False)
        #embed.add_field(name='!메이플 - 캐릭명', value='캐릭터 이미지,순위를 보여줍니다.', inline=False)

        #embed.add_field(name='!실검', value='실시간 검색어 순위 1~10위를 알려줍니다.', inline=False)
        #embed.add_field(name='!영화', value='실시간 예매,누적관객수 1~4위를 알려줍니다.', inline=False)

        await client.send_message(message.channel, embed = embed)

    #-------------------------------------------------------------------------------------------------------------------------------------------------
    #$$$$$$$$\ $$$$$$$$\  $$$$$$\
    #$$  _____|\__$$  __|$$  __$$\
    #$$ |         $$ |   $$ /  \__|
    #$$$$$\       $$ |   $$ |
    #$$  __|      $$ |   $$ |
    #$$ |         $$ |   $$ |  $$\
    #$$$$$$$$\    $$ |   \$$$$$$  |
    #\________|   \__|    \______/

    #네이버 이미지
    if message.content.startswith('!사진'):
        print('사진 명령어 실행')
        temp = message.content.split(" ")

        mURL = "https://search.naver.com/search.naver?where=image&query=" + temp[1]
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
        }

        mTemp = requests.get(mURL, timeout=60, allow_redirects=False, headers=headers)
        mheader = mTemp.headers
        msoup = BeautifulSoup(mTemp.text, 'html.parser')

        img_res = msoup.find('div',{'id': 'content'}).find('div',{'class': 'sp_image section _prs_img_noc'}).find('div',{'class': 'photo_grid _box'}).find_all('div')
        #print(img_res[1])
        ran = random.randint(0,5)
        img_res1 = img_res[ran].find('a').find('img')
        img_res2 = str(img_res1)[str(img_res1).find('ce="')+4:str(img_res1).find('&amp')]
        #print(img_res2)
        embed = discord.Embed(title='검색결과', colour=discord.Colour.green())
        embed.set_image(url=img_res2)

        await client.send_message(message.channel, embed=embed)


    #YOUTUBE Search
    if message.content.startswith("!유튜브"):
        print('유튜브 명령어 실행')
        yt = message.content.split(" ")

        mURL = "https://www.youtube.com/results?search_query=" + yt[1]
        driver.get(mURL)

        yt_html = driver.page_source
        yt_soup = BeautifulSoup(yt_html,'html.parser')
        yt_res = yt_soup.find('div',{'id':'dismissable'}).find('a',{'id':'thumbnail'})
        yt_link = "https://www.youtube.com" + yt_res['href']

        await client.send_message(message.channel, yt_link)

    #날씨검색
    if message.content.startswith("!날씨"):
        print('날씨 명령어 실행')
        wea_learn = message.content.split(" ")
        location = wea_learn[1]
        enc_location = urllib.parse.quote(location+'날씨')

        mURL = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=' + enc_location
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
        }

        mTemp = requests.get(mURL, timeout=60, headers=headers)
        msoup = BeautifulSoup(mTemp.text, 'html.parser')

        todayBase = msoup.find('div', {'class': 'main_info'})

        todayTemp1 = todayBase.find('span', {'class': 'todaytemp'})
        todayTemp = todayTemp1.text.strip()  # 온도

        todayValueBase = todayBase.find('ul', {'class': 'info_list'})
        todayValue2 = todayValueBase.find('p', {'class': 'cast_txt'})
        todayValue = todayValue2.text.strip()  # 밝음,어제보다 ?도 높거나 낮음을 나타내줌

        todayMiseaMongi1 = msoup.find('div', {'class': 'sub_info'})
        todayMiseaMongi2 = todayMiseaMongi1.find('div', {'class': 'detail_box'})
        todayMiseaMongi3 = todayMiseaMongi2.find('dd')
        todayMiseaMongi = todayMiseaMongi3.text  # 미세먼지

        tomorrowBase = msoup.find('div', {'class': 'table_info weekly _weeklyWeather'})
        tomorrowTemp1 = tomorrowBase.find('li', {'class': 'date_info'})
        tomorrowTemp2 = tomorrowTemp1.find('dl')
        tomorrowTemp3 = tomorrowTemp2.find('dd')
        tomorrowTemp = tomorrowTemp3.text.strip()  # 오늘 오전,오후온도

        tomorrowAreaBase = msoup.find('div', {'class': 'tomorrow_area'})
        tomorrowMoring1 = tomorrowAreaBase.find('div', {'class': 'main_info morning_box'})
        tomorrowMoring2 = tomorrowMoring1.find('span', {'class': 'todaytemp'})
        tomorrowMoring = tomorrowMoring2.text.strip()  # 내일 오전 온도

        tomorrowValue1 = tomorrowMoring1.find('div', {'class': 'info_data'})
        tomorrowValue = tomorrowValue1.text.strip()  # 내일 오전 날씨상태, 미세먼지 상태

        tomorrowAreaBase = msoup.find('div', {'class': 'tomorrow_area'})
        tomorrowAllFind = tomorrowAreaBase.find_all('div', {'class': 'main_info morning_box'})
        tomorrowAfter1 = tomorrowAllFind[1]
        tomorrowAfter2 = tomorrowAfter1.find('p', {'class': 'info_temperature'})
        tomorrowAfter3 = tomorrowAfter2.find('span', {'class': 'todaytemp'})
        tomorrowAfterTemp = tomorrowAfter3.text.strip()  # 내일 오후 온도

        tomorrowAfterValue1 = tomorrowAfter1.find('div', {'class': 'info_data'})
        tomorrowAfterValue = tomorrowAfterValue1.text.strip()

        embed = discord.Embed(title=wea_learn[1]+ ' 날씨(Naver)', url = mURL, colour=discord.Colour.green())
        embed.set_thumbnail(url='https://blogfiles.pstatic.net/MjAxODExMDVfMTc4/MDAxNTQxNDAwMjI2NDAx.aHHw9T_Cwk61lMLYUW-snKE4xqwkzWbKGgsTVn6iwmgg.HsqcZu4sucA_DEfZpP8DUOXmX0j03J8rhTnKP57qu8gg.PNG.ig6268/%EB%84%A4%EC%9D%B4%EB%B2%84.PNG')
        embed.add_field(name='현재온도, 날씨', value=todayTemp+'˚, ' + todayValue, inline=False)  # 현재온도
        embed.add_field(name='현재 미세먼지', value=todayMiseaMongi, inline=False)  # 오늘 미세먼지
        embed.add_field(name='오늘 오전/오후 온도', value=tomorrowTemp + '\n **--------------------------------------**', inline=False)  # 오늘날씨
        embed.add_field(name='내일 오전/오후 온도', value=tomorrowMoring+'˚/' + tomorrowAfterTemp, inline=False)  # 내일오전오후날씨
        embed.add_field(name='내일 오전/오후 날씨', value=tomorrowValue + '\n' + tomorrowAfterValue, inline=False)  # 내일오전 날씨상태

        await client.send_message(message.channel,embed=embed)

    #실시간 검색어 순위
    if message.content.startswith("!실검"):
        print('실검 명령어 실행')
        mURL = "https://datalab.naver.com/keyword/realtimeList.naver?where=main"

        driver.get(mURL)
        rs_html = driver.page_source
        rs_soup = BeautifulSoup(rs_html,"html.parser")
        rs_list = rs_soup.find('div',{'class': 'rank_scroll'})
        #rs_list2 = rs_list.find('ul',{'class': 'rank_list v2'})
        rs_list3 = rs_list.find_all('span', {'class': 'title'})

        rs_time = rs_soup.find('div',{'class': 'time_indo'})
        rs_time2 = rs_time.find('span', {'class': 'time_txt _title_hms'})
        rs_time2 = str(rs_time2)[str(rs_time2).find('ms">')+4:str(rs_time2).find('</span>')]

        #rs_list3[0] = str(rs_list3[0])[str(rs_list3[0]).find('le">')+4:str(rs_list3[0]).find('</span>')]
        rs_int = range(10)
        for i in rs_int:
            rs_list3[i] = str(rs_list3[i])[str(rs_list3[i]).find('le">')+4:str(rs_list3[i]).find('</span>')]

        embed = discord.Embed(title = '실시간 검색어 순위(Naver)', url = 'https://naver.com', colour=discord.Colour.green())
        embed.set_thumbnail(url='https://blogfiles.pstatic.net/MjAxODExMDVfMTc4/MDAxNTQxNDAwMjI2NDAx.aHHw9T_Cwk61lMLYUW-snKE4xqwkzWbKGgsTVn6iwmgg.HsqcZu4sucA_DEfZpP8DUOXmX0j03J8rhTnKP57qu8gg.PNG.ig6268/%EB%84%A4%EC%9D%B4%EB%B2%84.PNG')
        embed.add_field(name=str(rs_time2) + '분 1위 ~ 10위', value = '\n1위  ' + rs_list3[0] + '\n2위 ' + rs_list3[1] +
        '\n3위 ' + rs_list3[2] + '\n4위 ' + rs_list3[3] + '\n5위 ' + rs_list3[4] + '\n6위 ' + rs_list3[5] +
        '\n7위 ' + rs_list3[6] + '\n8위 ' + rs_list3[7] + '\n9위 ' + rs_list3[8] + '\n10위 ' + rs_list3[9], inline=False)

        await client.send_message(message.channel,embed=embed)

    #영화 순위
    if message.content.startswith("!영화"):
        print('영화 명령어 실행')
        mURL = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
        }

        mTemp = requests.get(mURL, timeout=60, headers=headers)
        msoup = BeautifulSoup(mTemp.text, 'html.parser')

        mov_list = msoup.find('div',{'class': 'contents03'})
        mov_list2 = mov_list.find('div',{'class': '_content'}).find('ul')
        mov_list3 = mov_list2.find_all('li')

        mov_rank = 0

        for i in range(0,4):
            mov_rank = mov_rank + 1
            mov_chart = mov_list3[i]
            mov_thumb = mov_chart.find('div',{'class': 'thumb'}).find('img')
            mov_info = mov_chart.find('div',{'class': 'movie_info'})
            mov_name = mov_info.find('div',{'class': 'scm_ellipsis _ellipsis'})
            mov_name2 = mov_name.find('strong',{'class': 'scm_ellipsis_text _text'}) #영화 제목
            mov_info2 = mov_info.find('dl',{'class': 'movie_item'}).find_all('dd') #영화 개봉일, 일간,누적 관람객수

            embed = discord.Embed(title='현재 예매율 '+str(mov_rank)+'위', url = mURL, colour=discord.Colour.green())
            embed.set_thumbnail(url=mov_thumb['src'])
            embed.add_field(name=mov_name2.text.strip(), value = "\n개봉 : " + mov_info2[0].text.strip() +
            "\n누적/일간 : " + mov_info2[2].text.strip()+ " / " + mov_info2[1].text.strip(), inline=True)
            await client.send_message(message.channel, embed=embed)

#링크 모음
    if message.content.startswith("!링크"):
        print('링크 명령어 실행')
        #검색엔진
        a_link1 = 'https://www.naver.com'
        a_link2 = 'https://www.daum.net'
        a_link3 = 'https://www.google.com'
        a_link4 = 'https://www.nate.com'
        a_link5 = 'https://www.youtube.com'

        all_link1 = "[네이버]("+a_link1+") | [다음]("+a_link2+") | [구글]("+a_link3+") | [유튜브]("+a_link5+") | [네이트]("+a_link4+")"
        #소셜
        c_link1 = 'https://www.facebook.com/'
        c_link2 = 'https://www.instagram.com/'
        c_link3 = 'https://twitter.com/'
        c_link4 = 'https://accounts.kakao.com/login/kakaostory'
        c_link5 = 'https://band.us/home'

        all_link2 = "[페북]("+c_link1+") | [인스타]("+c_link2+") | [트위터]("+c_link3+") | [카스]("+c_link4+") | [밴드]("+c_link5+")"
        #쇼핑몰
        s_link1 = 'http://www.auction.co.kr/'
        s_link2 = 'http://www.gmarket.co.kr/'
        s_link3 = 'http://www.11st.co.kr/'
        s_link4 = 'http://www.interpark.com/'
        s_link5 = 'http://display.cjmall.com/'
        s_link6 = 'https://shopping.naver.com/'

        all_link3 = "[옥션]("+s_link1+") | [지마켓]("+s_link2+") | [11번가]("+s_link3+") | [인터파크]("+s_link4+") | [CJ몰]("+s_link5+") | [네이버쇼핑]("+s_link6+")"

        s_link7 = 'http://www.ticketmonster.co.kr/home'
        s_link8 = 'http://www.wemakeprice.com/'
        s_link9 = 'https://www.coupang.com/'
        s_link10 = 'http://www.g9.co.kr/'
        s_link11 = 'https://www.gsshop.com/'

        all_link4 = "[티몬]("+s_link7+") | [위메프]("+s_link8+") | [쿠팡]("+s_link9+") | [지구]("+s_link10+") | [GS샵]("+s_link11+")"

        #음약
        m_link1 = 'https://www.melon.com/'
        m_link2 = 'https://music.bugs.co.kr/'
        m_link3 = 'http://www.mnet.com/'
        m_link4 = 'http://www.genie.co.kr/'

        all_link5 = "[멜론]("+m_link1+") | [벅스]("+m_link2+") | [엠넷]("+m_link3+") | [지니]("+m_link4+")"

        #영화
        m_link5 = 'http://www.cgv.co.kr/'
        m_link6 = 'http://www.megabox.co.kr/'
        m_link7 = 'http://www.lottecinema.co.kr/'

        all_link6 = "[CGV]("+m_link5+") | [메가박스]("+m_link6+") | [롯데시네마]("+m_link7+")"

        #방송 플랫폼
        b_link1 = 'http://www.afreecatv.com/'
        b_link2 = 'https://www.twitch.tv/'
        b_link3 = 'https://tv.kakao.com/'
        b_link4 = 'https://tv.naver.com/'

        all_link7 = "[아프리카TV]("+b_link1+") | [트위치]("+b_link2+") | [카카오TV]("+b_link3+") | [네이버TV]("+b_link4+")"

        #전적 검색사이트
        g_link1 = 'http://fow.kr/'
        g_link2 = 'https://dak.gg/'
        g_link3 = 'http://www.op.gg/'

        all_link8 = "[FOW]("+g_link1+") | [닥지지]("+g_link2+") | [OP.GG]("+g_link3+")"

        embed = discord.Embed(title='', colour=discord.Colour.green())
        embed.set_author(name='바로가기')#,icon_url=mp_sv_img['src'], url=mp_url)
        embed.add_field(name='검색엔진', value = all_link1, inline=False)
        embed.add_field(name='소셜', value = all_link2, inline=False)
        embed.add_field(name='쇼핑몰', value = all_link3+'\n'+all_link4, inline=False)
        embed.add_field(name='음악', value = all_link5, inline=False)
        embed.add_field(name='영화', value = all_link6, inline=False)
        embed.add_field(name='방송 플랫폼', value = all_link7, inline=False)
        embed.add_field(name='전적 검색사이트', value = all_link8, inline=False)

        await client.send_message(message.channel,embed=embed)


    if message.content.startswith('!주사위'):
        print('주사위 명령어 실행')
        ran = random.randrange(1,7)
        if(ran%2 == 0):
            await client.send_message(message.channel, embed=discord.Embed(description='🎲주사위의 선택은?\n'+str(ran)+'\n짝'))
        if(ran%2 == 1):
            await client.send_message(message.channel, embed=discord.Embed(description='🎲주사위의 선택은?\n'+str(ran)+'\n홀'))

    if message.content.startswith('!랜덤'):
        print('랜덤 명령어 실행')
        temp = message.content.split(" ")

        ran = random.randrange(int(temp[1]),int(temp[2]))
        if(ran%2 == 0):
            await client.send_message(message.channel, embed=discord.Embed(description='🎲봇의 선택은?\n '+str(ran)+'\n짝'))
        if(ran%2 == 1):
            await client.send_message(message.channel, embed=discord.Embed(description='🎲봇의 선택은?\n '+str(ran)+'\n홀'))


#로스트아크 링크제공
    if message.content.startswith('!로스트아크'):
        print('로스트아크 명령어 실행')

        temp = message.content.split(" ")
        lost_name = urllib.parse.quote(temp[1]) # 아이디 url인코딩

        mURL = 'http://lostark.game.onstove.com/Profile/Character/' + lost_name
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
        }

        loa_link1 = 'http://loaq.kr/'#대기열
        loa_link2 = 'http://mococo.co/map'#모코코
        loa_link3 = 'http://lostark.inven.co.kr/'#인벤
        loa_link4 = 'http://lostark.game.onstove.com/'#공홈
        loa_link5 = 'https://loahae.com/calendar/'#로아해

        loa_all_link = "[공홈]("+mURL+") | [모코코]("+loa_link2+") | [로아인벤]("+loa_link3+") | [로아해]("+loa_link5+") | [대기열]("+loa_link1+")"

        embed = discord.Embed(title='', colour=discord.Colour.green())
        embed.add_field(name='링크', value= loa_all_link, inline=False)

        mTemp = requests.get(mURL, timeout=60, allow_redirects=False, headers=headers)
        mheader = mTemp.headers
        msoup = BeautifulSoup(mTemp.text, 'html.parser')

        lost_base = msoup.find('div',{'class': 'middle'}).find('main').find('div',{'class': 'content content--profile'})
        #if(lost_base.find('div',{'class': 'profile-ingame'}).find('div'){'class': 'profile-attention'}):
        #if not (lost_base.find('div',{'class': 'profile-ingame'}).find('div',{'class': 'profile-attention'}.find('h3')) in lost_base):
        lost_base2 = lost_base.find('div',{'class': 'profile-ingame'}).find('div',{'class': 'profile-character'})
        lost_base3 = lost_base2.find('h3')# 레벨, 캐릭터명

        lost_info = lost_base2.find('div',{'class': 'profile-info'})
        lost_info1 = lost_info.find('div',{'class': 'game-info'}).find_all('div')
        #0서버 1길드 2클래스 3칭호
        lost_info2 = lost_info1[0].find_all('span')#서버
        lost_info3 = lost_info1[1].find_all('span')#길드
        lost_info4 = lost_info1[2].find_all('span')#클래스
        lost_info5 = lost_info1[3].find_all('span')#칭호

        lost_lv = lost_info.find('div',{'class': 'level-info'}).find_all('div')
        #0아이템렙 1원정대렙 2pvp등급
        lost_lv1 = lost_lv[0].find_all('span')#템
        lost_lv2 = lost_lv[1].find_all('span')#원정대
        lost_lv3 = lost_lv[2].find_all('span')#pvp

        lost_char = lost_base2.find('div',{'class': 'lui-tab profile-tab'}).find('div',{'id': 'profile-ability'}).find('div',{'class': 'lui-tab profile-ability-tab'})
        lost_char2 = lost_char.find('div',{'id': 'profile-equipment'}).find('div').find('img')
        lost_char3 = 'http:'+lost_char2['src'] #캐릭터 이미지

        embed.set_author(name = lost_base3.text.strip())
        embed.add_field(name='플레이어 정보',value='서버 : '+lost_info2[1].text.strip()+'\n길드 : '+lost_info3[1].text.strip()+'\n클래스 : '+lost_info4[1].text.strip()+'\n칭호 : '+lost_info5[1].text.strip(), inline=True)
        embed.add_field(name='LV',value='아이템 : '+lost_lv1[1].text.strip()+'\n원정대 : '+lost_lv2[1].text.strip()+'\nPVP : '+lost_lv3[1].text.strip(), inline=True)
        embed.set_image(url = lost_char3)
        embed.set_footer(text='현재는 공홈에서 캐릭터 클래스 이미지만 제공중입니다.')
        await client.send_message(message.channel,embed = embed)


#메이플
    if message.content.startswith("!메이플"):
        print('메이플 명령어 실행')
        mp_nick = message.content.split(" ")
        mp_nick2 = urllib.parse.quote(mp_nick[1])
        mp_url = 'https://maple.gg/u/' + mp_nick2

        mp_th = 'https://blogfiles.pstatic.net/MjAxODExMDdfMTk4/MDAxNTQxNTcyMTQyMDY1.G82N0CYAhk2lwWeGPpR0g8WPLexxWMtifwFzqAqOf0Qg.xAMFcAkPG7nxv5vMJVtGI_2QngD2-to2TzFmdvrB09cg.PNG.ig6268/%EB%A9%94%EC%9D%B4%ED%94%8C.png'

        mp_link1 = 'https://maplestory.nexon.com/'
        mp_link2 = 'http://maple.inven.co.kr/'
        mp_link3 = 'https://cafe.naver.com/heart910'

        mp_all_link = "[공홈]("+mp_link1+") | [메이플인벤]("+mp_link2+") | [메공카]("+mp_link3+") | [메이플지지]("+mp_url+")"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
        }

        mTemp = requests.get(mp_url, timeout=60, headers=headers)
        msoup = BeautifulSoup(mTemp.text, 'html.parser')


        mp_pro = msoup.find('div',{'class':'user-profile'}).find('section').find('div',{'class':'row'})
        mp_img = mp_pro.find('div',{'class':'col-lg-2'}).find('img') #캐릭 이미지
        mp_info = mp_pro.find('div',{'class':'col-lg-10'})
        #print(mp_img['src'])
        mp_sv_img = mp_info.find('div',{'class':'mb-1'}).find('img') #서버 서버이미지
        mp_sv = mp_info.find('div',{'class':'mb-1'}).find('span')#서버 이름
        mp_info1 = mp_info.find('div',{'class':'user-summary'}).find('ul').find_all('li') #[0]렙 [1]직업 [2]인기도
        mp_info2 = mp_info.find('div',{'class':'row user-additional'}).find_all('div')#1길드 2종합 3월드 4직업 5전제직업
        #mp_info3 = mp_info2[0].find('a')#길드명
        mp_info3 = mp_info2[0].text.strip().split('\n')
        mp_info4 = mp_info2[1].find('span')#종합랭킹
        mp_info5 = mp_info2[2].find('span')#월드랭킹
        mp_info6 = mp_info2[3].find('span')#직업랭킹

        embed = discord.Embed(title='', colour=discord.Colour.orange())
        embed.set_author(name=mp_sv.text.strip()+'서버 ⭐'+mp_nick[1]+'님',icon_url=mp_sv_img['src'], url=mp_url)
        embed.add_field(name='링크', value = mp_all_link, inline=False)
        embed.add_field(name='정보', value =  mp_info1[0].text.strip()+'\n'+ mp_info1[1].text.strip()+'\n'+mp_info1[2].text.strip()+'\n길드 : '+mp_info3[1], inline=True)
        embed.add_field(name='랭킹', value = '종합 : '+mp_info4.text.strip()+'\n월드 : '+mp_info5.text.strip()+'\n직업(월드) : '+mp_info6.text.strip(), inline=True)
        embed.set_image(url=mp_img['src'])
        embed.set_thumbnail(url=mp_th)

        #무릉 + 유니온 기록
        mp_list = msoup.find('div',{'class':'card border-bottom-0'}).find('div',{'class':'bg-light'}).find('section').find('div')
        mp_list1 = mp_list.find_all('div',{'class':'col-lg-3'}) #0무릉 2유니온

        #무릉
        mp_sp = mp_list1[0].find('section')
        if(mp_sp.find('div',{'class':'user-summary-box-content text-center'}) in mp_sp):
            mp_sp1 = mp_sp.find('div').find('div').find('div') #h1층수 small시간
            mp_spt = mp_sp.find('footer').find_all('div')
            mp_spt1 = mp_spt[2].find('span')#기준일

            embed.add_field(name='무릉도장', value = '최고기록 : '+mp_sp1.h1.text.strip()+' ('+mp_sp1.small.text.strip()+')\n'+mp_spt1.text.strip(), inline=True)
        else:
            embed.add_field(name='무릉도장', value = '무릉도장 기록이 없습니다.', inline=True)

        #유니온
        mp_un = mp_list1[2].find('section')
        if(mp_un.find('div',{'class':'user-summary-box-content text-center'}) in mp_un):
            mp_un1 = mp_un.find('div').find('div') #div 등급 , span 유니온렙

            embed.add_field(name='유니온', value = mp_un1.div.text.strip()+' ('+mp_un1.span.text.strip()+')', inline=True)
        else:
            embed.add_field(name='유니온', value = '유니온 기록이 없습니다.', inline=True)

        await client.send_message(message.channel, embed=embed)

    #else:
        #embed = discord.Embed(title='', colour=discord.Colour.orange())
        #embed.add_field(name='링크', value = mp_all_link+'\n검색결과가 없습니다.\n 캐릭터 이름을 확인해주세요', inline=False)

        #await client.send_message(message.channel, embed=embed)

    #-------------------------------------------------------------------------------------------------------------------------------------------------
    # $$$$$$\                                                          $$\               $$\
    #$$  __$$\                                                         $$ |              $$ |
    #$$ /  $$ |$$\    $$\  $$$$$$\   $$$$$$\  $$\  $$\  $$\  $$$$$$\ $$$$$$\    $$$$$$$\ $$$$$$$\
    #$$ |  $$ |\$$\  $$  |$$  __$$\ $$  __$$\ $$ | $$ | $$ | \____$$\\_$$  _|  $$  _____|$$  __$$\
    #$$ |  $$ | \$$\$$  / $$$$$$$$ |$$ |  \__|$$ | $$ | $$ | $$$$$$$ | $$ |    $$ /      $$ |  $$ |
    #$$ |  $$ |  \$$$  /  $$   ____|$$ |      $$ | $$ | $$ |$$  __$$ | $$ |$$\ $$ |      $$ |  $$ |
    # $$$$$$  |   \$  /   \$$$$$$$\ $$ |      \$$$$$\$$$$  |\$$$$$$$ | \$$$$  |\$$$$$$$\ $$ |  $$ |
    # \______/     \_/     \_______|\__|       \_____\____/  \_______|  \____/  \_______|\__|  \__|

    #오버워치 전적검색
    if message.content.startswith('!오버워치'):
        temp = message.content.split(" ")

        changeNameURLEncode = urllib.parse.quote(temp[1])

        mURL = 'https://overwatch.op.gg/search/?playerName=' + changeNameURLEncode
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
            'Referer': 'https://overwatch.op.gg/',
            'accept-language': 'ko-KR'
        }

        mTemp = requests.get(mURL, timeout=60, allow_redirects=False, headers=headers)
        mheader = mTemp.headers
        msoup = BeautifulSoup(mTemp.text, 'html.parser')

        #print(mheader['Location'])

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
            'accept-language': 'ko-KR'
        }

        ov_link = 'https://playoverwatch.com/ko-kr/'
        ov_link2 = 'http://overwatch.inven.co.kr/'
        ov_link3 = 'https://playoverwatch.com/ko-kr/news/patch-notes/pc/'
        ov_all_link = "[OP.GG]("+mURL+") | [공홈]("+ov_link+") | [인벤]("+ov_link2+") | [패치노트]("+ov_link3+")"

        embed = discord.Embed(title='', color=0x1DDB16)
        embed.add_field(name='링크', value= ov_all_link, inline=False)

        mTemp = requests.get(mURL, timeout=60, headers=headers)
        msoup = BeautifulSoup(mTemp.text, 'html.parser')

        #아이디가 없을 때
        #if(msoup.find('div', {'class':'1-container'}).find('div', {'id':'PlayerLayout'}) in msoup):
        mURL = mheader['Location']
        temp2 = msoup.select('#PlayerLayoutHeader > div > div.PlayerInfo')
        temp3 = msoup.select('#PlayerLayoutHeader > div > div.ProfileImage')
        temp4 = msoup.select('#PlayerLayoutContent > div')

        ProfileImage = temp3[0].img['src']
        PlayerLevel = temp2[0].find('div', {'class':'Level'})
        ov_update = temp2[0].find('div', {'class':'LastUpdated'}).find('b')

        RatingTemp = temp4[0].find('div', {'class':'SkillRating'})
        StatsTemp = temp4[0].find('div', {'class':'PlayerSummaryStats'}).find_all('div')
        #print(RatingTemp)#랭킹 출력이안됨
        #if(StatsTemp[0].em in StatsTemp): #경쟁전 정보있을때
        StatsTemp1 = StatsTemp[0].find('span')
        RatingTemp1 = str(RatingTemp.h2.text).split('\n')
        StatsTemp2 = str(StatsTemp[0].em.text).split('\n') #[1]승 [3]패

        ov_kd = StatsTemp[1].span.text.strip().split(':')#kd율
        ov_kd1 = StatsTemp[1].em.text.strip().split('\n')# k / d

        embed.set_author(name = temp[1]+' 님의 전적검색\n(최근갱신 : '+ov_update.text.strip()+')',icon_url=ProfileImage)
        embed.set_thumbnail(url=RatingTemp.img['src'])
        embed.add_field(name='플레이어 정보',value=str(PlayerLevel.text)+' | '+RatingTemp1[1]+' | '+ RatingTemp1[2]
        +'\n경쟁전 : '+StatsTemp2[1]+' '+StatsTemp2[3]+' (승률 : '+StatsTemp1.text.strip() +') | K/D : '+ov_kd[0], inline=True)
        #embed.add_field(name='전적',value=StatsTemp2[1]+' '+StatsTemp2[3]+' (승률 : '+StatsTemp1.text.strip() +')\nK/D : '+ov_kd[0], inline=True)

        ov_base = msoup.find('div',{'id':'PlayerLayoutContent'}).find('div').find('div',{'class':'MainContent'})
        ov_most = ov_base.find('div',{'class':'ChampionStatsTable'}).find('table').find('tbody').find_all('tr')

        ov_aa1 = ov_most[0].find_all('td') # 0영웅 1승 2패 3승률 4kd비율
        ov_aa2 = ov_aa1[4].b.text.strip().split(':')
        ov_bb1 = ov_most[1].find_all('td') # 0영웅 1승 2패 3승률 4kd비율
        ov_bb2 = ov_bb1[4].b.text.strip().split(':')
        ov_cc1 = ov_most[2].find_all('td') # 0영웅 1승 2패 3승률 4kd비율
        ov_cc2 = ov_cc1[4].b.text.strip().split(':')
        ov_dd1 = ov_most[3].find_all('td') # 0영웅 1승 2패 3승률 4kd비율
        ov_dd2 = ov_dd1[4].b.text.strip().split(':')
        ov_ee1 = ov_most[4].find_all('td') # 0영웅 1승 2패 3승률 4kd비율
        ov_ee2 = ov_ee1[4].b.text.strip().split(':')

        embed.add_field(name='Most 영웅',
            value='1.'+ov_aa1[0].text.strip()+'(승 : '+ov_aa1[3].text.strip()+') | '
            +'K/D : '+ov_aa2[0] +' | 폭주 : '+ov_aa1[6].text.strip()+' | Time : '+ov_aa1[7].text.strip()
            +'\n2.'+ov_bb1[0].text.strip()+'(승 : '+ov_bb1[3].text.strip()+') | '
            +'K/D : '+ov_bb2[0] +' | 폭주 : '+ov_bb1[6].text.strip()+' | Time : '+ov_bb1[7].text.strip()
            +'\n3.'+ov_cc1[0].text.strip()+'(승 : '+ov_cc1[3].text.strip()+') | '
            +'K/D : '+ov_cc2[0] +' | 폭주 : '+ov_cc1[6].text.strip()+' | Time : '+ov_cc1[7].text.strip()
            +'\n4.'+ov_dd1[0].text.strip()+'(승 : '+ov_dd1[3].text.strip()+') | '
            +'K/D : '+ov_dd2[0] +' | 폭주 : '+ov_dd1[6].text.strip()+' | Time : '+ov_dd1[7].text.strip()
            +'\n5.'+ov_ee1[0].text.strip()+'(승 : '+ov_ee1[3].text.strip()+') | '
            +'K/D : '+ov_ee2[0] +' | 폭주 : '+ov_ee1[6].text.strip()+' | Time : '+ov_ee1[7].text.strip(),inline=False)

        await client.send_message(message.channel, embed=embed)
        #else:
        #    embed.set_author(name = temp[1]+' 님의 전적검색\n(최근갱신 : '+ov_update.text.strip()+')',icon_url=ProfileImage)
        #    #embed.set_thumbnail(url=RatingTemp.img['src'])
        #    embed.add_field(name='플레이어 정보',value=str(PlayerLevel.text)+'\n 경쟁전 정보가 없습니다.\n빠른대전은 제공하지 않습니다. 죄송합니다.', inline=True)
        #    await client.send_message(message.channel, embed=embed)
    #    else:
    #        embed.set_author(name = temp[1]+'님의 전적검색')
    #        embed.add_field(name='플레이어 정보',value='플레이어 정보가 존재하지않습니다.\n닉네임 또는 배틀태그를 확인해주세요\nEX) !오버워치 닉네임#배틀태그', inline=True)
    #        await client.send_message(message.channel, embed=embed)

    #-------------------------------------------------------------------------------------------------------------------------------------------------
    #$$\       $$$$$$\  $$\
    #$$ |     $$  __$$\ $$ |
    #$$ |     $$ /  $$ |$$ |
    #$$ |     $$ |  $$ |$$ |
    #$$ |     $$ |  $$ |$$ |
    #$$ |     $$ |  $$ |$$ |
    #$$$$$$$$\ $$$$$$  |$$$$$$$$\
    #\________|\______/ \________|

    if message.content.startswith('!lol'):
        print('롤 명령어 실행')
        lol_name = message.content.split(" ")
        lol_name2 = urllib.parse.quote(lol_name[1])

        mURL = 'http://www.op.gg/summoner/userName=' + lol_name2
        fow_url = 'http://fow.kr/find/'+lol_name2
        lol_url = 'http://www.leagueoflegends.co.kr/'
        lol_inv_url = 'http://lol.inven.co.kr/'
        lol_url2='http://lol.inven.co.kr/dataninfo/champion/manualTool.php'

        lol_all_link = "[OP.GG]("+mURL+") | [FOW]("+fow_url+")"
        lol_all_link2 = "[롤 홈피]("+lol_url+") | [롤 인벤]("+lol_inv_url+") | [챔프 공략]("+lol_url2+")"

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
            'Referer':'http://www.op.gg/',
            'accept-language':'ko-KR'
        }

        mTemp = requests.get(mURL, timeout=60, headers=headers)
        msoup = BeautifulSoup(mTemp.text, 'html.parser')

        #레벨 및 정보
        lol_info = msoup.find('div',{'class':'Header'}) #레벨, 전시즌티어, 래대확인
        #lol_info1 = lol_info.find('ul',{'class':'PastRankList'}).find_all('li')#전시즌 티어 현재사용x

        #롤 닉네임이 존재하지 않을때 else
        if(lol_info.find('div',{'class':'Face'}) in lol_info):
            lol_lv = msoup.find('div',{'class':'Face'}).find('span')#레벨
            lol_img = lol_info.find('div',{'class':'Face'}).find('div',{'class':'ProfileIcon'}).find('img')#소환사이미지
            lol_img1 = 'http:'+lol_img['src']

            lol_info2 = lol_info.find('div',{'class':'Profile'}).find('div',{'class':'Information'}).find('div',{'class':'Rank'})

            #print(lol_img1)
            #print(lol_lv)

            #print(lol_pro)

            lol_side = msoup.find('div',{'class':'SideContent'}) #솔랭 + 자유 + 모스트챔 박스
            lol_tier = lol_side.find('div',{'class':'TierBox Box'}) #솔랭 +자유 박스

            embed = discord.Embed(title='', colour=discord.Colour.green())
            embed.set_author(name = lol_name[1],icon_url=lol_img1, url = mURL)
            embed.add_field(name='링크', value = lol_all_link+' | '+lol_all_link2,inline=False)

            #레더정보가 존재할 때
            if(lol_info2.find('div',{'class':'LadderRank'}) in lol_info2):
                lol_info3 = lol_info2.find('div',{'class':'LadderRank'})
                lol_pro = lol_info3.find('a')#래더랭킹
                embed.add_field(name='레벨', value = lol_lv.text.strip()+' ( '+lol_pro.text.strip()+' )\n',inline=False)
            else:
                embed.add_field(name='레벨', value = lol_lv.text.strip(),inline = False)

            #------------------------------------------솔랭--------------------------------------------------------------#
            lol_solo = lol_tier.find('div',{'class':'SummonerRatingMedium'}) #솔랭 박스
            lol_solo_img = lol_solo.find('div',{'class':'Medal'}).find('img')#티어 이미지
            lol_solo_img1 = 'http:' + lol_solo_img['src']#티어 이미지
            lol_solo1 = lol_solo.find('div',{'class':'TierRankInfo'})

            embed.set_thumbnail(url=lol_solo_img1)

            #솔랭 티어가 존재할 때
            if(lol_solo1.find('div',{'class':'TierInfo'}) in lol_solo1):
                lol_solo2 = lol_solo1.find('div',{'class':'TierRank'})# 티어
                lol_solo3 = lol_solo1.find('div',{'class':'TierInfo'})
                lol_solo_lp = lol_solo3.find('span')# LP
                lol_solo5 = lol_solo3.find('span',{'class':'WinLose'}).find_all('span')#승패 [0]승 [1]패 [2]승률

                embed.add_field(name='솔로 랭크', value = '티어 : '+lol_solo2.text.strip()+' ( '+lol_solo_lp.text.strip()+' )\n'
                    +lol_solo5[0].text.strip()+' '+lol_solo5[1].text.strip()+' ('+lol_solo5[2].text.strip()+')',inline=True)

            else:
                embed.add_field(name='솔로 랭크', value = '솔랭 기록이 없습니다.',inline=True)
            #------------------------------------------자유랭-------------------------------------------------------------#

            #자랭 티어가 존재할 때
            if(lol_tier.find('div',{'class':'SummonerRatingLine'}) in lol_tier):
                    lol_free = lol_tier.find('div',{'class':'SummonerRatingLine'}) #자유랭 박스

                    #솔랭은 있는데 자랭은 기록이 없을 때
                    if(lol_free.find('div',{'class':'WinLose'}) in lol_free):
                        #lol_free_img = lol_free.find('div',{'class':'Medal'}).find('span') #자유랭 티어 이미지 현재사용x
                        lol_free1 = lol_free.find('div',{'class':'TierRank'}).find_all('div') # [0]자유랭 티어, [1]점수
                        lol_free2 = lol_free.find('div',{'class':'WinLose'}).find_all('span') # [0]승 [1]패 [2]승률

                        embed.add_field(name='자유 랭크', value = '티어 : '+lol_free1[0].text.strip()+' ( '+lol_free1[1].text.strip()+' )\n'
                            +lol_free2[0].text.strip()+' '+lol_free2[1].text.strip()+' ('+lol_free2[2].text.strip()+')',inline=True)
                    else:
                        embed.add_field(name='자유 랭크', value = '자랭 기록이 없습니다.',inline=True)
            else:
                embed.add_field(name='자유 랭크', value = '자랭 기록이 없습니다.',inline=True)

            #모스트
            if(lol_side.find('div',{'class':'Box tabWrap stats-box'}) in lol_side):
                lol_most = lol_side.find('div',{'class':'Box tabWrap stats-box'})
                lol_most1 = lol_most.find('div',{'class':'Content tabItems'}).find('div',{'class':'MostChampionContent tabItem overview-stats--all'})
                lol_most2 = lol_most1.find('div',{'class':'MostChampionContent'}).find_all('div',{'class':'ChampionBox Ranked'})

                lol_ach1 = lol_most2[0].find('div',{'class':'ChampionInfo'}).find('div',{'class':'ChampionName'}).find('a')#모스트챔프 이름
                lol_ach2 = lol_most2[0].find('div',{'class':'PersonalKDA'}).find('div').find('span')#KDA
                lol_ach3 = lol_most2[0].find('div',{'class':'PersonalKDA'}).find('div',{'class':'KDAEach'}).find_all('span') # [0]킬 [2]데스 [4]어시
                lol_ach4 = lol_most2[0].find('div',{'class':'Played'}).find_all('div')# [0]승률 [1]게임수
                lol_ach5 = lol_ach2.text.strip().split(':')

                lol_bch1 = lol_most2[1].find('div',{'class':'ChampionInfo'}).find('div',{'class':'ChampionName'}).find('a')#모스트챔프 이름
                lol_bch2 = lol_most2[1].find('div',{'class':'PersonalKDA'}).find('div').find('span')#KDA
                lol_bch3 = lol_most2[1].find('div',{'class':'PersonalKDA'}).find('div',{'class':'KDAEach'}).find_all('span') # [0]킬 [2]데스 [4]어시
                lol_bch4 = lol_most2[1].find('div',{'class':'Played'}).find_all('div')# [0]승률 [1]게임수
                lol_bch5 = lol_bch2.text.strip().split(':')

                #lol_cch1 = lol_most2[2].find('div',{'class':'ChampionInfo'}).find('div',{'class':'ChampionName'}).find('a')#모스트챔프 이름
                #lol_cch2 = lol_most2[2].find('div',{'class':'PersonalKDA'}).find('div').find('span')#KDA
                #lol_cch3 = lol_most2[2].find('div',{'class':'PersonalKDA'}).find('div',{'class':'KDAEach'}).find_all('span') # [0]킬 [2]데스 [4]어시
                #lol_cch4 = lol_most2[2].find('div',{'class':'Played'}).find_all('div')# [0]승률 [1]게임수
                #lol_cch5 = lol_cch2.text.strip().split(':')

                #lol_dch1 = lol_most2[3].find('div',{'class':'ChampionInfo'}).find('div',{'class':'ChampionName'}).find('a')#모스트챔프 이름
                #lol_dch2 = lol_most2[3].find('div',{'class':'PersonalKDA'}).find('div').find('span')#KDA
                #lol_dch3 = lol_most2[3].find('div',{'class':'PersonalKDA'}).find('div',{'class':'KDAEach'}).find_all('span') # [0]킬 [2]데스 [4]어시
                #lol_dch4 = lol_most2[3].find('div',{'class':'Played'}).find_all('div')# [0]승률 [1]게임수
                #lol_dch5 = lol_dch2.text.strip().split(':')

                #lol_ech1 = lol_most2[4].find('div',{'class':'ChampionInfo'}).find('div',{'class':'ChampionName'}).find('a')#모스트챔프 이름
                #lol_ech2 = lol_most2[4].find('div',{'class':'PersonalKDA'}).find('div').find('span')#KDA
                #lol_ech3 = lol_most2[4].find('div',{'class':'PersonalKDA'}).find('div',{'class':'KDAEach'}).find_all('span') # [0]킬 [2]데스 [4]어시
                #lol_ech4 = lol_most2[4].find('div',{'class':'Played'}).find_all('div')# [0]승률 [1]게임수
                #lol_ech5 = lol_ech2.text.strip().split(':')

                embed.add_field(name="모스트 챔프",
                value = lol_ach1.text.strip()+'('+lol_ach4[1].text.strip()+' : '+lol_ach4[0].text.strip()+') '+'- | - KDA : '
                        + lol_ach5[0] +' ('+lol_ach3[0].text.strip()+'/'+lol_ach3[2].text.strip()+'/'+lol_ach3[4].text.strip()+')\n'

                        + lol_bch1.text.strip()+'('+lol_bch4[1].text.strip()+' : '+lol_bch4[0].text.strip()+') '+'- | - KDA : '
                        + lol_bch5[0] +' ('+lol_bch3[0].text.strip()+'/'+lol_bch3[2].text.strip()+'/'+lol_bch3[4].text.strip()+')\n',inline=False)

                        #+ lol_cch1.text.strip()+'(승률 : '+lol_cch4[0].text.strip()+') '+'- | - KDA : '
                        #+ lol_cch5[0] +' ('+lol_cch3[0].text.strip()+'/'+lol_cch3[2].text.strip()+'/'+lol_cch3[4].text.strip()+')\n'

                        #+ lol_dch1.text.strip()+'(승률 : '+lol_dch4[0].text.strip()+') '+'- | - KDA : '
                        #+ lol_dch5[0] +' ('+lol_dch3[0].text.strip()+'/'+lol_dch3[2].text.strip()+'/'+lol_dch3[4].text.strip()+')\n'

                        #+ lol_ech1.text.strip()+'(승률 : '+lol_ech4[0].text.strip()+') '+'- | - KDA : '
                        #+ lol_ech5[0] +' ('+lol_ech3[0].text.strip()+'/'+lol_ech3[2].text.strip()+'/'+lol_ech3[4].text.strip()+')\n',inline=False)

            else:
                embed.add_field(name="모스트 챔프", value = '랭크 기록이 없습니다.')


            await client.send_message(message.channel, embed=embed)

        else: #닉네임이 존재하지 않을 때
            embed = discord.Embed(title='', colour=discord.Colour.green())
            embed.add_field(name='링크', value = lol_all_link+' | '+lol_all_link2+'\n등록되지 않은 소환사입니다.\n소환사명을 확인해주세요',inline=False)

            await client.send_message(message.channel, embed=embed)

#라인별 인기 챔프
    if message.content.startswith('!인기챔프'):
        print('인기챔프 명령어 실행')

        fow_link = "http://fow.kr/champs/"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
            'Referer': 'http://www.fow.kr/',
            'accept-language': 'ko-KR'
        }

        win_req = requests.get(fow_link, timeout=60, headers=headers)
        soup = BeautifulSoup(win_req.text, 'html.parser')

        #승률순위 정보
        rank = soup.find('div',{'style':'position:relative; width:850px; margin:0 auto;'})
        rank2 = rank.find('div',{'style':'position:relative; width:850px; margin:0 auto 0 0;'})
        rank3 = rank2.find('div',{'style':'background-color:#eeeeee; border:1px solid #dddddd; color:#333333; border-radius: 4px; padding:10px 10px 8px 10px;'})
        rank4 = rank3.find('div',{'style':'position:relative; height:auto;'})
        rank5 = rank4.find('div',{'class':'champ_list'}).find_all('a')

        #http://opgg-static.akamaized.net/images/logo
        # lol_logo = lol_tier.find('div', {'class': 'header'})
        # lol_logo_img = lol_solo.find('ul', {'class': 'sites'}).find('img')
        # lol_logo_img = 'http:' + lol_logo_img['src']

        info_link = "[웹사이트 바로가기]("+fow_link+")"
        embed = discord.Embed(title='', url=fow_link, colour=discord.Colour.green())
        # embed.set_author(name='', icon_url=lol_logo_img, url=fow_link)

        embed.add_field(name='챔피언 인기 순위\n링크', value=info_link, inline=False)
        embed.add_field(name='- Top Champion Pop Ranking', value=
        '1위. ' + rank5[0].text.strip()+'\n'+
        '2위. ' + rank5[1].text.strip()+'\n'+
        '3위. ' + rank5[2].text.strip()+'\n'+
        '4위. ' + rank5[3].text.strip()+'\n'+
        '5위. ' + rank5[4].text.strip(), inline=True)
        embed.add_field(name='- Mid Champion Pop Ranking', value=
        '1위. ' + rank5[10].text.strip() + '\n' +
        '2위. ' + rank5[11].text.strip() + '\n' +
        '3위. ' + rank5[12].text.strip() + '\n' +
        '4위. ' + rank5[13].text.strip() + '\n' +
        '5위. ' + rank5[14].text.strip(), inline=True)
        embed.add_field(name='- Bottom Champion Pop Ranking', value=
        '1위. ' + rank5[15].text.strip() + '\n' +
        '2위. ' + rank5[16].text.strip() + '\n' +
        '3위. ' + rank5[17].text.strip() + '\n' +
        '4위. ' + rank5[18].text.strip() + '\n' +
        '5위. ' + rank5[19].text.strip(), inline=True)
        embed.add_field(name='- Jungle Champion Pop Ranking', value=
        '1위. ' + rank5[5].text.strip() + '\n' +
        '2위. ' + rank5[6].text.strip() + '\n' +
        '3위. ' + rank5[7].text.strip() + '\n' +
        '4위. ' + rank5[8].text.strip() + '\n' +
        '5위. ' + rank5[9].text.strip(), inline=True)
        embed.add_field(name='- Support Champion Pop Ranking', value=
        '1위. ' + rank5[20].text.strip() + '\n' +
        '2위. ' + rank5[21].text.strip() + '\n' +
        '3위. ' + rank5[22].text.strip() + '\n' +
        '4위. ' + rank5[23].text.strip() + '\n' +
        '5위. ' + rank5[24].text.strip(), inline=True)

        await client.send_message(message.channel, embed=embed)

    #-------------------------------------------------------------------------------------------------------------------------------------------------
    #$$$$$$$\  $$\   $$\ $$$$$$$\   $$$$$$\
    #$$  __$$\ $$ |  $$ |$$  __$$\ $$  __$$\
    #$$ |  $$ |$$ |  $$ |$$ |  $$ |$$ /  \__|
    #$$$$$$$  |$$ |  $$ |$$$$$$$\ |$$ |$$$$\
    #$$  ____/ $$ |  $$ |$$  __$$\ $$ |\_$$ |
    #$$ |      $$ |  $$ |$$ |  $$ |$$ |  $$ |
    #$$ |      \$$$$$$  |$$$$$$$  |\$$$$$$  |
    #\__|       \______/ \_______/  \______/

    #배틀그라운드 맵(지도) 조회
    if message.content.startswith("!배그지도"):
        pbm = message.content.split(" ")

        if pbm[1] == '에란겔':
            embed = discord.Embed(title='에란겔 erangel (자세히보기 Click!)', url = 'http://pubg.inven.co.kr/dataninfo/map/erangel/', colour=discord.Colour.green())
            embed.set_image(url='https://postfiles.pstatic.net/MjAxODEwMjZfMTMz/MDAxNTQwNDgzNTE4Njky.XUYgyEfCKCXPwkap2GSQKYinBO8YpCQ4OHtrvnm9gHkg.hgdBzNy8hfyoQvMosY-V_9lxkRcmsgyQ3nmHeJCTybwg.PNG.ig6268/%EC%97%90%EB%9E%80%EA%B2%94.PNG?type=w773')
            await client.send_message(message.channel, embed=embed)

        if pbm[1] == '미라마':
            embed = discord.Embed(title='미라마 miramar (자세히보기 Click!)', url = 'http://pubg.inven.co.kr/dataninfo/map/miramar/', colour=discord.Colour.green())
            embed.set_image(url='https://postfiles.pstatic.net/MjAxODEwMjZfMjQ5/MDAxNTQwNDgzNTIwMDQy.tZ9sKNbPcZa44sPk5-w3uAP29vxA51M_QjNRlPi53jQg.a9_0330UiZjIKQ3Ci_LWFqSWheU-LtoY16bXiJkxW-cg.PNG.ig6268/%EB%AF%B8%EB%9D%BC%EB%A7%88.PNG?type=w773')
            await client.send_message(message.channel, embed=embed)

        if pbm[1] == '사녹':
            embed = discord.Embed(title='사녹 sanhok (자세히보기 Click!)', url = 'http://pubg.inven.co.kr/dataninfo/map/sanhok/', colour=discord.Colour.green())
            embed.set_image(url='https://postfiles.pstatic.net/MjAxODEwMjZfMTc4/MDAxNTQwNDgzNTIxNTc3.5pJ2-g0KvcM26wAXVW6c87qDRxwOe8PH-N9fXnP5DD0g.RxdJVIB6Smby2E3HxPI7Lt3Rtk_Q8hTPv4B9UmHFl3gg.PNG.ig6268/%EC%82%AC%EB%85%B9.PNG?type=w773')
            await client.send_message(message.channel, embed=embed)

    #배틀그라운드 전적검색 (간략히)
    if message.content.startswith('!배그'):
        print('배그 명령어 실행')
        temp = message.content.split(" ")

        mURL = 'https://pubg.op.gg/user/' + temp[1]
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
        }

        mTemp = requests.get(mURL, timeout=60, headers=headers)
        msoup = BeautifulSoup(mTemp.text, 'html.parser')

        #rankedStatsWrap > div.ranked-stats-wrapper__list
        #닉네임 없을 때
        #if(msoup.find('div', {'id':'userNickname'}) in msoup):
        temp2 = msoup.find('div', {'id':'userNickname'})
        #if(temp2.attrs['data-user_id'] != " "):
        temp3 = temp2.attrs['data-user_id']

##############광고부분##################
        #ad_url = 'https://naver.com'
        #embed = discord.Embed(title='', colour = 0xfdfd00)
        #embed.set_image(url= 'https://s0.2mdn.net/8391437/AZR_FreeAcctDeveloperOpenSourceCh2_KOR_728x90_BAN_Direct_KO_Trial_Standard_SBAN_TN_T2_1.png')
        #embed.set_footer(text='[ 광고 ] 어떤 오픈소스 언어로도 코딩한다! Azure 체험해보세요!', icon_url='https://image.ibb.co/ksbTcf/adlogo-89215.png')
        #await client.send_message(message.channel, embed=embed)

        #https://pubg.op.gg/api/users/59fdc8c6370520000172fab6/ranked-stats?season=pc-2018-01&queue_size=1&mode=tpp
        soloTemp = 'https://pubg.op.gg/api/users/' + temp3 + '/ranked-stats?season=pc-2018-01&queue_size=1&mode=tpp'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
        }

        mTemp = requests.get(soloTemp, timeout=60, headers=headers)
        msoup = BeautifulSoup(mTemp.text, 'html.parser')

        pb_link1 = 'https://cafe.naver.com/playbattlegrounds'
        pb_link2 = 'http://pubg.game.daum.net/pubg/index.daum'
        pb_link3 = 'https://pubg.op.gg/'
        pb_link4 = 'https://dak.gg'

        pb_all_link = "[OP.GG에서 보기]("+mURL+") | [공식카페]("+pb_link1+") | [카카오배그]("+pb_link2+") | [닥지지]("+pb_link4+")"
        embed = discord.Embed(title='', colour = 0xfdfd00)
        embed.set_author(name = temp[1]+'님 전적검색',icon_url='http://static.inven.co.kr/image_2011/site_image/battlegrounds/dataninfo/itemimage/4013.png', url = mURL)
        embed.add_field(name='링크', value = pb_all_link, inline=False)
        #embed.set_footer(text='값싼 광고비로 봇의 개발자를 도와주세요. 광고문의 : @카카오톡', icon_url='https://i.imgur.com/wSTFkRM.png')

        #솔로
        solo = json.loads(mTemp.text)
        #print(solo)
        if not('message' in solo):
            solo_tier = solo['tier']['title']
            solo_imageurl = solo['tier']['image_url']

            solo_win_matches_cnt = solo['stats']['win_matches_cnt']
            solo_kills_sum = solo['stats']['kills_sum']
            solo_deaths_sum = solo['stats']['deaths_sum']
            solo_damage_dealt_avg = round(solo['stats']['damage_dealt_avg'])
            solo_rating = solo['stats']['rating']
            solo_rank = solo['ranks']['rank_points']
            solo_max_rank = solo['max_ranks']['rank_points']

            if(solo_deaths_sum == 0):
                solo_kd = 'Perfect!'
            else:
                solo_kd = solo_kills_sum/solo_deaths_sum
                solo_kd = round(solo_kd,2)

            if(str(solo_rank) =='None'):
                embed.add_field(name='🏃‍ 솔로 ( '+str(solo_rank)+' 위 )',value= str(solo_tier)+'\n레이팅 : '+str(solo_rating) +'\n치킨 수 : '
                +str(solo_win_matches_cnt)+'마리'+'\n평균딜 : '+str(solo_damage_dealt_avg)+ '\nK/D : '+str(solo_kd), inline=True)
            else:
                solo_rank_avg = solo_rank / solo_max_rank*100
                solo_rank_avg = round(solo_rank_avg,4)
                embed.add_field(name='🏃‍ 솔로 ( '+str(solo_rank)+' 위 )\n상위 '+str(solo_rank_avg)+'%',value= str(solo_tier)+'\n레이팅 : '+str(solo_rating) +'\n치킨 수 : '
                +str(solo_win_matches_cnt)+'마리'+'\n평균딜 : '+str(solo_damage_dealt_avg)+ '\nK/D : '+str(solo_kd), inline=True)

        else:
            embed.add_field(name='🏃‍ 솔로',value= '기록이 없습니다.\n 경기 후 확인해주세요', inline=True)

        #듀오
        DuoTemp = 'https://pubg.op.gg/api/users/' + temp3 + '/ranked-stats?season=pc-2018-01&queue_size=2&mode=tpp'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
        }

        mTemp = requests.get(DuoTemp, timeout=60, headers=headers)
        msoup = BeautifulSoup(mTemp.text, 'html.parser')

        Duo = json.loads(mTemp.text)

        if not('message' in Duo):
            Duo_tier = Duo['tier']['title']
            Duo_imageurl = Duo['tier']['image_url']

            Duo_win_matches_cnt = Duo['stats']['win_matches_cnt']
            Duo_kills_sum = Duo['stats']['kills_sum']
            Duo_deaths_sum = Duo['stats']['deaths_sum']
            Duo_damage_dealt_avg = round(Duo['stats']['damage_dealt_avg'])
            Duo_rating = Duo['stats']['rating']
            Duo_rank = Duo['ranks']['rank_points']
            Duo_max_rank = Duo['max_ranks']['rank_points']

            if(Duo_deaths_sum == 0):
                Duo_kd = 'Perfect!'
            else:
                Duo_kd = Duo_kills_sum/Duo_deaths_sum
                Duo_kd = round(Duo_kd,2)

            if(str(Duo_rank) =='None'):
                embed.add_field(name='👬 듀오 ( '+str(Duo_rank)+' 위 )',value= str(Duo_tier)+'\n레이팅 : '+str(Duo_rating) + '\n치킨 수 : '
                +str(Duo_win_matches_cnt)+'마리'+'\n평균딜 : '+str(Duo_damage_dealt_avg)+ '\nK/D : '+str(Duo_kd), inline=True)
            else:
                Duo_rank_avg = Duo_rank / Duo_max_rank*100
                Duo_rank_avg = round(Duo_rank_avg,4)
                embed.add_field(name='👬 듀오 ( '+str(Duo_rank)+' 위 )\n상위 '+str(Duo_rank_avg)+'%',value= str(Duo_tier)+'\n레이팅 : '+str(Duo_rating) + '\n치킨 수 : '
                +str(Duo_win_matches_cnt)+'마리'+'\n평균딜 : '+str(Duo_damage_dealt_avg)+ '\nK/D : '+str(Duo_kd), inline=True)

        else:
            embed.add_field(name='👬 듀오',value= '기록이 없습니다.\n 경기 후 확인해주세요', inline=True)
        #await client.send_message(message.channel, embed=embed)

        SquadTemp = 'https://pubg.op.gg/api/users/' + temp3 + '/ranked-stats?season=pc-2018-01&queue_size=4&mode=tpp'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
        }

        #스쿼드
        mTemp = requests.get(SquadTemp, timeout=60, headers=headers)
        msoup = BeautifulSoup(mTemp.text, 'html.parser')

        Squad = json.loads(mTemp.text)

        if not('message' in Squad):
            Squad_tier = Squad['tier']['title']
            Squad_imageurl = Squad['tier']['image_url']

            Squad_win_matches_cnt = Squad['stats']['win_matches_cnt']
            Squad_kills_sum = Squad['stats']['kills_sum']
            Squad_deaths_sum = Squad['stats']['deaths_sum']
            Squad_damage_dealt_avg = round(Squad['stats']['damage_dealt_avg'])
            Squad_rating = Squad['stats']['rating']
            Squad_rank = Squad['ranks']['rank_points']
            Squad_max_rank = Squad['max_ranks']['rank_points']

            if(Squad_deaths_sum == 0):
                Squad_kd = 'Perfect!'
            else:
                Squad_kd = Squad_kills_sum/Squad_deaths_sum
                Squad_kd = round(Squad_kd,2)

            if(str(Squad_rank) =='None'):
                embed.add_field(name='👨‍👨‍👧‍👧 스쿼드 ( '+str(Squad_rank)+' 위 ) ',value= str(Squad_tier)+'\n레이팅 : '+str(Squad_rating) + '\n치킨 수 : '
                +str(Squad_win_matches_cnt)+'마리'+'\n평균딜 : '+str(Squad_damage_dealt_avg)+ '\nK/D : '+str(Squad_kd), inline=True)
            else:
                Squad_rank_avg = Squad_rank / Squad_max_rank*100
                Squad_rank_avg = round(Squad_rank_avg,4)
                embed.add_field(name='👨‍👨‍👧‍👧 스쿼드 ( '+str(Squad_rank)+' 위 )\n상위 '+str(Squad_rank_avg)+'%',value= str(Squad_tier)+'\n레이팅 : '+str(Squad_rating) + '\n치킨 수 : '
                +str(Squad_win_matches_cnt)+'마리'+'\n평균딜 : '+str(Squad_damage_dealt_avg)+ '\nK/D : '+str(Squad_kd), inline=True)


        else:
            embed.add_field(name='👨‍👨‍👧‍👧 스쿼드',value= '기록이 없습니다.\n 경기 후 확인해주세요', inline=True)

        await client.send_message(message.channel, embed=embed)

        #elif(temp2.attrs['data-user_id'] == " "):
        #    embed = discord.Embed(title='', colour = 0xfdfd00)
        #    embed.add_field(name = '닉네임 정보가 없습니다.', value = '닉네임을 다시한번 확인해주세요')
        #    await client.send_message(message.channel, embed=embed)


    #배틀그라운드 DB 정보
    if message.content.startswith('!pubgdb'):
        temp = message.content.split(" ")

        map_db = {
                #HG(권총)
                'p18c': "1100", 'p1911': "1101", 'p92': "1102", 'r1895': '1103', 'r45': "1104",
                #SMG(기관단총)
                'uzi': "1800", 'tommy gun': "1801", 'ump9': "1802", 'vector': "1803",
                #AR(돌격소총)
                'akm': "1200", 'groza': "1201", 'm16': "1202", 'm4': "1203", 'scar': "1204", 'aug': "1205", 'qbz': "1206",
                'beryl': "1207", 'mk47': "1208",
                #DMR(지정사수 소총)
                'mk14': "1003", 'sks': "1004", 'vss': "1005", 'mini': "1006", 'slr': "1008", 'qbu': "1009",
                #SR(저격소총)
                'awm': "1000", 'kar98': "1001", 'm24': "1002", 'win94': "1007",
                #LMG(경기관총)
                'm249': "1300", 'dp': "1301",
                #SG(산탄총)
                's12k': "1600", 's1897': "1601", 's686': "1602", '소드오프': "1603",
                #BOW(활)
                '석궁': "1900",
                #Melee(근접)
                '빠루': "1700", '마체테': "1701", '프라이팬': "1702", '낫': "1703",
                #Throwables(투척)
                '수류탄': "1400", '화염병': "1401", '연막탄': "1402", '섬광탄': "1403",
                #소모품
                '아드레날린': "5000", '붕대': "5001", '에너지드링크': "5002", '구급상자': "5003", '연료통': "5004", '의료용키트': "5005", '진통제': "5006",
                #차량
                '버기': "6100", '다시아': "6101", '오토바이': "6102", '삼토바이': "6103", 'uaz': "6106", '버스': "6108",
                '트럭': "6110", '미라도': "6112", '로니': "6113", '스쿠터': "6114", '툭샤이': "6115", '보트': "6104",
                '아쿠아레일': "6107"
            }

        key = str(uuid4())
        dbitemnum = map_db[temp[1]]

        print(key)
        print(dbitemnum)

        mURL = 'http://pubg.inven.co.kr/dataninfo/item/detail.php?itemcode=' + dbitemnum
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
        }

        mTemp = requests.get(mURL, timeout=60, headers=headers)
        msoup = BeautifulSoup(mTemp.text, 'html.parser')

        #battlegroundsDb > div.battle.battle_box
        temp2 = msoup.select('#battlegroundsDb > div.battle.battle_box')
        temp3 = msoup.find('tbody')
        temp4 = temp3.find_all('th')
        temp5 = temp3.find_all('td')
        murl = temp2[0].img['src']
        temp4_count = len(temp4)

        embed = discord.Embed(title='배틀그라운드 검색하신 아이템정보 : ' + temp5[0].text, color=0xDD7311)
        embed.set_thumbnail(url=murl)

        a = 0;
        for item in temp4:
            embed.add_field(name=item.text,value=temp5[a].text, inline=True)
            a = a + 1;

        await client.send_message(message.channel, embed=embed)

        #embed.set_author(name="코하쿠봇 (KOHAKU BOT)")
        #embed.add_field(name=temp5[item], value=temp4[item], inline=True)
        #embed.add_field(name="서버 ID ", value=ctx.message.server.id, inline=True)
        #embed.add_field(name="존재하는 역할 ", value=len(ctx.message.server.roles), inline=True)
        #embed.add_field(name="멤버 수 ", value=len(ctx.message.server.members), inline=True)
        #embed.set_thumbnail(url=ctx.message.server.icon_url)

    #else: #위의 if에 해당되지 않는 경우
        #메시지를 보낸사람을 호출하며 말한 메시지 내용을 그대로 출력해줍니다.
        #await client.send_message(channel, "<@"+id+">님이 \""+message.content+"\"라고 말하였습니다.")

    #배틀그라운드 상세 전적조회
    if message.content.startswith('!배그전적'):
        temp = message.content.split(" ")

        mURL = 'https://pubg.op.gg/user/' + temp[1]
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
        }

        mTemp = requests.get(mURL, timeout=60, headers=headers)
        msoup = BeautifulSoup(mTemp.text, 'html.parser')

        #rankedStatsWrap > div.ranked-stats-wrapper__list
        temp2 = msoup.find('div', {'id':'userNickname'})
        temp3 = temp2.attrs['data-user_id']

        #https://pubg.op.gg/api/users/59fdc8c6370520000172fab6/ranked-stats?season=pc-2018-01&queue_size=1&mode=tpp
        soloTemp = 'https://pubg.op.gg/api/users/' + temp3 + '/ranked-stats?season=pc-2018-01&queue_size=1&mode=tpp'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
        }

        mTemp = requests.get(soloTemp, timeout=60, headers=headers)
        msoup = BeautifulSoup(mTemp.text, 'html.parser')

        solo = json.loads(mTemp.text)

        solo_tier = solo['tier']['title']
        solo_imageurl = solo['tier']['image_url']

        solo_matches_cnt = solo['stats']['matches_cnt']
        solo_win_matches_cnt = solo['stats']['win_matches_cnt']
        solo_topten_matches_cnt = solo['stats']['topten_matches_cnt']
        solo_kills_sum = solo['stats']['kills_sum']
        solo_kills_max = solo['stats']['kills_max']
        solo_assists_sum = solo['stats']['assists_sum']
        solo_headshot_kills_sum = solo['stats']['headshot_kills_sum']
        solo_deaths_sum = solo['stats']['deaths_sum']
        solo_longest_kill_max = solo['stats']['longest_kill_max']
        solo_rank_avg = round(solo['stats']['rank_avg'])
        solo_damage_dealt_avg = round(solo['stats']['damage_dealt_avg'])
        solo_time_survived_avg = solo['stats']['time_survived_avg']
        solo_rank_points = solo['stats']['rank_points']
        solo_rating = solo['stats']['rating']

        solo_rank = solo['ranks']['rank_points']

        embed = discord.Embed(title='[ 🔫 솔로 ] ' + temp[1], color=0x1DDB16)
        embed.set_thumbnail(url=solo_imageurl)
        embed.add_field(name='👑 타이틀',value=str(solo_tier), inline=True)
        embed.add_field(name='🏅 전체 순위',value=str(solo_rank) + ' 위', inline=True)
        embed.add_field(name='총 플레이 수',value=str(solo_matches_cnt) + ' 게임', inline=True)
        embed.add_field(name='승리한 경기 수',value=str(solo_win_matches_cnt) + ' 승리', inline=True)
        embed.add_field(name='Top 10 이내 경기 수',value=str(solo_topten_matches_cnt) + ' 진입', inline=True)
        embed.add_field(name='전체 플레이 Kill 수',value=str(solo_kills_sum) + ' 명', inline=True)
        embed.add_field(name='최다 킬',value=str(solo_kills_max) + ' 명', inline=True)
        embed.add_field(name='최다 어시스트',value=str(solo_assists_sum) + ' 번', inline=True)
        embed.add_field(name='헤드샷',value=str(solo_headshot_kills_sum) + ' 번', inline=True)
        embed.add_field(name='최대 거리 킬',value=str(solo_longest_kill_max) + ' M', inline=True)
        embed.add_field(name='평균 등수',value=str(solo_rank_avg) + ' 등', inline=True)
        embed.add_field(name='경기 당 데미지',value=str(solo_damage_dealt_avg), inline=True)
        embed.add_field(name='레이팅',value=str(solo_rating), inline=True)

        await client.send_message(message.channel, embed=embed)

        DuoTemp = 'https://pubg.op.gg/api/users/' + temp3 + '/ranked-stats?season=pc-2018-01&queue_size=2&mode=tpp'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
        }

        mTemp = requests.get(DuoTemp, timeout=60, headers=headers)
        msoup = BeautifulSoup(mTemp.text, 'html.parser')

        Duo = json.loads(mTemp.text)

        Duo_tier = Duo['tier']['title']
        Duo_imageurl = Duo['tier']['image_url']

        Duo_matches_cnt = Duo['stats']['matches_cnt']
        Duo_win_matches_cnt = Duo['stats']['win_matches_cnt']
        Duo_topten_matches_cnt = Duo['stats']['topten_matches_cnt']
        Duo_kills_sum = Duo['stats']['kills_sum']
        Duo_kills_max = Duo['stats']['kills_max']
        Duo_assists_sum = Duo['stats']['assists_sum']
        Duo_headshot_kills_sum = Duo['stats']['headshot_kills_sum']
        Duo_deaths_sum = Duo['stats']['deaths_sum']
        Duo_longest_kill_max = Duo['stats']['longest_kill_max']
        Duo_rank_avg = round(Duo['stats']['rank_avg'])
        Duo_damage_dealt_avg = round(Duo['stats']['damage_dealt_avg'])
        Duo_time_survived_avg = Duo['stats']['time_survived_avg']
        Duo_rank_points = Duo['stats']['rank_points']
        Duo_rating = Duo['stats']['rating']

        Duo_rank = Duo['ranks']['rank_points']

        embed = discord.Embed(title='[ 🔫🔫 듀오 ] ' + temp[1], color=0xFF5E00)
        embed.set_thumbnail(url=Duo_imageurl)
        embed.add_field(name='👑 타이틀',value=str(Duo_tier), inline=True)
        embed.add_field(name='🏅 전체 순위',value=str(Duo_rank) + ' 위', inline=True)
        embed.add_field(name='총 플레이 수',value=str(Duo_matches_cnt) + ' 게임', inline=True)
        embed.add_field(name='승리한 경기 수',value=str(Duo_win_matches_cnt) + ' 승리', inline=True)
        embed.add_field(name='Top 10 이내 경기 수',value=str(Duo_topten_matches_cnt) + ' 진입', inline=True)
        embed.add_field(name='전체 플레이 Kill 수',value=str(Duo_kills_sum) + ' 명', inline=True)
        embed.add_field(name='최다 킬',value=str(Duo_kills_max) + ' 명', inline=True)
        embed.add_field(name='최다 어시스트',value=str(Duo_assists_sum) + ' 번', inline=True)
        embed.add_field(name='헤드샷',value=str(Duo_headshot_kills_sum) + ' 번', inline=True)
        embed.add_field(name='최대 거리 킬',value=str(Duo_longest_kill_max) + ' M', inline=True)
        embed.add_field(name='평균 등수',value=str(Duo_rank_avg) + ' 등', inline=True)
        embed.add_field(name='경기 당 데미지',value=str(Duo_damage_dealt_avg), inline=True)
        embed.add_field(name='레이팅',value=str(Duo_rating), inline=True)

        await client.send_message(message.channel, embed=embed)

        SquadTemp = 'https://pubg.op.gg/api/users/' + temp3 + '/ranked-stats?season=pc-2018-01&queue_size=4&mode=tpp'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
        }

        mTemp = requests.get(SquadTemp, timeout=60, headers=headers)
        msoup = BeautifulSoup(mTemp.text, 'html.parser')

        Squad = json.loads(mTemp.text)

        Squad_tier = Squad['tier']['title']
        Squad_imageurl = Squad['tier']['image_url']

        Squad_matches_cnt = Squad['stats']['matches_cnt']
        Squad_win_matches_cnt = Squad['stats']['win_matches_cnt']
        Squad_topten_matches_cnt = Squad['stats']['topten_matches_cnt']
        Squad_kills_sum = Squad['stats']['kills_sum']
        Squad_kills_max = Squad['stats']['kills_max']
        Squad_assists_sum = Squad['stats']['assists_sum']
        Squad_headshot_kills_sum = Squad['stats']['headshot_kills_sum']
        Squad_deaths_sum = Squad['stats']['deaths_sum']
        Squad_longest_kill_max = Squad['stats']['longest_kill_max']
        Squad_rank_avg = round(Squad['stats']['rank_avg'])
        Squad_damage_dealt_avg = round(Squad['stats']['damage_dealt_avg'])
        Squad_time_survived_avg = Squad['stats']['time_survived_avg']
        Squad_rank_points = Squad['stats']['rank_points']
        Squad_rating = Squad['stats']['rating']

        Squad_rank = Squad['ranks']['rank_points']

        embed = discord.Embed(title='[ 🔫🔫🔫🔫 스쿼드 ] ' + temp[1], color=0xFF0000)
        embed.set_thumbnail(url=Squad_imageurl)
        embed.add_field(name='👑 타이틀',value=str(Squad_tier), inline=True)
        embed.add_field(name='🏅 전체 순위',value=str(Squad_rank) + ' 위', inline=True)
        embed.add_field(name='총 플레이 수',value=str(Squad_matches_cnt) + ' 게임', inline=True)
        embed.add_field(name='승리한 경기 수',value=str(Squad_win_matches_cnt) + ' 승리', inline=True)
        embed.add_field(name='Top 10 이내 경기 수',value=str(Squad_topten_matches_cnt) + ' 진입', inline=True)
        embed.add_field(name='전체 플레이 Kill 수',value=str(Squad_kills_sum) + ' 명', inline=True)
        embed.add_field(name='최다 킬',value=str(Squad_kills_max) + ' 명', inline=True)
        embed.add_field(name='최다 어시스트',value=str(Squad_assists_sum) + ' 번', inline=True)
        embed.add_field(name='헤드샷',value=str(Squad_headshot_kills_sum) + ' 번', inline=True)
        embed.add_field(name='최대 거리 킬',value=str(Squad_longest_kill_max) + ' M', inline=True)
        embed.add_field(name='평균 등수',value=str(Squad_rank_avg) + ' 등', inline=True)
        embed.add_field(name='경기 당 데미지',value=str(Squad_damage_dealt_avg), inline=True)
        embed.add_field(name='레이팅',value=str(Squad_rating), inline=True)

        await client.send_message(message.channel, embed=embed)

        #embed.set_author(name="코하쿠봇 (KOHAKU BOT)")
        #embed.add_field(name=temp5[item], value=temp4[item], inline=True)
        #embed.add_field(name="서버 ID ", value=ctx.message.server.id, inline=True)
        #embed.add_field(name="존재하는 역할 ", value=len(ctx.message.server.roles), inline=True)
        #embed.add_field(name="멤버 수 ", value=len(ctx.message.server.members), inline=True)
        #embed.set_thumbnail(url=ctx.message.server.icon_url)

    #-------------------------------------------------------------------------------------------------------------------------------------------------
    #$$$$$$$\   $$$\     $$$$$$$$\
    #$$  __$$\ $$ $$\    $$  _____|
    #$$ |  $$ |\$$$\ |   $$ |
    #$$ |  $$ |$$\$$\$$\ $$$$$\
    #$$ |  $$ |$$ \$$ __|$$  __|
    #$$ |  $$ |$$ |\$$\  $$ |
    #$$$$$$$  | $$$$ $$\ $$ |
    #\_______/  \____\__|\__|

    #GjSTNvOnIkQwN6iXwsUAF6EbAHVMimDS
    #카인 진깽.
    #던전앤파이터 캐릭터 정보 조회
    if message.content.startswith("!던파"):
        df_search = message.content.split(" ")

        df_url = 'https://api.neople.co.kr/df/servers/'
        img_url = 'https://img-api.neople.co.kr/df/servers/'
        zoom = '?zoom=1'
        char_url = '/characters?characterName='
        key_url = '&apikey=h59qCgA8YFc7IIwDWSPO2igPReBzJFJh'

        server_db = {
                #던전앤파이터 서버목록
                '카인': "cain", '디레지에': "diregie", '안톤': "anton",
                '바칼': 'bakal', '카시야스': "casillas", '힐더': "hilder",
                '프레이': 'prey', '시로코': "siroco"
        }

        key = str(uuid4())
        df_sv = server_db[df_search[1]]

        charname = urllib.parse.quote(df_search[2]) # 아이디 url인코딩
        df_requrl = df_url + df_sv + char_url + charname + key_url #캐릭터 기본정보 조회
        df_req = Request(df_requrl)
        df_html = urllib.request.urlopen(df_req)
        df_soup = BeautifulSoup(df_html,"html.parser")
        json_data = json.loads(df_soup.text)

        df_data = json_data['rows'] #rows안의 값만 가져옴
        chid = df_data[0]['characterId']
        level = df_data[0]['level']
        job = df_data[0]['jobGrowName']

        ch_img = img_url + df_sv + '/characters/' + chid + zoom #캐릭터 이미지 url
        ch_ab = df_url + df_sv + '/characters/' + chid + '/status?apikey=h59qCgA8YFc7IIwDWSPO2igPReBzJFJh' #장비
        df_main = 'http://df.nexon.com/df/info/character?sv=' + df_sv + '&charac_name=' + charname

        #캐릭터 능력치
        df_req1 = Request(ch_ab)
        df_html1 = urllib.request.urlopen(df_req1)
        df_soup1 = BeautifulSoup(df_html1,"html.parser")
        json_data1 = json.loads(df_soup1.text)
        df_data1 = json_data1['status'] #rows안의 값만 가져옴

        basic1 = df_data1[2]['value']#힘
        basic2 = df_data1[3]['value']#지능
        basic3 = df_data1[4]['value']#체력
        basic4 = df_data1[5]['value']#정신력

        att1 = df_data1[6]['value']#물공
        att2 = df_data1[7]['value']#마공
        att3 = df_data1[8]['value']#독공

        percent1 = df_data1[11]['value']#물크
        percent2 = df_data1[12]['value']#마크
        percent3 = df_data1[16]['value']#항마

        up1 = df_data1[23]['value']#화속강
        up2 = df_data1[25]['value']#수속강
        up3 = df_data1[27]['value']#명속강
        up4 = df_data1[29]['value']#암속강

        dun_url = 'http://dundam.xyz/view.jsp?server=' + df_sv + '&name=' + charname + '&image=' + chid

        df_home1 = 'http://dunp.net/'
        #df_hom2 = 'http://dundam.xyz'
        df_home3 = 'http://dnfa.kr/DNFAssist_Caracter/Detail?characterId='+chid+'&server='+df_sv
        df_all_link = "[공홈]("+df_main+") | [던담]("+dun_url+") | [어시스트]("+df_home3+") | [프로필생성]("+df_home1+")"

        embed2 = discord.Embed(title='', colour=0x000000)
        embed2.set_author(name = '검색결과', url =df_main )
        embed2.set_thumbnail(url='https://blogfiles.pstatic.net/MjAxODExMDVfMjc4/MDAxNTQxNDAwMjI2NDA5.UlXRGCOrzAXvUWaGsJ5xc552ImbmiWcjsZyPfYyrIaAg.r7O_scBHyT9hsYI78U5NZS9YZj12CbjyLxiGZ5FTdw0g.PNG.ig6268/%EB%8D%98%ED%8C%8C.png')
        embed2.set_image(url=ch_img)
        embed2.add_field(name='정보', value = df_search[1] +' - '+df_search[2]+'\n레벨 : '+str(level)+'\n직업 : '+str(job), inline=True)
        #embed2.add_field(name='캐릭터명', value = df_search[2], inline=True)
        #embed2.add_field(name='직업', value = str(job), inline=True)
        #embed2.add_field(name='레벨', value = str(level), inline=True)


        embed = discord.Embed(title='', colour=0x000000)
        embed.add_field(name=':arrow_right: 링크', value = df_all_link, inline=False)
        embed.add_field(name='힘\t\t\t지능 \t\t 체력 \t\t 정신력',
        value = str(basic1) + ' :black_small_square: ' + str(basic2) + ' :black_small_square: '+ str(basic3) + ' :black_small_square: '+ str(basic4), inline=False)
        embed.add_field(name='물리공격 \t 마법공격 \t 독립공격',
        value = str(att1) + ':black_small_square::black_small_square:' + str(att2) + ':black_small_square::black_small_square:' + str(att3), inline=False)
        embed.add_field(name='항마 \t 물크 \t 마크',
        value = str(percent3) + ':black_small_square: '+ str(percent1) + ':black_small_square: ' + str(percent2), inline=False)
        embed.add_field(name='화속 \t 수속 \t 명속 \t 암속',
        value = str(up1) + ':black_small_square: ' + str(up2) + ':black_small_square: '+ str(up3) + ':black_small_square: '+ str(up4), inline=False)

        await client.send_message(message.channel,embed=embed2)
        await client.send_message(message.channel,embed=embed)

client.run(token)
