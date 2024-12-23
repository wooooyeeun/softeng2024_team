const swiper = new Swiper('.swiper-container', {
    loop: true, // 무한 루프
    autoplay: {
        delay: 4000, // 4초마다 자동 슬라이드
        disableOnInteraction: false,
    },
    pagination: {
        el: '.swiper-pagination',
        clickable: true,
    },
    navigation: {
        nextEl: '.swiper-button-next',
        prevEl: '.swiper-button-prev',
    },
});