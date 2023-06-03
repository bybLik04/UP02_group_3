% rebase('layout.tpl', title=title, year=year)

<div class="page-layout">
	<div class="l">
		<div class="mainnav">
			<div class="calc-list">
				<a class="nav-back"> 
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
								<img id="result-image" src="{{image_data}}" alt="Результат графика">
								<div class="text">
									<form action="/plott" method="post" id="myForm">
										<div class="approx">
											<select class="select1" id="function" name="function">
												<option value="selection">Выберите функцию: </option>
												<option value="linear">Линейная  y = kx+b</option>
												<option value="quadratic">Квадратичная  y = ax^2+bx+c</option>
												<option value="power">Степенная  y = x^a</option>
											</select>
											<input class="input1" id="k_coefficient" name="k_coefficient" placeholder="Значение k" required>
											<input class="input1" id="a_coefficient" name="a_coefficient" placeholder="Значение a" required>
											<input class="input1" id="b_coefficient" name="b_coefficient" placeholder="Значение b" required>
											<input class="input1" id="c_coefficient" name="c_coefficient" placeholder="Значение c" required>
											<input class="input1" id="x_value" name="x_value" placeholder="Значение x" required>
											<input class="input1" id="start_length" name="start_length" placeholder="Начало отрезка" required>
											<input class="input1" id="end_length" name="end_length" placeholder="Конец отрезка" required>
										</div>
										<div class="div-btns">
											<input id="calc"type="submit" class="calc-btn" onclick="handleFormSubmit(event)" value="Решить">
											<label id="ERROR" style="padding-left: 30px;">{{message}}</label>
										</div>
									</form>
								</div>
							</div>
						</div>
						<div class="ImageParagraph-section">
							<div class="solve-text">
								<label>Пояснение к функциям</label>
								<label class="solve-text">Линейная функция - это функция вида y = kx + b, где х - независимая переменная, k, b - некоторые числа. При этом k - угловой коэффициент, b - свободный коэффициент.</label>
								<label class="solve-text">Квадратичная функция - это функция вида y = ax^2 + bx + c, где x и y - переменные, a, b, c - заданные числа, обязательное условие - a ≠ 0.</label>
								<label class="solve-text">Cтепенная функция - это функция вида у=х^a, где a- любое действительное число.</label>
							</div>
						</div>
					</div>
				</div>
			</div>
		</main>
	</div>
</div>
