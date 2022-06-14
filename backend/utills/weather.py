from operator import itemgetter
import requests
import json
import datetime

def today_weather(date, input_datetime, lat, lng):
    url = "http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getVilageFcst?"
    ServiceKey = "kK+hUecCXInxgNTPSHW+P132fAuWPScRIujCRBLQQJ9w1J3S+sHfNBxM+DbgdE36m2pj6hS+kSkzGPBRKwghJg=="

    base_date = ''.join(date.split('-'))
    base_time = ''.join(input_datetime.split(':'))

    # base_time : 0200, 0500, 0800, 1100, 1400, 1700, 2000, 2300
    if int(base_time) < int("0500"): 
        base_time = "0200" 
    elif int(base_time) < int("0800"):
        base_time = "0500" 
    elif int(base_time) < int("1100"):
        base_time = "0800" 
    elif int(base_time) < int("1400"):
        base_time = "1100" 
    elif int(base_time) < int("1700"):
        base_time = "1400" 
    elif int(base_time) < int("2000"): 
        base_time = "1700" 
    elif int(base_time) < int("2300"): 
        base_time = "2000" 
    else:
        base_time = "2300"

    params ={
        'ServiceKey' : ServiceKey,
        'numOfRows' : '113',
        'dataType' : 'json',
        'base_date' : base_date,
        'base_time' : base_time,
        'nx' : lat,
        'ny' : lng 
        }

    # 값 요청
    res = requests.get(url, params=params, allow_redirects=False)
    try:
        items = res.json().get('response').get('body').get('items')
    except:
        return {'date': '0000-00-00', 'temperature': '0', 'state': '시간 안나와', 'precipitation': '0'}
    weather_data = dict()
    weather_data['date'] = date
    weather_states = {'1' : '비', '2' : '비/눈', '3' : '눈', '4' : '소나기'}
    for item in items['item']:
        # 강수형태
        if item['category'] == 'PTY':
            
            weather_code = item['fcstValue']
            
            # if weather_code == '1':
            #     weather_state = '비'
            # elif weather_code == '2':
            #     weather_state = '비/눈'
            # elif weather_code == '3':
            #     weather_state = '눈'
            # elif weather_code == '4':
            #     weather_state = '소나기'
            # else:
            #     weather_state = '맑음'

            if weather_code in weather_states.keys():
                weather_state = weather_states[weather_code]
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