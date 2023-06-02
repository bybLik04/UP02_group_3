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
				<a href="/approx1"> 
					<img src="static\images\linear.png" alt="линейная регрессия">
					<span>Линейная регрессия</span>
				</a>
				<div class="separator"></div>
				<a class="nav-back"> 
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
									<button id="toggleButton">Теория</button>
									<form action="/approx2" method="post">
										<div class="approx">
											<input class="input1" id="fname" name="X" placeholder="Значение X, через пробел" required>
											<input class="input1" name="Y" placeholder="Значение Y, через пробел" required>
										</div>
										<div class="div-btns">
											<input type="submit" class="calc-btn" value="Решить">
											<input type="submit" class="revcalc-btn" value="Пример">
										</div>
									</form>
									
								</div>
							</div>
						</div>
						<div class="ImageParagraph-section">
							<div class="solve-text">
								<label class="s">Решение:</label>
								<label class="solve"></label>
								<div id="hiddenTextContainer">
									<div id="hiddenText"></div>
								</div>
							</div>
						</div>
					</div>
				</div>
			</div>
		</main>
	</div>
</div>

