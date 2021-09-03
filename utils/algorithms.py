from .settings import *

# Selecionando o algoritmo para exibir na tela
def draw_lines(grid, algorithm, posX1, posY1, posX2, posY2, color, rows, pixel_size):
	# Não fazer nada se for a primeira iteração
	if posX1 > 0 and posX2 > 0 and posY1 > 0 and posY2 > 0:
		if algorithm == "DDA":
			grid = init_grid()
			grid = DDA(posX1, posY1, posX2, posY2, grid, color, rows, pixel_size)

		elif algorithm == "Brensenham":
			pass

		elif algorithm == "Linha":
			pass

		elif algorithm == "Círculo":
			pass

		elif algorithm == "Segundo Ponto":
			pass

		elif algorithm == "Limpar":
			return init_grid()

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
			return grid

	return grid

# Algoritmo de Brensenham para desenhar linha
def Brensenham(posX1, posY1, posX2, posY2, grid, color, rows, pixel_size):
	pass