// �������� ��������� ��� ��������� �� ������
var ctx = document.getElementById('graph').getContext('2d');

// ��������� ������ ��� �������
var data = [];
for (var x = 0; x <= 10; x += 0.1) {
    var y = Math.sin(x);
    data.push({ x: x, y: y });
}

// �������� �������
var chart = new Chart(ctx, {
    type: 'line',
    data: {
        datasets: [{
            label: 'f(x) = sin(x)',
            data: data,
            borderColor: 'blue',
            backgroundColor: 'transparent'
        }]
    },
    options: {
        scales: {
            x: {
                type: 'linear',
                position: 'bottom'
            }
        }
    }
});