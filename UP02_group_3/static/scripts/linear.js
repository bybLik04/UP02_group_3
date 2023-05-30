// Генерация случайных данных
var data = [];
var n = 100; // Количество точек данных

for (var i = 0; i < n; i++) {
    var x = Math.random() * 10;
    var y = 2 * x + Math.random() * 3; // Уравнение линейной регрессии: y = 2x + noise
    data.push({ x: x, y: y });
}

// Создание SVG-контейнера
var svg = d3.select('#chart')
    .attr('width', 400)
    .attr('height', 400);

// Создание шкалы для осей
var xScale = d3.scaleLinear()
    .domain([0, 10]) // Диапазон значений по оси X
    .range([0, 400]); // Диапазон пикселей

var yScale = d3.scaleLinear()
    .domain([0, 30]) // Диапазон значений по оси Y
    .range([400, 0]); // Диапазон пикселей

// Создание точек на графике
svg.selectAll('circle')
    .data(data)
    .enter()
    .append('circle')
    .attr('cx', function (d) { return xScale(d.x); })
    .attr('cy', function (d) { return yScale(d.y); })
    .attr('r', 4)
    .attr('fill', 'steelblue');

// Расчет коэффициентов линейной регрессии
var regression = d3.regressionLinear()
    .x(function (d) { return d.x; })
    .y(function (d) { return d.y; });

var regressionData = regression(data);

// Создание линии линейной регрессии
var line = d3.line()
    .x(function (d) { return xScale(d[0]); })
    .y(function (d) { return yScale(d[1]); });

svg.append('path')
    .datum(regressionData)
    .attr('fill', 'none')
    .attr('stroke', 'red')
    .attr('stroke-width', 2)
    .attr('d', line(regressionData));