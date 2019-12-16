#201444032 정성준
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from matplotlib import font_manager
import urllib.request as urls
import json
import xmltodict
import folium
import webbrowser
import os


#폰트 깨짐 방지
font_location="C:/Windows/Fonts/malgun.ttf"
font_name = font_manager.FontProperties(fname=font_location).get_name()
matplotlib.rc('font', family=font_name)
matplotlib.rcParams['axes.unicode_minus'] = False

try:
    
    #각 년도별 합계 들어갈 데이터프레임 0=2014, 1=2015, 2=2016, 3=2017, 4=2018
    list_year = list()
    
    #서비스 키를 이용해 가져올 url
    for y in range(4,9,1):
        index_list = list()
        url = 'http://openapi.airport.co.kr/service/rest/totalAirportStatsService/getAirportStats?startDePd=201{0}01&endDepd=201{1}12&routeBe=0&nvgBe=0&pasngrCargoBe=0&pasngrBe=0&cargoBe=0&ServiceKey=X0XxUEIEhuM%2BzyhkbAVSessJ0OZbzG%2FHyT0N0Mg26We%2BWHDaybRGPuPStJBzIzM%2FWH2TZvo9noxqEwDYFTj4Aw%3D%3D'.format(y,y)
        req = urls.Request(url)
        res = urls.urlopen(req)
        rescode = res.getcode()
        #오류 확인(성공적으로 가져올시 code:200)
        if(rescode == 200):
            res_body = res.read()
            rD = xmltodict.parse(res_body) #xml 형태의 데이터를 dict형식으로 변환(list형식으로 들어옴) 보기불편
            rDJ = json.dumps(rD) #보기불편해서 json형식으로 변환
            rDD = json.loads(rDJ) #다시 보기 편하게 dict형태로 변환

            w_data = rDD['response']['body']['items']['item'] #dict형식에서 item을 사용하기 편하게 설정

            for i in w_data:
                index_list.append(i['airport'])
                
                '''
                print('공항:', i['airport'])
                print('도착 화물(KG):', i['arrcargo'])
                print('도착 운항 편수:', i['arrflgt'])
                print('도착 여객 인원수:', i['arrpassenger'])
                print('출발 화물(KG):', i['depcargo'])
                print('출발 운항 편수:', i['depflgt'])
                print('출발 여객 인원수', i['deppassenger'])
                print('화물 소계:', i['subcargo'])
                print('운항편수 소계:', i['subflgt'])
                print('여객 인원 소계:', i['subpassenger'])
                print('-------------------------------------')
                '''
        print('=============201{0}==========='.format(y))
        # df = 디셔너리 형태의 데이터를 데이터 프레임으로 만듬
        df = pd.DataFrame(w_data, index = index_list)
        # df2 = 쓸모없는 데이터 슬라이싱해서 제거하고 첫번째 열을 인덱스로 바꿈
        df2 = df[:len(index_list)-1]
        del df2['airport']
        index_list.pop()
        #데이터프레임안에 str값들을 int타입으로 변경
        df2=df2.apply(pd.to_numeric, errors='coerce').fillna(0)
        print(df2)
        df2= round(df2/1200)
        list_year.append(df2)
    #각 년도별로 데이터 프레임을 리스트로 변경해서 저장
    df_2014 = list_year[0]
    df_2015 = list_year[1]
    df_2016 = list_year[2]
    df_2017 = list_year[3]
    df_2018 = list_year[4]
    #양양을 제거
    df_2014 = df_2014.drop('양양')
    df_2015 = df_2015.drop('양양')
    df_2016 = df_2016.drop('양양')


    list_folium = []
    #2018년도 총 여객수를 백분율로 처리
    for f in range(len(df_2018)):
        list_folium.append(((df_2018['subpassenger'][f])/41366)*100)

    #포리움을 이용해 맵을 생성
    map_osm = folium.Map(location=[36.392087, 127.979799], zoom_start=7)
    #JSON파일을 가져와 한국 지도를 읽어옴
    rfile = open('./provinces-geo.json', 'r', encoding='utf-8').read()
    #json파일을 읽어옴
    jsonData = json.loads(rfile)
    #json형식의 데이터로 읽어온 지도를 시각화
    folium.GeoJson(jsonData, name='json_data').add_to(map_osm)
    #각 공항별 서클마커를 이용해 마킹
    folium.CircleMarker([37.5566873, 126.808431],radius=list_folium[0], popup='김포공항', color='red').add_to(map_osm)
    folium.CircleMarker([35.1730746, 128.945753],radius=list_folium[1], popup='김해공항', color='red').add_to(map_osm)
    folium.CircleMarker([33.5078867, 126.493115],radius=list_folium[2], popup='제주공항', color='red').add_to(map_osm)
    folium.CircleMarker([35.8995071, 128.638413],radius=list_folium[3], popup='대구공항', color='red').add_to(map_osm)
    folium.CircleMarker([35.1404087, 126.810244],radius=list_folium[4], popup='광주공항', color='red').add_to(map_osm)
    folium.CircleMarker([34.993608, 126.387823],radius=list_folium[5], popup='무안공항', color='red').add_to(map_osm)
    folium.CircleMarker([36.7244680, 127.495894],radius=list_folium[6], popup='청주공항', color='red').add_to(map_osm)
    folium.CircleMarker([34.8419284, 127.612867],radius=list_folium[7], popup='여수공항', color='red').add_to(map_osm)
    folium.CircleMarker([35.5939500, 129.356123],radius=list_folium[8], popup='울산공항', color='red').add_to(map_osm)
    folium.CircleMarker([35.0919269, 128.086335],radius=list_folium[9], popup='진주공항', color='red').add_to(map_osm)
    folium.CircleMarker([35.9842810, 129.434131],radius=list_folium[10], popup='포항공항', color='red').add_to(map_osm)
    folium.CircleMarker([35.9264216, 126.615624],radius=list_folium[11], popup='군산공항', color='red').add_to(map_osm)
    folium.CircleMarker([37.4591310, 127.977068],radius=list_folium[12], popup='원주공항', color='red').add_to(map_osm)
    folium.CircleMarker([37.4795073, 126.440877],radius=list_folium[13], popup='인천공항', color='red').add_to(map_osm)
    #그린 맵을 html형태로 저장
    map_osm.save('./map.html')
    #저장된 파일을 브라우저로 띄움
    webbrowser.open('file:\\'+os.path.realpath('./map.html'))

        

    #그래프1 공항별 5년간 (출발,도착)인원, 화물
    index = np.arange(df2.shape[0])
    bar_width = 0.2
    fig, ax = plt.subplots()
    b1 = ax.bar(index-bar_width,df_2014['arrcargo'] , bar_width, label='도착 화물')
    b2 = ax.bar(index,df_2014['depcargo'] , bar_width, label='출발 화물')
    b3 = ax.bar(index+bar_width,df_2014['arrpassenger'] , bar_width, label='도착 여객 인원수')
    b4 = ax.bar(index+(bar_width*2),df_2014['deppassenger'] , bar_width, label='도착 여객 인원수')
    ax.set_xlabel('공항')
    ax.set_ylabel('이용수')
    ax.set_title('공항별 (도착/출발) 인원, 화물')
    ax.set_xticks(index+bar_width/2)
    ax.set_xticklabels(index_list)
    ax.legend()
    plt.show()

except Exception as er:
    print(er)
else:
    print('Completed!!')
