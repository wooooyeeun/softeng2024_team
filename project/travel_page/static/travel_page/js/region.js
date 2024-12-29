document.addEventListener("DOMContentLoaded", () => {
    const photoContainer = document.getElementById('photo-container');
    let currentCategory = 'restaurants'; // 초기 카테고리 설정
    let currentRegion = '전주'; // 초기 지역 설정
    let currentTab = 'jeonbuk'; // 초기 탭 설정


    const categoryData = {};
    document.querySelectorAll('#category-data > div[data-category]').forEach(categoryElem => {
        const category = categoryElem.dataset.category;
        categoryData[category] = {};

        categoryElem.querySelectorAll('div[data-region]').forEach(regionElem => {const region = regionElem.dataset.region;
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

    window.selectRegion = function (region) {
        currentRegion = region;

        document.querySelectorAll(`#${currentTab} .region-card`).forEach(card => {
            const isActive = card.dataset.region === region;
            card.classList.toggle('active', isActive);SS
        });

        if (currentCategory === 'weather') {
            document.querySelectorAll('#weather-container .weather-card').forEach(card => {
                card.style.display = card.dataset.region === currentRegion ? 'block' : 'none';
            });
        } else {
            showCategoryPhotos(currentCategory);
        }

        console.log(`Region selected: ${region}, Current Category: ${currentCategory}`);
    };

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

    document.getElementById('category-select').addEventListener('change', (event) => {
        currentCategory = event.target.value;

        if (currentCategory === 'weather') {
            document.getElementById('photo-container').style.display = 'none';
            document.getElementById('weather-container').style.display = 'flex';

            document.querySelectorAll('#weather-container .weather-card').forEach(card => {
                card.style.display = card.dataset.region === currentRegion ? 'block' : 'none';
            });
        } else {
            document.getElementById('photo-container').style.display = 'flex';
            document.getElementById('weather-container').style.display = 'none';
            showCategoryPhotos(currentCategory);
        }
    });

    document.querySelectorAll('.tab').forEach(tab => {
        tab.addEventListener('click', () => {
            document.querySelectorAll('.tab').forEach(t => t.classList.remove('active'));
            tab.classList.add('active');

            currentTab = tab.dataset.tab;
            currentRegion = currentTab === 'jeonbuk' ? '전주' : '여수';
            document.querySelectorAll('.tab-content').forEach(content => {
                content.classList.toggle('active', content.id === currentTab);
            });

            selectRegion(currentRegion);
            showCategoryPhotos(currentCategory);
        });
    });

    selectRegion(currentRegion);
    showCategoryPhotos(currentCategory);
});