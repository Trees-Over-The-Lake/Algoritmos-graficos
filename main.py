import utils
from utils import *

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Trabalho Prático 1")

# Função genérica de desenha -> Serve apenas para ordenar a execução das funções de desenho
def draw(win, grid, buttons):
    win.fill(BG_COLOR)
    draw_grid(win, grid)

    # Desenhar todos os botões na tela
    for button in buttons:
        button.draw(win)

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

# Retorna se a função que está marcada é a de desenhar
def podeDesenhar(algoritmo) -> bool:
    return algoritmo == "DDA" or algoritmo == "Bresenham" or algoritmo == "Círculo"

# Inicializando configurações básicas do pygame
clock = pygame.time.Clock()   # Pegando um ponteiro para a função de clock do pygame
grid = utils.init_grid()  # Colorindo o grid da cor inicial
drawing_color = INVERTED_BG_COLOR  # Cor inicial de desenho

# Botões do programa
button_y = HEIGHT - TOOLBAR_HEIGHT/2 - 25     # Posição de início dos botões de baixo para cima
buttons = [
    Button(10, button_y, 50, 50, BLACK, WHITE, "DDA", BLACK),
    Button(70, button_y, 100, 50, RED, WHITE, "Bresenham", BLACK),
    Button(180, button_y, 60, 50, BLUE, WHITE, "Círculo", BLACK),
    Button(250, button_y, 130, 50, GREEN, WHITE, "Cohen Sutherland", BLACK),
    Button(390, button_y, 120, 50, WHITE, WHITE, "Liang Barsky", BLACK),
    Button(520, button_y, 60, 50, WHITE, WHITE, "Limpar", BLACK)
]

# Algoritmos de transformaç�o
transformacoes = [
    "Nenhum",
    "Translaç�o",
    "Rotaç�o",
    "Outro"
]

pos1 = (0, 0)  # Primeiro click do mouse
pos2 = (0, 0)  # Click do mouse quando selecionado segundo ponto
algorithm = "DDA"
ultimo_botao = buttons[0]  # Último botão clicado
trocar_cor_botao = buttons[0]  # Trocar a cor dos botões
transformacao = transformacoes[0]
line = Lines()
run = True
while run:
    # Selecionando os FPS
    clock.tick(FPS)

    # Loop principal do pygame para verificar ações do usuário
    for event in pygame.event.get():
        # Verificando se o usuário clicou o botão de sair do programa
        if event.type == pygame.QUIT:
            run = False

        # Pegando a posição do mouse na tela
        mousePos = pygame.mouse.get_pos()
        mousePosX, mousePosY = mousePos
        area_grid = True
        if HEIGHT - TOOLBAR_HEIGHT <= mousePosY:
            area_grid = False

        # Verificando se o botão esquerdo do mouse foi clicado
        if pygame.mouse.get_pressed()[0]:
            # Se o botão for clicado mudar algoritmo
            for button in buttons:
                if button.clicked(mousePos):
                    algorithm = button.text

                    # Trocar as cores dos botões
                    ultimo_botao.text_color = BLACK
                    button.text_color = GREEN
                    ultimo_botao = button

                    if podeDesenhar(button):
                        ultimo_botao = button

                    if button.text == 'Limpar':
                        line = Lines()
                        pos1 = (0, 0)
                        pos2 = (0, 0)
                        grid = init_grid()

        if pygame.mouse.get_pressed()[0] and area_grid and podeDesenhar(algorithm):
            pos1 = mousePos
            mousePosX, mousePosY = mousePos
            line.salvar_linhasX(mousePosX, mousePosY, ultimo_botao.text)
        elif pygame.mouse.get_pressed()[0] and area_grid:
            pos1 = mousePos

        if pygame.mouse.get_pressed()[2] and area_grid:
            pos2 = mousePos
            mousePosX, mousePosY = mousePos
            line.salvar_linhasY(mousePosX, mousePosY)

        # Eventos de teclado dentro do pygame
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LSHIFT:
                # Se o bot�o j� tiver sido clicado desliga-lo
                if transformacao == transformacoes[1]:
                    transformacao = transformacoes[0]

                else:
                    BG_COLOR = RED
                    transformacao = transformacoes[1]

            elif event.key == pygame.K_LCTRL:
                # Se o bot�o j� tiver sido clicado desliga-lo
                if transformacao == transformacoes[2]:
                    transformacao = transformacoes[0]

                else:
                    BG_COLOR = BLUE
                    transformacao = transformacoes[2]

            elif event.key == pygame.K_LALT:
                # Se o bot�o j� tiver sido clicado desliga-lo
                if transformacao == transformacoes[3]:
                    transformacao = transformacoes[0]

                else:
                    BG_COLOR = GREEN
                    transformacao = transformacoes[3]

    # Desenhando o backgorund na tela
    if transformacao == transformacoes[0]:
        BG_COLOR = WHITE

    # Desenhando os algoritmos na tela
    posX1, posY1 = pos1
    posX2, posY2 = pos2
    grid = utils.algorithms.draw_lines(grid, algorithm, posX1, posY1, posX2, posY2, BLACK, ROWS, PIXEL_SIZE, line)

    # Atualizar tela
    draw(WIN, grid, buttons)

pygame.quit()