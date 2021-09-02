from utils import *

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Trabalho Prático 1")

# Função genérica de desenha -> Serve apenas para ordenar a execução das funções de desenho
def draw(win, grid):
    win.fill(BG_COLOR)
    draw_grid(win, grid)
    pygame.display.update()

# Desenhando os pixels dentro do grid
def draw_grid(win, grid):
    # Desenhando dentro do grid
    for i, row in enumerate(grid):
        for j, pixel in enumerate(row):
            pygame.draw.rect(win, pixel, (j * PIXEL_SIZE, i * PIXEL_SIZE, PIXEL_SIZE, PIXEL_SIZE))

    # Caso o usuário escolha querer ver os lugares que é possível desenhar
    if DRAW_GRID_LINES:
        # Desenhando na vertical
        for i in range(ROWS + 1):
            pygame.draw.line(win, INVERTED_BG_COLOR, (0, i * PIXEL_SIZE), (WIDTH, i * PIXEL_SIZE))
            
        # Desenhando na horizontal
        for i in range(COLS + 1):
            pygame.draw.line(win, INVERTED_BG_COLOR, (i * PIXEL_SIZE, 0), (i * PIXEL_SIZE, HEIGHT - TOOLBAR_HEIGHT))

# Inicializando o grid que será desenhado
def init_grid(rows, cols, color):
    grid = []

    for i in range(rows):
        grid.append([])
        for _ in range(cols):
            grid[i].append(color)
    
    return grid

# Transformando uma posição do pygame em uma posição do grid 
def get_row_col_from_pos(pos):
    x, y = pos
    row = x // PIXEL_SIZE
    col = y // PIXEL_SIZE

    # A posição passada não está dentro da área desenhavel
    if row >= ROWS:
        raise IndexError

    return row, col

# Inicializando configurações básicas do pygame
clock = pygame.time.Clock()            # Pegando um ponteiro para a função de clock do pygame
grid = init_grid(ROWS, COLS, BG_COLOR) # Colorindo o grid da cor inicial
drawing_color = INVERTED_BG_COLOR      # Cor inicial de desenho

run = True
while run:
    # Selecionando os FPS
    clock.tick(FPS)

    # Loop principal do pygame para verificar ações do usuário
    for event in pygame.event.get():
        # Verificando se o usuário clicou o botão de sair do programa
        if event.type == pygame.QUIT:
            run = False

        # Verificando se o botão esquerdo do mouse foi clicado
        if pygame.mouse.get_pressed()[0]:
            pos = pygame.mouse.get_pos()

            # Verificando se posição clicada pelo usuário é válida
            try:
                row, col = get_row_col_from_pos(pos)
                grid[col][row] = drawing_color # Desenhando na posição clicada

            # A posição clicada pelo usuário não é válida
            except IndexError:
                pass
    
    # Atualizar tela
    draw(WIN, grid)

pygame.quit()