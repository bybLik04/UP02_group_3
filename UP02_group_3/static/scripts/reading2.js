var xhr2 = new XMLHttpRequest();
var filePath2 = 'static/scripts/aprox1.txt';
xhr2.open('GET', filePath2, true);

// ���������� �������� �����, ������� ����� �������� ��� �������� ���������� �������
xhr2.onload = function () {
    if (xhr.status === 200) {
        var text2 = xhr2.responseText;

        // ��������� ����� � ������� � id "content"
        document.getElementById('hiddenText2').innerText = text2;
    }
};

// ���������� ������
xhr2.send();