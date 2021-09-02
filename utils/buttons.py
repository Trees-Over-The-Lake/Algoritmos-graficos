from .settings import *

# Classe para definir botões
class Button:
    def __init__(self, x, y, width, height, color, text=None, text_color=BLACK):
        self.x = x
        self.y = y
        self.width = width
        self.heigth = height
        self.color = color
        self.text = text
        self.text_color = text_color

    # Desenhando o botão na tela
    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.heigth))
        pygame.draw.rect(win, INVERTED_BG_COLOR, (self.x, self.y, self.width, self.heigth), 2)

        # Se o texto existir
        if self.text:
            button_font = get_font(22)
            text_surface = button_font.render()

    #
    def clicked(self, pos):
        pass