import array


class Jogador:
    def __init__(self):

        self._cor = 0
        self._seuTurno = False
        self._vencedor = False
        self._quadrantesProximos = [0,0]

    def initialize(self, cor: int):
        self._cor = cor
        if(cor==0):
            self._quadrantesProximos = [0,2]
        else:
            self._quadrantesProximos = [1,3]
    def isDaVez(self):
        return self._seuTurno

    def habilitarJogador(self):
        self._seuTurno = True

    def desabilitarJogador(self):
        self._seuTurno = False

    def isQuadranteProximo(self, quadrante: int):
        if(self._quadrantesProximos[0] == quadrante or self._quadrantesProximos[1] == quadrante):
            return True
        return False

    def setVencedor(self):
        self._vencedor = True
        self._seuTurno = False

    def inverterVezDoJogador(self):
        vez = self.isDaVez()
        if(vez):
            self.desabilitarJogador()
        else:
            self.habilitarJogador()

    def isVencedor(self):
        return self._vencedor

    def getCor(self):
        return self._cor

    def setNaoVencedor(self):
        self._vencedor = False
