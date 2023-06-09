% rebase('layout.tpl', title=title, year=year)

<div class="page-layout">
	<div class="l">
		<div class="mainnav">
			<div class="calc-list">
				<a href="/plott"> 
					<img src="static\images\graph.png" alt="графический конструктор">
					<span>Графический конструктор</span>
				</a>
				<div class="separator"></div>
				<a class="nav-back"> 
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
								<div>
									<img id="result-image" src="{{image_data}}" alt="Результат графика">
								</div>
								<div class="text">
								<button id="toggleButton2">Теория</button>
									<form action="/approx1" method="post">
										<div class="approx">
											<input class="input1" id="fname" name="X" placeholder="Значение X, через пробел(пример '-')">
											<input class="input1" name="Y" placeholder="Значение Y, через пробел(пример '-')">
										</div>
										<div class="div-btns">
											<input type="submit" class="calc-btn" name='deg1_btn' value="Решить">
											<input type="submit" class="revcalc-btn" value="Пример">
										</div>
									</form>
								</div>
							</div>
						</div>
						<div class="ImageParagraph-section">
							<div class="solve-text">
								<label class="s">Решение:</label>
								<label class="solve">{{ex}}k = {{k}}, b = {{b}}, r2 = {{r}}</label>
								<div id="hiddenTextContainer2">
									<div id="hiddenText2"></div>
								</div>
							</div>
						</div>
					</div>
				</div>
			</div>
		</main>
	</div>
</div>

