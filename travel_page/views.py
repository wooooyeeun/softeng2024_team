from django.shortcuts import render
import random
import csv
import os
from .utils import get_weather
import requests

BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # views.py 파일의 디렉토리
region_csv_path = os.path.join(BASE_DIR, 'static', 'travel_page', 'data', 'region_data.csv')
travel_csv_path = os.path.join(BASE_DIR, 'static', 'travel_page', 'data', 'travel_data.csv')
FLASK_API_URL = "http://192.168.0.103:5000/weather"

def load_travel_data(csv_file_path):
    travel_data = []
    try:
        with open(csv_file_path, newline='', encoding='utf-8-sig') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                travel_data.append({
                    'file': row.get('image', 'default.png').strip(),
                    'alt': row.get('name', 'No name').strip(),
                    'title': row.get('name', 'No title').strip(),
                    'description': row.get('description', 'No description').strip()
                })
    except Exception as e:
        print(f"Error reading travel_data.csv: {e}")
    return travel_data

def index(request):
    travel_data = load_travel_data(travel_csv_path)

    images = [
        {
            'file': 'jeonju.jpg',
            'alt': '전주 한옥마을',
            'title': '전주 한옥마을',
            'description': '한국 전통의 멋을 느낄 수 있는 전주 한옥마을.'
        },
        {
            'file': 'yeosu.jpg',
            'alt': '여수 밤바다',
            'title': '여수 밤바다~',
            'description': '낭만적인 여수의 아름다운 밤바다.'
        },
        {
            'file': 'suncheon.jpg',
            'alt': '순천만 습지',
            'title': '순천만 습지',
            'description': '생태계의 보고, 순천만 자연 습지.'
        }
    ]

    options = [
        {'name': '여행지', 'image': 'food.jpg', 'link': '/region/'},
        {'name': '체크리스트', 'image': 'check.jpg', 'link': '/todo/'},
        {'name': '커뮤니티', 'image': 'community.jpg', 'link': '/community/'},
    ]

    return render(request, 'travel_page/index.html', {'images': images, 'options': options})


def load_region_data(csv_file_path):
    data = {'restaurants': {}, 'touristSpots': {}}
    try:
        with open(csv_file_path, newline='', encoding='utf-8-sig') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                category = row.get('category', '').strip()
                region = row.get('region', '').strip()
                name = row.get('name', '').strip()
                image = row.get('image', '').strip() or 'default.png'

                if not category or not region or not name:
                    continue

                if category not in data:
                    data[category] = {}
                if region not in data[category]:
                    data[category][region] = []

                # 파일 이름만 포함
                data[category][region].append({
                    'name': name,
                    'image': image
                })
    except Exception as e:
        print(f"Error reading CSV file: {e}")
    return data

# 지역별 페이지
def region(request):
    jeonbuk = []
    jeonnam = []
    weather_data = {}
    category_data = load_region_data(travel_csv_path)
    travel_data = load_travel_data(travel_csv_path)

    try:
        with open(region_csv_path, encoding='utf-8-sig') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # 이미지 이름만 전달
                if row['province'] == '전라북도':
                    jeonbuk.append({'name': row['region'], 'image': row['image']})
                elif row['province'] == '전라남도':
                    jeonnam.append({'name': row['region'], 'image': row['image']})
                weather_data[row['region']] = get_weather(row['region_eng'])
    except Exception as e:
        print(f"Error reading region_data.csv: {e}")

    if request.method == "POST":
        region_name = request.POST.get("region_eng")  # 선택된 지역 (영문)
        if region_name:
            try:
                # Flask API 호출
                response = requests.get(f"{FLASK_API_URL}?region_name={region_name}")
                weather_data = response.json()  # Flask에서 반환된 JSON 데이터
                return render(request, 'travel_page/region.html', {
                    'jeonbuk': jeonbuk,
                    'jeonnam': jeonnam,
                    'category_data': category_data,
                    'weather_data': weather_data,
                    'selected_region': region_name,
                })
            except requests.exceptions.RequestException as e:
                return render(request, 'travel_page/region.html', {
                    'jeonbuk': jeonbuk,
                    'jeonnam': jeonnam,
                    'category_data': category_data,
                    'weather_error': "Flask 서버와 통신할 수 없습니다."
                })

    return render(request, 'travel_page/region.html', {
        'jeonbuk': jeonbuk,
        'jeonnam': jeonnam,
        'category_data': category_data,
        'weather_data': weather_data,
        'travel_data': travel_data,
    })

def detail_view(request, name):
    travel_data = load_travel_data(travel_csv_path)

    detail = next((item for item in travel_data if item['title'] == name), None)
    if not detail:
        return render(request, '404.html')

    return render(request, 'travel_page/region_detail.html', {'detail': detail})

