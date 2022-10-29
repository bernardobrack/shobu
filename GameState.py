import array
from Jogador import Jogador


class GameState:
    def __init__(self):

        self._vezjogador1 = False
        self._map0 = []
        self._map1 = []
        self._map2 = []
        self._map3 = []
        self._matchStatus = 0
        self._vencedor = None

    def setMatchStatus(self, matchStatus: int):
        self._matchStatus = matchStatus

    def getMatchStatus(self):
        return self._matchStatus

    def setVencedor(self, jogador: Jogador):
        self._vencedor = jogador

    def getVencedor(self):
        return self._vencedor

    def setMap(self, map: [], number: int):
        if(number==0):
            self._map0 = map
        elif(number==1):
            self._map1 = map
        elif (number == 2):
            self._map2 = map
        elif (number == 3):
            self._map3 = map
    def getMap(self, number: int):
        if (number == 0):
            return self._map0
        if (number == 1):
            return self._map1
        if (number == 2):
            return self._map2
        if (number == 3):
            return self._map3

    def setVezJogadorUm(self, vez: bool):
        self._vezjogador1 = vez

    def getVezJogadorUm(self):
        return self._vezjogador1
