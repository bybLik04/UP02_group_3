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
