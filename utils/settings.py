WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE  = (0, 0, 255)

FPS = 60

WIDTH, HEIGHT = 601, 700

ROWS = COLS = 50

TOOLBAR_HEIGHT = HEIGHT - WIDTH

PIXEL_SIZE = WIDTH // COLS

BG_COLOR = WHITE
INVERTED_BG_COLOR = BLACK

DRAW_GRID_LINES = True

def get_font(size):
    return pygame.font.SysFont("comicsans", size)