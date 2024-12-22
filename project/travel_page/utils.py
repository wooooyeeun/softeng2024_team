import requests

def get_weather(region_name):
    api_key = 'b7ea75b3754ae3000da1e7c19ef1d1dd'  # 발급받은 API 키 입력
    base_url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {
        'q': region_name,  # 지역명 (영어)
        'appid': api_key,  # API 키
        'units': 'metric',  # 섭씨 온도
        'lang': 'kr'  # 한국어 지원
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # 요청 실패 시 예외 발생

        response_text = response.text  # 응답 텍스트 가져오기

        # 온도 추출
        temp_key = '"temp":'
        temp_start = response_text.find(temp_key) + len(temp_key)
        temp_end = response_text.find(',', temp_start)
        temperature = response_text[temp_start:temp_end].strip()

        # 날씨 상태 추출
        condition_key = '"description":"'
        condition_start = response_text.find(condition_key) + len(condition_key)
        condition_end = response_text.find('"', condition_start)
        condition = response_text[condition_start:condition_end].strip()

        # 결과 반환
        return {
            'temperature': temperature,  # 온도
            'condition': condition       # 날씨 상태
        }
    except requests.exceptions.RequestException as e:
        print(f"날씨 정보를 가져오는 데 실패했습니다: {e}")
        return {'temperature': 'N/A', 'condition': '정보 없음'}