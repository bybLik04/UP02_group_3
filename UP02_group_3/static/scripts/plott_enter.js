// �������� ������ �� ��� ������ ��������
const selectElement = document.getElementById("function");
const kInput = document.getElementById("k_coefficient");
const aInput = document.getElementById("a_coefficient");
const bInput = document.getElementById("b_coefficient");
const cInput = document.getElementById("c_coefficient");
const xInput = document.getElementById("x_value");
const startInput = document.getElementById("start_length");
const endInput = document.getElementById("end_length");

// ������� ��� ������� ����
function hideElement(element) {
    element.style.display = "none";
}

// ������� ��� ����������� ����
function showElement(element) {
    element.style.display = "block";
}

// ������� ��� ������� ����� ��� �������� ��������
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

// ���������� ������� ��������� ��������� �������
selectElement.addEventListener("change", function () {
    // �������� ��������� ��������
    const selectedFunction = selectElement.value;

    // ���������� ��� ����
    showElement(kInput);
    showElement(aInput);
    showElement(bInput);
    showElement(cInput);
    showElement(xInput);
    showElement(startInput);
    showElement(endInput);
    showElement(calc);

    // �������� �������� ���� � ����������� �� ��������� �������
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

// ������� ����� ��� �������� ��������
hideAllFields();

function handleFormSubmit(event) {
    // ��������� ��������� ������� � �������� �������� ����
    // ...

    // ���������� �����
    document.getElementById("myForm").submit();

    // �������� �������� �� ��������� (�������� �����) ��� �������������� ������������ ��������
    event.preventDefault();
}