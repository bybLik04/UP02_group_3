// ��������� ��������� ������
var data = [];
var n = 100; // ���������� ����� ������

for (var i = 0; i < n; i++) {
    var x = Math.random() * 10;
    var y = 2 * x + Math.random() * 3; // ��������� �������� ���������: y = 2x + noise
    data.push({ x: x, y: y });
}

// �������� SVG-����������
var svg = d3.select('#chart')
    .attr('width', 400)
    .attr('height', 400);

// �������� ����� ��� ����
var xScale = d3.scaleLinear()
    .domain([0, 10]) // �������� �������� �� ��� X
    .range([0, 400]); // �������� ��������

var yScale = d3.scaleLinear()
    .domain([0, 30]) // �������� �������� �� ��� Y
    .range([400, 0]); // �������� ��������

// �������� ����� �� �������
svg.selectAll('circle')
    .data(data)
    .enter()
    .append('circle')
    .attr('cx', function (d) { return xScale(d.x); })
    .attr('cy', function (d) { return yScale(d.y); })
    .attr('r', 4)
    .attr('fill', 'steelblue');

// ������ ������������� �������� ���������
var regression = d3.regressionLinear()
    .x(function (d) { return d.x; })
    .y(function (d) { return d.y; });

var regressionData = regression(data);

// �������� ����� �������� ���������
var line = d3.line()
    .x(function (d) { return xScale(d[0]); })
    .y(function (d) { return yScale(d[1]); });

svg.append('path')
    .datum(regressionData)
    .attr('fill', 'none')
    .attr('stroke', 'red')
    .attr('stroke-width', 2)
    .attr('d', line(regressionData));