$(document).ready(function () {
    $('.content picture img').hide(); // —начала скрываем картинку 
    $('.content picture img').css({ opacity: 0, marginTop: '20px' }); // ”станавливаем начальные стили

    $('.content picture img').slideDown(1000).animate({ opacity: 1 }, 1000); // ѕримен€ем анимации дл€ сдвига вниз и плавного по€влени€
});
