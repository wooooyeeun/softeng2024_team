import requests

def get_weather(region_name):
    api_key = 'b7ea75b3754ae3000da1e7c19ef1d1dd'  # 발급받은 API 키 입력
    base_url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {
        'q': region_name,
        'appid': api_key,
        'units': 'metric',
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()

        response_text = response.text

        temp_key = '"temp":'
        temp_start = response_text.find(temp_key) + len(temp_key)
        temp_end = response_text.find(',', temp_start)
        temperature = response_text[temp_start:temp_end].strip()

        condition_key = '"description":"'
        condition_start = response_text.find(condition_key) + len(condition_key)
        condition_end = response_text.find('"', condition_start)
        condition = response_text[condition_start:condition_end].strip()

        return {
            'temperature': temperature,
            'condition': condition
        }
    except requests.exceptions.RequestException as e:
        print(f"날씨 정보를 가져오는 데 실패했습니다: {e}")
        return {'temperature': 'N/A', 'condition': '정보 없음'}

