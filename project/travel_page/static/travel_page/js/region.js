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

    // 지역 선택 함수


    // 카테고리 선택 함수
    document.getElementById('category-select').addEventListener('change', (event) => {
    currentCategory = event.target.value;

    if (currentCategory === 'weather') {
        document.getElementById('photo-container').style.display = 'none';
        document.getElementById('weather-container').style.display = 'flex';

        // 선택한 지역에 해당하는 날씨만 표시
        document.querySelectorAll('#weather-container .weather-card').forEach(card => {
            if (card.dataset.region === currentRegion) {
                card.style.display = 'block';
            } else {
                card.style.display = 'none';
            }
        });
    } else {
        document.getElementById('photo-container').style.display = 'flex';
        document.getElementById('weather-container').style.display = 'none';
        showCategoryPhotos(currentCategory);
    }
});
    window.selectRegion = function (region) {
        currentRegion = region;
        document.querySelectorAll(`#${currentTab} .region-card`).forEach(card => {
            card.classList.toggle('active', card.dataset.region === region);
        });
        if (currentCategory === 'weather') {
        document.querySelectorAll('#weather-container .weather-card').forEach(card => {
            card.style.display = card.dataset.region === currentRegion ? 'block' : 'none';
        });
    }
        showCategoryPhotos(currentCategory);
    };

    // 사진 렌더링 함수
    window.showCategoryPhotos = function (category) {
        photoContainer.innerHTML = '';
        let photos = [];

        photos = categoryData[category][currentRegion] || [];

        if (photos.length === 0) {
            photoContainer.innerHTML = `<p>해당 지역 및 카테고리에 대한 데이터가 없습니다.</p>`;
        } else {
            photos.forEach(photo => {
                const photoCard = document.createElement('div');
                photoCard.className = 'photo-card';
                photoCard.innerHTML = `
                    <img src="/static/travel_page/images/${photo.image}" alt="${photo.name}">
                    <h3>${photo.name}</h3>
                `;
                photoCard.addEventListener('click', () => {
                    window.location.href = `/detail/${encodeURIComponent(photo.name)}/`;
                });
                photoContainer.appendChild(photoCard);
            });
        }
    };


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

    // 초기 설정
    selectRegion('전주'); // 초기 지역 설정
    showCategoryPhotos('restaurants'); // 초기 카테고리 사진 출력
});