from Jogador import Jogador

class Posicao:
    def __init__(self):

        self._ocupante = None
        self._ocupanteInicial = None

    def initialize(self, jogador: Jogador):
        self._ocupante = jogador
        self._ocupanteInicial = jogador
    def reiniciarPosicao(self):
        self._ocupante = self._ocupanteInicial

    def isPosOcupadaPor(self, jogador: Jogador):
        return self._ocupante == jogador

    def isOcupada(self):
        return self._ocupante != None

    def desocuparPosicao(self):
        self._ocupante = None

    def ocuparPosicao(self, jogador: Jogador):
        self._ocupante = jogador

    def getOcupante(self):
        return self._ocupante
