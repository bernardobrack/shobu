class JogadaPassiva:
    def __init__(self):

        self._quadrante = 0
        self._xInicial = 0
        self._yInicial = 0
        self._deltaX = 0
        self._deltaY = 0

    def getQuadrante(self):
        return self._quadrante

    def getXInicial(self):
        return self._xInicial

    def getYInicial(self):
        return self._yInicial
        
    def getDeltaX(self):
        return self._deltaX

    def getDeltaY(self):
        return self._deltaY

    def setQuadrante(self, quadrantePassiva: int):
        self._quadrante = quadrantePassiva
    
    def setXInicial(self, xInicial: int):
        self._xInicial = xInicial

    def setYInicial(self, yInicial: int):
        self._yInicial = yInicial

    def setDeltaX(self, deltaX: int):
        self._deltaX = deltaX

    def setDeltaY(self, deltaY: int):
        self._deltaY = deltaY

    def getXFinal(self):
        return self._xInicial + self._deltaX

    def getYFinal(self):
        return self._yInicial + self._deltaY
