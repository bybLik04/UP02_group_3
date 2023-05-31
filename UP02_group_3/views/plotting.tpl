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
                                        <input class="input1" id="coefficients" name="coefficients" placeholder="Значение k" required>
                                        <input class="input1" id="coefficients" name="coefficients" placeholder="Значение a" required>
                                        <input class="input1" id="coefficients" name="coefficients" placeholder="Значение b" required>
                                        <input class="input1" id="coefficients" name="coefficients" placeholder="Значение c" required>
                                        <input class="input1" id="coefficients" name="coefficients" placeholder="Значение x" required>
                                        <input class="input1" id="length" name="length" placeholder="Начало отрезка" required>
                                        <input class="input1" id="length" name="length" placeholder="Конец отрезка" required>
                                    </div>
                                    <div>
                                        <input type="submit" class="calc-btn" value="Решить">
                                        <input type="submit" class="calc-btn" value="Теория по функциям">
                                    </div>
                                </form>
                            </div>
                        </div>
                    </div>
                    <div class="ImageParagraph-section">
                        <div>
                            <label class="solve-text">Решение:</label>
                            <label class="solve"></label>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </main>
</div>

</div>

