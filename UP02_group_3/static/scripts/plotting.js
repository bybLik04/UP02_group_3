// Генерация случайных коэффициентов
function getRandomCoefficients() {
    return {
        a0: Math.random() * 10,
        a1: Math.random() * 10,
        a2: Math.random() * 10
    };
}

// Вычисление значений функции для заданных коэффициентов
function calculateFunction(coefficients, x) {
    const { a0, a1, a2 } = coefficients;
    return a0 + a1 * x + a2 * x * x;
}

function calculateFunction2(coefficients, x) {
    const { a0, a1} = coefficients;
    return a0 + a1 * x;
}

// Построение графика
function plotGraph(coefficients, canvasId) {
    const canvas = document.getElementById(canvasId);
    const ctx = canvas.getContext('2d');

    const data = [];
    for (let x = 0; x <= 10; x += 0.1) {
        const y = calculateFunction(coefficients, x);
        data.push({ x, y });
    }

    new Chart(ctx, {
        type: 'line',
        data: {
            datasets: [{
                label: 'Аппроксимированная функция',
                data: data,
                borderColor: 'blue',
                fill: false
            }]
        },
        options: {
            responsive: true,
            scales: {
                x: {
                    type: 'linear',
                    position: 'bottom'
                },
                y: {
                    type: 'linear',
                    position: 'left'
                }
            }
        }
    });
}

function plotGraph2(coefficients, canvasId) {
    const canvas = document.getElementById(canvasId);
    const ctx = canvas.getContext('2d');

    const data = [];
    for (let x = 0; x <= 10; x += 0.1) {
        const y = calculateFunction2(coefficients, x);
        data.push({ x, y });
    }

    new Chart(ctx, {
        type: 'line',
        data: {
            datasets: [{
                label: 'Аппроксимированная функция',
                data: data,
                borderColor: 'blue',
                fill: false
            }]
        },
        options: {
            responsive: true,
            scales: {
                x: {
                    type: 'linear',
                    position: 'bottom'
                },
                y: {
                    type: 'linear',
                    position: 'left'
                }
            }
        }
    });
}

// Табличные данные (x и y)

const tableData = [
    { x: 1, y: 3 },
    { x: 2, y: 5 },
    { x: 3, y: 7 },
    { x: 4, y: 9 },
    { x: 5, y: 11 }
];

// Вычисление коэффициентов линейной линии регрессии
function calculateRegressionCoefficients() {
    const sumX = tableData.reduce((sum, data) => sum + data.x, 0);
    const sumY = tableData.reduce((sum, data) => sum + data.y, 0);
    const sumXY = tableData.reduce((sum, data) => sum + data.x * data.y, 0);
    const sumXX = tableData.reduce((sum, data) => sum + data.x * data.x, 0);
    const n = tableData.length;

    const a1 = (n * sumXY - sumX * sumY) / (n * sumXX - sumX * sumX);
    const a0 = (sumY - a1 * sumX) / n;

    return { a0, a1 };
}

// Вычисление коэффициента детерминированности R^2
function calculateR2(regressionCoefficients) {
    const { a0, a1 } = regressionCoefficients;

    const meanY = tableData.reduce((sum, data) => sum + data.y, 0) / tableData.length;
    const sst = tableData.reduce((sum, data) => sum + (data.y - meanY) ** 2, 0);
    const ssr = tableData.reduce((sum, data) => sum + (calculateFunction(regressionCoefficients, data.x) - meanY) ** 2, 0);

    return 1 - ssr / sst;
}

// Создание графика для функции y = sin(x)
var ctx = document.getElementById('graph').getContext('2d');
var data = [];
for (var x = 0; x <= 10; x += 0.1) {
    var y = Math.sin(x);
    data.push({ x: x, y: y });
}
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

// Генерация случайных коэффициентов и построение графика аппроксимации
const coefficients = getRandomCoefficients();
plotGraph(coefficients, 'square');

// Генерация случайных коэффициентов, вычисление линейной линии регрессии и построение графика
const regressionCoefficients = calculateRegressionCoefficients();
const r2 = calculateR2(regressionCoefficients);
plotGraph2(regressionCoefficients, 'linear');

console.log('Коэффициенты линейной линии регрессии:', regressionCoefficients);
console.log('Коэффициент детерминированности R^2:', r2);