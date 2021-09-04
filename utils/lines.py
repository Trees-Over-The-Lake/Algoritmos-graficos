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

    def toString(self):
        return 'PontoX1: ' + str(self.pontoX1) + ' PontoX2: ' + str(self.pontoX2) + ' PontoY1: ' + str(self.pontoY1) + ' PontoY2: ' + str(self.pontoY2) + ' algoritmo: ' + str(self.algoritmo)