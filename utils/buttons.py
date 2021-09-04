from .settings import *
import pygame

# Classe para definir botões
class Button:
    def __init__(self, x, y, width, height, color, button_color, text=None, text_color=BLACK):
        self.x = x
        self.y = y
        self.width = width
        self.heigth = height
        self.color = color
        self.button_color = button_color
        self.text = text
        self.text_color = text_color

    # Desenhando o botão na tela
    def draw(self, win):
        pygame.draw.rect(win, self.button_color, (self.x, self.y, self.width, self.heigth))
        pygame.draw.rect(win, INVERTED_BG_COLOR, (self.x, self.y, self.width, self.heigth), 2)

        # Se o texto existir
        if self.text:
            button_font = get_font(15)
            text_surface = button_font.render(self.text, 1, self.text_color)
            # Procurando a posição em cima da esquerda de um pixel (0, 0) relativo a uma posição do grid
            win.blit(text_surface, (self.x + self.width/2 - text_surface.get_width()/2, 
                                    self.y + self.heigth/2 - text_surface.get_height()/2))

    # Returning if the button has been clicked
    def clicked(self, pos):
        x, y = pos

        if not (x >= self.x and x <= self.x + self.width):
            return False
        
        if not (y >= self.y and y <= self.y + self.heigth):
            return False

        return True