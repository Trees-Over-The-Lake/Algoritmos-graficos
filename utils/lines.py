# Classe que armazena as posições do objeto da tela

class Lines:
    def __init__(self):
        self.pontoX1 = -1
        self.pontoY1 = -1
        self.pontoX2 = -1
        self.pontoY2 = -1
        self.algoritmo = "DDA"

    def salvar_linhasX(self, ponto1, ponto2, algoritmo):
        self.pontoX1 = ponto1
        self.pontoY1 = ponto2
        self.algoritmo = algoritmo

    def salvar_linhasY(self, ponto1, ponto2):
        self.pontoX2 = ponto1
        self.pontoY2 = ponto2