// Получаем ссылки на все нужные элементы
const selectElement = document.getElementById("function");
const kInput = document.getElementById("k_coefficient");
const aInput = document.getElementById("a_coefficient");
const bInput = document.getElementById("b_coefficient");
const cInput = document.getElementById("c_coefficient");
const xInput = document.getElementById("x_value");
const startInput = document.getElementById("start_length");
const endInput = document.getElementById("end_length");

// Функция для скрытия поля
function hideElement(element) {
    element.style.display = "none";
}

// Функция для отображения поля
function showElement(element) {
    element.style.display = "block";
}

// Функция для скрытия полей при загрузке страницы
function hideAllFields() {
    hideElement(kInput);
    hideElement(aInput);
    hideElement(bInput);
    hideElement(cInput);
    hideElement(xInput);
    hideElement(startInput);
    hideElement(endInput);
    hideElement(calc);
}

// Обработчик события изменения выбранной функции
selectElement.addEventListener("change", function () {
    // Получаем выбранное значение
    const selectedFunction = selectElement.value;

    // Показываем все поля
    showElement(kInput);
    showElement(aInput);
    showElement(bInput);
    showElement(cInput);
    showElement(xInput);
    showElement(startInput);
    showElement(endInput);
    showElement(calc);

    // Скрываем ненужные поля в зависимости от выбранной функции
    if (selectedFunction === "linear") {
        hideElement(aInput);
        hideElement(xInput);
        hideElement(cInput);
    } else if (selectedFunction === "quadratic") {
        hideElement(kInput);
        hideElement(xInput);
    } else if (selectedFunction === "power") {
        hideElement(kInput);
        hideElement(xInput);
        hideElement(bInput);
        hideElement(cInput);
    } else if (selectedFunction === "selection") {
        hideElement(kInput);
        hideElement(aInput);
        hideElement(bInput);
        hideElement(cInput);
        hideElement(xInput);
        hideElement(startInput);
        hideElement(endInput);
    }
});

// Скрытие полей при загрузке страницы
hideAllFields();

function handleFormSubmit(event) {
    // Проверяем выбранную функцию и скрываем ненужные поля
    // ...

    // Отправляем форму
    document.getElementById("myForm").submit();

    // Отменяем действие по умолчанию (отправку формы) для предотвращения дублирования отправки
    event.preventDefault();
}