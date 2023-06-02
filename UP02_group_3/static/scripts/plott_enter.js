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

// ������� ��� ������� �������� �����
function clearInputValue(element) {
    element.value = "";
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
        hideElement(ERROR);
    } else if (selectedFunction === "quadratic") {
        hideElement(kInput);
        hideElement(xInput);
        hideElement(ERROR);
    } else if (selectedFunction === "power") {
        hideElement(kInput);
        hideElement(xInput);
        hideElement(bInput);
        hideElement(cInput);
        hideElement(ERROR);
    } else if (selectedFunction === "selection") {
        hideElement(kInput);
        hideElement(aInput);
        hideElement(bInput);
        hideElement(cInput);
        hideElement(xInput);
        hideElement(startInput);
        hideElement(endInput);
        hideElement(calc);
        hideElement(ERROR);
    }

    // ������� �������� �����
  clearInputValue(kInput);
  clearInputValue(aInput);
  clearInputValue(bInput);
  clearInputValue(cInput);
  clearInputValue(xInput);
  clearInputValue(startInput);
  clearInputValue(endInput);
});

// ������� ����� ��� �������� ��������
hideAllFields();

const lastSelectedFunction = localStorage.getItem("lastSelectedFunction");
if (lastSelectedFunction) {
    selectElement.value = lastSelectedFunction;
    // ���������� ��� ����
    showElement(kInput);
    showElement(aInput);
    showElement(bInput);
    showElement(cInput);
    showElement(xInput);
    showElement(startInput);
    showElement(endInput);
    showElement(calc);
    showElement(ERROR);

    // �������� �������� ���� � ����������� �� ��������� �������
    if (lastSelectedFunction === "linear") {
        hideElement(aInput);
        hideElement(xInput);
        hideElement(cInput);
    } else if (lastSelectedFunction === "quadratic") {
        hideElement(kInput);
        hideElement(xInput);
    } else if (lastSelectedFunction === "power") {
        hideElement(kInput);
        hideElement(xInput);
        hideElement(bInput);
        hideElement(cInput);
    } else if (lastSelectedFunction === "selection") {
        hideElement(kInput);
        hideElement(aInput);
        hideElement(bInput);
        hideElement(cInput);
        hideElement(xInput);
        hideElement(startInput);
        hideElement(endInput);
        hideElement(calc);
    }

}

function handleFormSubmit(event) {
    const selectedFunction = selectElement.value;
    localStorage.setItem("lastSelectedFunction", selectedFunction);
    // ���������� �����
    document.getElementById("myForm").submit();

    // �������� �������� �� ��������� (�������� �����) ��� �������������� ������������ ��������
    event.preventDefault();
}