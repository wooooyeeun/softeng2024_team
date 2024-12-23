from django.shortcuts import render
import random
import csv
import os
from .utils import get_weather

BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # views.py 파일의 디렉토리
region_csv_path = os.path.join(BASE_DIR, 'static', 'travel_page', 'data', 'region_data.csv')
travel_csv_path = os.path.join(BASE_DIR, 'static', 'travel_page', 'data', 'travel_data.csv')

def load_travel_data(csv_file_path):
    """travel_data.csv를 읽고 데이터를 반환"""
    travel_data = []
    try:
        with open(csv_file_path, newline='', encoding='utf-8-sig') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                travel_data.append({
                    'file': row.get('image', 'default.png').strip(),  # 이미지 경로
                    'alt': row.get('name', 'No name').strip(),  # 대체 텍스트
                    'title': row.get('name', 'No title').strip(),  # 타이틀
                    'description': row.get('description', 'No description').strip()  # 설명
                })
    except Exception as e:
        print(f"Error reading travel_data.csv: {e}")
    return travel_data

def index(request):
    """메인 페이지"""
    travel_data = load_travel_data(travel_csv_path)  # travel_data.csv 데이터 로드

    # travel_data에서 랜덤으로 최대 3개의 항목 선택
    images = random.sample(travel_data, min(3, len(travel_data))) if travel_data else []

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
    category_data = load_region_data(travel_csv_path)  # CSV 데이터 로드

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

    return render(request, 'travel_page/region.html', {
        'jeonbuk': jeonbuk,
        'jeonnam': jeonnam,
        'category_data': category_data,
        'weather_data': weather_data
    })

def detail_view(request, name):
    """디테일 페이지"""
    travel_data = load_travel_data(travel_csv_path)  # travel_data.csv 데이터 로드

    # 이름에 해당하는 데이터 찾기
    detail = next((item for item in travel_data if item['title'] == name), None)
    if not detail:
        return render(request, '404.html')  # 데이터가 없으면 404 페이지 렌더링

    return render(request, 'travel_page/region_detail.html', {'detail': detail})

