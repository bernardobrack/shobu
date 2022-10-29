class Clique:
    def __init__(self):

        self._quadrante = 0
        self._posX = 0
        self._posY = 0

    def registrarClique(self,posX: int,posY: int,quadrante: int):
        self._posX = posX
        self._posY = posY
        self._quadrante = quadrante

    def getQuadrante(self):
        return self._quadrante

    def getPosX(self):
        return self._posX

    def getPosY(self):
        return self._posY
