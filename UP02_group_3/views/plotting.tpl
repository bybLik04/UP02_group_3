% rebase('layout.tpl', title=title, year=year)

<div class="page-layout">
	<div class="l">
		<div class="mainnav">
			<div class="calc-list">
				<a style="background: #d7d7d7"> 
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
                                <form action="/approx1" method="post">
                                    <div class="approx">
                                        <select class="select1" id="function" name="function">
                                            <option value="linear">Линейная  y = kx+b</option>
                                            <option value="quadratic">Квадратичная  y = ax^2+bx+c</option>
                                            <option value="power">Степенная  y = x^a</option>
                                        </select>
                                        <label class="label-text">Если в вашей функции не используется какой то из коэффициентов, то поставьте знак "-"</label>
                                        <input class="input1" id="coefficients" name="coefficients" placeholder="Значение k" required>
                                        <input class="input1" id="coefficients" name="coefficients" placeholder="Значение a" required>
                                        <input class="input1" id="coefficients" name="coefficients" placeholder="Значение b" required>
                                        <input class="input1" id="coefficients" name="coefficients" placeholder="Значение c" required>
                                        <input class="input1" id="coefficients" name="coefficients" placeholder="Значение x" required>
                                        <input class="input1" id="length" name="length" placeholder="Начало отрезка" required>
                                        <input class="input1" id="length" name="length" placeholder="Конец отрезка" required>
                                    </div>
                                    <div class="div-btns">
                                        <input type="submit" class="calc-btn" value="Решить">
                                    </div>
                                </form>
                            </div>
                        </div>
                    </div>
                    <div class="ImageParagraph-section">
                        <div class="solve-text">
                            <label>Пояснение к функциям</label>
                            <label class="solve-text">Линейная функция - это функция вида y = kx + b, где х - независимая переменная, k, b - некоторые числа. При этом k - угловой коэффициент, b - свободный коэффициент.
                            </label>
                            <label class="solve-text">Квадратичная функция - это функция вида y = ax^2 + bx + c, где x и y - переменные, a, b, c - заданные числа, обязательное условие - a ≠ 0.
                            </label>
                            <label class="solve-text">Cтепенная функция - это функция вида у=х^a, где a- любое действительное число.</label>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </main>
</div>
</div>