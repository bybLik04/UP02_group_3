% rebase('layout.tpl', title='Home Page', year=year)

<div class="page-layout">
	<div class="l">
		<div class="mainnav">
			<div class="calc-list">
				<a href="/plott"> 
					<img src="static\images\graph.png" alt="графический конструктор">
					<span>Графический конструктор</span>
				</a>
				<div class="separator"></div>
				<a href="/approx1"> 
					<img src="static\images\linear.png" alt="линейная регрессия">
					<span>Линейная регрессия</span>
				</a>
				<div class="separator"></div>
				<a href="/approx2"> 
					<img src="static\images\square.png" alt="квадратичная регрессия">
					<span>Квадратичная регрессия</span>
				</a>
			</div>
		</div>
	</div>
	<div id="main" class="m">
		<main>
			<div class="c">
				<div class="c0">
					<div class="mainpage">
						<div class="ImageParagraph-section">
							<div class="content">
								<canvas id="graph"></canvas>
								
								<div class="text">
									<h3 class="title">
										Графический конструктор
									</h3>
									<div class="paragraph">
										  Этот раздел предоставляет пользователю возможность выбрать из списка функцию для построения графика. 
										  Пользователь может настроить коэффициенты и отрезок, на котором будет строиться график.
										  <a href="https://translated.turbopages.org/proxy_u/en-ru.ru.137d177e-647639eb-c95273fb-74722d776562/https/www.statology.org/quadratic-regression-r/">Подробнее.</a>
									</div>
									<div>
										<a href="/plott" class="calc-btn">Решить</a>
									</div>
								</div>
							</div>
						</div>
						<div class="ImageParagraph-section">
							<div class="content">
								<div class="revtext">
									<h3 class="revtitle">
										Линейная регрессия
									</h3>
									<div class="revparagraph">
										В этом разделе используется метод наименьших квадратов для аппроксимации заданной 
										табличной функции с помощью линейного многочлена первой степени. 
										<a href="https://translated.turbopages.org/proxy_u/en-ru.ru.137d177e-647639eb-c95273fb-74722d776562/https/www.statology.org/quadratic-regression-r/">Подробнее.</a>
									</div>
								</div>
								<svg id="chart"></svg>
							</div>
						</div>
						<div class="ImageParagraph-section">
							<div class="content">
								<canvas id="square"></canvas>
								<div class="text">
									<h3 class="title">
										Квадратичная регрессия
									</h3>
									<div class="paragraph">
										В данном разделе применяется метод наименьших квадратов для аппроксимации 
										таблично заданной функции с помощью квадратичного многочлена второй степени. 
										<a href="https://translated.turbopages.org/proxy_u/en-ru.ru.137d177e-647639eb-c95273fb-74722d776562/https/www.statology.org/quadratic-regression-r/">Подробнее.</a>
									</div>
								</div>
							</div>
						</div>
					</div>
				</div>
			</div>
		</main>
	</div>
<div>
