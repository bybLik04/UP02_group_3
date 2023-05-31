$(document).ready(function () {
    $('.content picture img').hide(); // —начала скрываем картинку 
    $('.content picture img').css({ opacity: 0, marginTop: '20px' }); // ”станавливаем начальные стили

    $('.content picture img').slideDown(1000).animate({ opacity: 1 }, 1000); // ѕримен€ем анимации дл€ сдвига вниз и плавного по€влени€
});
var toggleButton = document.getElementById('toggleButton');
var hiddenTextContainer = document.getElementById('hiddenTextContainer');
hiddenText = document.getElementById('hiddenText');

toggleButton.addEventListener('click', function () {
    if (hiddenTextContainer.style.height === '0px') {
        hiddenTextContainer.style.height = hiddenText.offsetHeight + 'px';
        hiddenText.style.opacity = '1';
    } else {
        hiddenTextContainer.style.height = '0px';
        hiddenText.style.opacity = '0';
    }
});
