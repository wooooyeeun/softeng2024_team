document.addEventListener("DOMContentLoaded", () => {
    const photoContainer = document.getElementById('photo-container');
    let currentCategory = 'restaurants'; // 초기 카테고리 설정
    let currentRegion = '전주'; // 초기 지역 설정
    let currentTab = 'jeonbuk'; // 초기 탭 설정

    // 데이터 파싱
    const categoryData = {};
    document.querySelectorAll('#category-data > div[data-category]').forEach(categoryElem => {
        const category = categoryElem.dataset.category;
        categoryData[category] = {};

        categoryElem.querySelectorAll('div[data-region]').forEach(regionElem => {
            const region = regionElem.dataset.region;
            categoryData[category][region] = [];

            regionElem.querySelectorAll('div[data-name]').forEach(placeElem => {
                categoryData[category][region].push({
                    name: placeElem.dataset.name,
                    image: placeElem.dataset.image
                });
            });
        });
    });

    console.log("Parsed Category Data:", categoryData);

    // 지역 선택 함수
    window.selectRegion = function (region) {
        currentRegion = region;

        // 지역 카드 활성화 상태 업데이트
        document.querySelectorAll(`#${currentTab} .region-card`).forEach(card => {
            const isActive = card.dataset.region === region;
            card.classList.toggle('active', isActive);
        });

        // 현재 카테고리가 'weather'(날씨)인 경우 처리
        if (currentCategory === 'weather') {
            document.querySelectorAll('#weather-container .weather-card').forEach(card => {
                card.style.display = card.dataset.region === currentRegion ? 'block' : 'none';
            });
            update_display(region);

        } else {
            // 날씨가 아닌 경우 사진 표시 함수 호출
            showCategoryPhotos(currentCategory);
        }

        console.log(`Region selected: ${region}, Current Category: ${currentCategory}`);
    };
    function update_display(region) {
        const regionToEnglish = {
    "전주": "Jeonju",
    "군산": "Gunsan",
    "익산": "Iksan",
    "정읍": "Jeongeup",
    "김제": "Gimje",
    "남원": "Namwon",
    "목포": "Mokpo",
    "여수": "Yeosu",
    "순천": "Suncheon",
    "나주": "Naju",
    "광양": "Gwangyang",
    "광주": "Gwangju"
};
        let region_eng = regionToEnglish[region] || region
        // alert(region_eng);

        fetch('http://113.198.63.27:20350/weather?region_name=' + region_eng)
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json(); // JSON 데이터로 변환
    })
    .then(data => {
        console.log('API 호출 결과:', data); // 성공적으로 받은 데이터
    })
    .catch(error => {
        console.error('API 호출 중 오류 발생:', error);
    });

    }

    // 사진 렌더링 함수
    window.showCategoryPhotos = function (category) {
    photoContainer.innerHTML = '';
    const photos = categoryData[category][currentRegion] || [];

    if (photos.length === 0) {
        photoContainer.innerHTML = `<p>해당 지역 및 카테고리에 대한 데이터가 없습니다.</p>`;
    } else {
        photos.forEach(photo => {
            const photoCard = document.createElement('div');
            photoCard.className = 'photo-card';
            photoCard.innerHTML = `
                <h3>${photo.name}</h3>
            `;
            photoCard.addEventListener('click', () => {
                window.location.href = `/detail/${encodeURIComponent(photo.name)}/`;
            });
            photoContainer.appendChild(photoCard);
        });
    }

        console.log(`Rendered photos for category "${category}" in region "${currentRegion}":`, photos);
    };

    // 카테고리 선택 함수
    document.getElementById('category-select').addEventListener('change', (event) => {
        currentCategory = event.target.value;

        if (currentCategory === 'weather') {
            document.getElementById('photo-container').style.display = 'none';
            document.getElementById('weather-container').style.display = 'flex';

            // 선택한 지역에 해당하는 날씨만 표시
            document.querySelectorAll('#weather-container .weather-card').forEach(card => {
                card.style.display = card.dataset.region === currentRegion ? 'block' : 'none';
            });
        } else {
            document.getElementById('photo-container').style.display = 'flex';
            document.getElementById('weather-container').style.display = 'none';
            showCategoryPhotos(currentCategory);
        }
    });

    // 탭 전환 함수
    document.querySelectorAll('.tab').forEach(tab => {
        tab.addEventListener('click', () => {
            document.querySelectorAll('.tab').forEach(t => t.classList.remove('active'));
            tab.classList.add('active');

            currentTab = tab.dataset.tab;
            currentRegion = currentTab === 'jeonbuk' ? '전주' : '여수'; // 전라북도는 전주, 전라남도는 여수로 초기화
            document.querySelectorAll('.tab-content').forEach(content => {
                content.classList.toggle('active', content.id === currentTab);
            });

            selectRegion(currentRegion);
            showCategoryPhotos(currentCategory);
        });
    });

    // 초기 데이터 렌더링
    selectRegion(currentRegion);
    showCategoryPhotos(currentCategory);
});