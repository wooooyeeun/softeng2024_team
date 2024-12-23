from django.shortcuts import render
import random
import csv
import os
from .utils import get_weather

BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # views.py 파일의 디렉토리
region_csv_path = os.path.join(BASE_DIR, 'static', 'travel_page', 'data', 'region_data.csv')
travel_csv_path = os.path.join(BASE_DIR, 'static', 'travel_page', 'data', 'travel_data.csv')


def index(request):
    images = [
        {'file': 'jeonju.png', 'alt': '여수 밤바다', 'title': '여수 밤바다~', 'description': '낭만적인 밤바다'},
        {'file': 'jeonju.png', 'alt': '전주 한옥마을', 'title': '전주 한옥마을', 'description': '우와~ 한옥마을!'},
        {'file': 'jeonju.png', 'alt': '순천', 'title': '순천', 'description': '순천순천'},
    ]
    random.shuffle(images)
    images = images[:3]

    options = [
        {'name': '맛집', 'image': 'food.jpg', 'link': '/region/'},
        {'name': '관광지', 'image': 'theme.jpg', 'link': '/theme/'},
        {'name': '날씨', 'image': 'season.jpg', 'link': '/season/'},
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
                image = row.get('image', '').strip() or 'default.png'  # 기본 이미지 설정

                if not category or not region or not name:
                    continue  # 필수 데이터가 없으면 건너뜀


                if category not in data:
                    data[category] = {}
                if region not in data[category]:
                    data[category][region] = []

                data[category][region].append({
                    'name': name,
                    'image': image,
                })
    except Exception as e:
        print(f"Error reading CSV file: {e}")
    return data

# 지역별 페이지
def region(request):
    jeonbuk = []
    jeonnam = []
    weather_data = {}
    category_data = load_region_data(travel_csv_path)  # CSV에서 데이터 로드

    try:
        with open(region_csv_path, encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                region_name = row.get('region_eng', '').strip()
                if row['province'] == '전라북도':
                    jeonbuk.append({'name': row['region'], 'image': row['image']})
                elif row['province'] == '전라남도':
                    jeonnam.append({'name': row['region'], 'image': row['image']})
                weather_data[row['region']] = get_weather(region_name)
    except Exception as e:
        print(f"Error reading region_data.csv: {e}")

    print("Category Data:", category_data)
    return render(request, 'travel_page/region.html', {
        'jeonbuk': jeonbuk,
        'jeonnam': jeonnam,
        'category_data': category_data,
        'weather_data': weather_data
    })

def detail_view(request, name):
    travel_csv_path = os.path.join('travel_page/static/travel_page/data', 'travel_data.csv')
    travel_data = []
    try:
        with open(travel_csv_path, encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                travel_data.append(row)
    except Exception as e:
        print(f"CSV 파일 읽기 오류: {e}")

    detail = next((item for item in travel_data if item['name'] == name), None)
    if not detail:
        return render(request, '404.html')  # 데이터가 없을 경우 404 페이지
    return render(request, 'travel_page/region_detail.html', {'detail': detail})




