from operator import itemgetter
import requests
import json
import datetime


def today_weather(nx, ny):
    vilage_weather_url = "http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getVilageFcst?"

    service_key = "kK%2BhUecCXInxgNTPSHW%2BP132fAuWPScRIujCRBLQQJ9w1J3S%2BsHfNBxM%2BDbgdE36m2pj6hS%2BkSkzGPBRKwghJg%3D%3D"

    today = datetime.datetime.today()
    base_date = "20220530"
    # base_date = today.strftime("%Y%m%d") # 날짜
    base_time = "0800" # 날씨 값

    payload = "serviceKey=" + service_key + "&" +\
        "dataType=json" + "&" +\
        "base_date=" + base_date + "&" +\
        "base_time=" + base_time + "&" +\
        "nx=" + str(nx) + "&" +\
        "ny=" + str(ny)

    # 값 요청
    res = requests.get(vilage_weather_url + payload)
    items = res.json().get('response').get('body').get('items')

    weather_data = dict()
    weather_data['date'] = today.strftime("%Y-%m-%d")
    for item in items['item']:
        # 강수형태
        if item['category'] == 'PTY':
            
            weather_code = item['fcstValue']
            
            if weather_code == '1':
                weather_state = '비'
            elif weather_code == '2':
                weather_state = '비/눈'
            elif weather_code == '3':
                weather_state = '눈'
            elif weather_code == '4':
                weather_state = '소나기'
            else:
                weather_state = '맑음'
            
            weather_data['state'] = weather_state

        # 1시간 강수량
        if item['category'] == 'PTY':
            weather_data['precipitation'] = item['fcstValue']      

        # 1시간 기온
        if item['category'] == 'TMP':
            weather_data['temperature'] = item['fcstValue']
        
    return weather_data 

# print(today_climate(60, 120))
# {'temperature': '20', 'state': '맑음', 'precipitation': '0'} 20도 맑음 강수량 0 