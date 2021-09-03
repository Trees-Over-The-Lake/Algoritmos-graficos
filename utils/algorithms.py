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
	# Swap dos elementos para sempre ter X1 sendo menor X2
	if x1 > x2:
		x1, x2 = x2, x1
	if y1 > y2:
		y1, y2 = y2, y1

	m_new = 2 * (y2 - y1)
	slope_error_new = m_new - (x2 - x1)

	y = y1
	for x in range(x1, x2 + 1):
		# Verificar se o pixel clicado está dentro da tela
		try:
			draw_x, draw_y = get_row_col_from_pos((x, y), rows, pixel_size)
			grid[int(draw_x)][int(draw_y)] = color
		except IndexError:
			return None

		# Add slope to increment angle formed
		slope_error_new = slope_error_new + m_new

		# Slope error reached limit, time to
		# increment y and update slope error.
		if (slope_error_new >= 0):
			y = y + 1
			slope_error_new = slope_error_new - 2 * (x2 - x1)

	return grid