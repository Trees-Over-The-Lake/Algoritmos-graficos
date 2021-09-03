from .settings import *

# Selecionando o algoritmo para exibir na tela
def draw_lines(grid, algorithm, posX1, posY1, posX2, posY2, color, rows, pixel_size):
	# Não fazer nada se for a primeira iteração
	if posX1 > 0 and posX2 > 0 and posY1 > 0 and posY2 > 0:
		grid = init_grid()

		if algorithm == "DDA":
			grid = DDA(posX1, posY1, posX2, posY2, grid, color, rows, pixel_size)

		elif algorithm == "Brensenham":
			grid = bresenham(posX1, posY1, posX2, posY2, grid, color, rows, pixel_size)

		elif algorithm == "Linha":
			pass

		elif algorithm == "Círculo":
			pass

		elif algorithm == "Segundo Ponto":
			pass

		elif algorithm == "Limpar":
			return init_grid()

	# Se o grid estiver vazio retornar um grid vazio
	if not grid:
		grid = init_grid()
	return grid

# Transformando uma posição do pygame em uma posição do grid
def get_row_col_from_pos(pos, rows, pixel_size):
    x, y = pos
    row = x // pixel_size
    col = y // pixel_size

    # A posição passada não está dentro da área desenhavel
    if row >= rows:
        raise IndexError

    return col, row


# Inicializando o grid que será desenhado
def init_grid():
	grid = []

	for i in range(ROWS):
		grid.append([])
		for _ in range(COLS):
			grid[i].append(BG_COLOR)

	return grid

# Algoritmo DDA para escrever na tela
def DDA(posX1, posY1, posX2, posY2, grid, color, rows, pixel_size):
	dx = dy = passos = 0
	x = y = 0

	# Inicio do algoritmo
	dx = posX2 - posX1
	dy = posY2 - posY1

	if abs(dx) > abs(dy):
		passos = abs(dx)
	else:
		passos = abs(dy)

	# Desenhar no mesmo pixel
	if passos == 0:
		passos = 1

	x_incr = dx / passos
	y_incr = dy / passos
	x = posX1
	y = posY1

	# Verificar se o pixel clicado está dentro da tela
	try:
		draw_x, draw_y = get_row_col_from_pos((x, y), rows, pixel_size)
		grid[int(draw_x)][int(draw_y)] = color
	except IndexError:
		return grid

	for i in range(passos):
		x = x + x_incr
		y = y + y_incr

		# Verificar se o pixel clicado está dentro da tela
		try:
			draw_x, draw_y = get_row_col_from_pos((x, y), rows, pixel_size)
			grid[int(draw_x)][int(draw_y)] = color
		except IndexError:
			return None

	return grid

# Algoritmo de Brensenham para desenhar linha
def bresenham(x1, y1, x2, y2, grid, color, rows, pixel_size):
	dx, dy, x, y, p, const1, const2, passo_x, passo_y = 0, 0, 0, 0, 0, 0, 0, 0, 0

	# Calcular o delta X e delta y
	dx = abs(x2 - x1)
	dy = abs(y2 - y1)

	p = 2*dy - dx

	# Evitando uma divisão por zero
	if dx == 0:
		return

	# Calcular angulo da reta
	slope = dy / dx

	if slope >= 1:
		const1 = 2 * dx
		const2 = 2 * dx - 2 * dy
	else:
		const1 = 2 * dy
		const2 = 2 * dy - 2 * dx

	x = x1
	y = y1

	# Definindo a direção da reta
	if y2 > y1:
		passo_y = 1

	else:
		passo_y = -1

	grid = draw_in_grid(x, y, rows, pixel_size, grid, color)  # Desenhar no grid
	# Retornando da função se não for possível desenhar
	if not grid:
		return

	if x2 > x1:
		passo_x = x

		while x <= x2:
			grid = draw_in_grid(x, y, rows, pixel_size, grid, color)  # Desenhar no grid
			# Retornando da função se não for possível desenhar
			if not grid:
				return

			if slope >= 1:
				y = y + passo_y
			else:
				x = x + passo_x

			if p < 0:
				p = p + const1
			else:
				p = p + const2

				if slope >= 1:
					x = x + passo_x
				else:
					y = y + passo_y

	else:
		passo_x = -1

		# Desenhe a reta
		while x >= x2:
			grid = draw_in_grid(x, y, rows, pixel_size, grid, color)  # Desenhar no grid
			# Retornando da função se não for possível desenhar
			if not grid:
				return

			if slope >= 1:
				y = y + passo_y
			else:
				x = x + passo_x

			if p < 0:
				p = p + const1
			else:
				p = p + const2

				if slope >= 1:
					x = x + passo_x
				else:
					y = y + passo_y


	return grid


# Desenhar dentro do grid
def draw_in_grid(x, y, rows, pixel_size, grid, color):
	# Verificar se o pixel clicado está dentro da tela
	try:
		draw_x, draw_y = get_row_col_from_pos((x, y), rows, pixel_size)
		grid[int(draw_x)][int(draw_y)] = color
	except IndexError:
		return None

	return grid