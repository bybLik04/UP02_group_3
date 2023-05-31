
$(document).ready(function () {
    $('.content picture img').hide(); // Сначала скрываем картинку 
    $('.content picture img').css({ opacity: 0, marginTop: '20px' }); // Устанавливаем начальные стили

    $('.content picture img').slideDown(1000).animate({ opacity: 1 }, 1000); // Применяем анимации для сдвига вниз и плавного появления
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


// Создаем новый объект XMLHttpRequest
var xhr = new XMLHttpRequest();
var filePath = 'static/scripts/aprox2.txt'; // Укажите путь к файлу, который вы хотите прочитать

// Открываем файл
xhr.open('GET', filePath, true);

// Определяем обратный вызов, который будет выполнен при успешном завершении запроса
xhr.onload = function () {
    if (xhr.status === 200) {
        var text = xhr.responseText;

        // Вставляем текст в элемент с id "content"
        document.getElementById('hiddenText').innerText = text;
    }
};

// Отправляем запрос
xhr.send();