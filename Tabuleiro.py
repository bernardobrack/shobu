import array
from Clique import Clique
from JogadaPassiva import JogadaPassiva
from Jogador import Jogador
from Quadrante import Quadrante
from GameState import GameState

class Tabuleiro:
    def __init__(self):
        self._jogador1 = Jogador()
        self._jogador2 = Jogador()
        self._jogador1.initialize(0)
        self._jogador2.initialize(1)
        self._quadrantes = []
        for x in range(2):
            linha = []
            for y in range(2):
                linha.append(Quadrante())
                linha[y].initialize(self._jogador1,self._jogador2)
            self._quadrantes.append(linha)
        self._primeiroClique = Clique()
        self._ultimaJogadaPassiva = JogadaPassiva()
        self.setMatchStatus(0)

    def startMatch(self):
        self._jogador1.setNaoVencedor()
        self._jogador2.setNaoVencedor()
        self.setMatchStatus(0)
        for a in range(4):
            quadranteObjeto = self.getQuadrante(a)
            quadranteObjeto.reiniciarContagemDePecas()
            quadranteObjeto.reiniciarPosicoes()
        self._jogador1.habilitarJogador()
        self.setMatchStatus(1)


    def setMatchStatus(self, status: int):
        self._matchStatus = status

    def getQuadrante(self,quadranteX: int,quadranteY: int):
        return self._quadrantes[quadranteX][quadranteY]

    def clicarPosicao(self,posX: int,posY: int,quadrante: int):
        jogadorDaVez = self.getJogadorDaVez()
        if(self.getMatchStatus()==1):
            quadranteValido = jogadorDaVez.isQuadranteProximo(quadrante)
            if(quadranteValido):
                quadranteObjeto = self.getQuadrante(quadrante)
                isPosicaoOcupadaPorDaVez = quadranteObjeto.isPosOcupadaPor(posX,posY,jogadorDaVez)
                if(isPosicaoOcupadaPorDaVez):
                    self._primeiroClique.registrarClique(posX,posY,quadrante)
                    self.setMatchStatus(2)
        elif(self.getMatchStatus()==2):
            quadranteObjeto = self.getQuadrante(quadrante)
            quadrantePrimeiroClique = self._primeiroClique.getQuadrante()
            if(quadrantePrimeiroClique == quadrante):
                xInicial = self._primeiroClique.getPosX()
                yInicial = self._primeiroClique.getPosY()
                ocupada = quadranteObjeto.isPosOcupada(posX,posY)
                if(not ocupada):
                    valido = quadranteObjeto.caminhoPassivoValido(xInicial,yInicial,posX,posY)
                    if(valido):
                        replicavel = self.passivaReplicavelEmAgressiva(xInicial,yInicial,posX,posY,quadrante)
                        if(replicavel):
                            self.efetuarJogadaPassiva(self._ultimaJogadaPassiva)
                        else:
                            self.setMatchStatus(1)
                    else:
                        self.setMatchStatus(1)
                else:
                    self.setMatchStatus(1)
            else:
                self.setMatchStatus(1)

        elif(self.getMatchStatus()==3):
            jogadaPassiva = self.getJogadaPassiva()
            quadrantePassiva = jogadaPassiva.getQuadrante()
            valido = self.quadranteAgressivaValido(quadrantePassiva,quadrante)
            if(valido):
                quadranteObjeto = self.getQuadrante(quadrante)
                ocupadaVez = self.isOcupadaPeloDaVez(posX,posY,quadranteObjeto)
                if(ocupadaVez):
                    agressivaPossivel = self.isAgressivaPossivelApartirDaPosicao(jogadaPassiva,quadrante,posX,posY,jogadorDaVez)
                    if(agressivaPossivel):
                        self.efetuarJogadaAgressiva(jogadaPassiva,posX,posY,quadrante)
                        haVencedor = self.haVencedor()
                        if(haVencedor):
                            self.finalizarPartida()
                        else:
                            self.inverterVezDosJogadores()
                            self.setMatchStatus(1)

    def getJogadorDaVez(self):
        vezJogadorUm = self._jogador1.isDaVez()
        if(vezJogadorUm):
            return self._jogador1
        return self._jogador2

    def getMatchStatus(self):
        return self._matchStatus

    def passivaReplicavelEmAgressiva(self,xInicialPassiva: int,yInicialPassiva: int,xFinalPassiva: int,yFinalPassiva: int,quadrantePassiva: int):
        self._ultimaJogadaPassiva.setQuadrante(quadrantePassiva)
        self._ultimaJogadaPassiva.setXInicial(xInicialPassiva)
        self._ultimaJogadaPassiva.setYInicial(yInicialPassiva)
        self._ultimaJogadaPassiva.setDeltaX(xFinalPassiva-xInicialPassiva)
        self._ultimaJogadaPassiva.setDeltaY(yFinalPassiva-yInicialPassiva)
        quadrantesValidos = self.getNumQuadrantesValidosParaAgressiva(quadrantePassiva)
        for a in range(2):
            quadranteObjeto = self.getQuadrante(quadrantesValidos[a])
            jogadorDaVez = self.getJogadorDaVez()
            possivel = quadranteObjeto.passivaReplicavelEmAgressiva(self._ultimaJogadaPassiva,jogadorDaVez)
            if(possivel):
                return True
        return False

    def efetuarJogadaPassiva(self, jogadaPassiva: JogadaPassiva):
        numQuadrante = jogadaPassiva.getQuadrante()
        xInicial = jogadaPassiva.getXInicial()
        yInicial = jogadaPassiva.getYInicial()
        xFinal = jogadaPassiva.getXFinal()
        yFinal = jogadaPassiva.getYFinal()
        jogadorDaVez = self.getJogadorDaVez()
        quadranteObjeto = self.getQuadrante(numQuadrante)
        quadranteObjeto.efetuarJogadaPassiva(xInicial,yInicial,xFinal,yFinal,jogadorDaVez)
        self.setMatchStatus(3)

    def getJogadaPassiva(self):
        return self._ultimaJogadaPassiva

    def quadranteAgressivaValido(self, quadrantePassiva: int,quadranteAgressiva: int):
        if(quadrantePassiva==0 or quadrantePassiva==1):
            return quadranteAgressiva == 2 or quadranteAgressiva == 3
        else:
            return quadranteAgressiva == 0 or quadranteAgressiva == 1
    
    def isOcupadaPeloDaVez(self,posX: int,posY: int,quadrante: Quadrante):
        jogadorDaVez = self.getJogadorDaVez()
        return quadrante.isPosOcupadaPor(posX,posY,jogadorDaVez)

    def isAgressivaPossivelApartirDaPosicao(self,jogadaPassiva: JogadaPassiva,quadranteAgressiva: int,xInicial: int,yInicial: int,jogadorDaVez: Jogador):
        quadranteObjeto = self.getQuadrante(quadranteAgressiva)
        return quadranteObjeto.isAgressivaPossivel(jogadaPassiva,xInicial,yInicial,jogadorDaVez)

    def getQuadrante(self, num: int):
        if num==0:
            return self._quadrantes[0][0]
        elif num == 1:
            return self._quadrantes[0][1]
        elif num == 2:
            return self._quadrantes[1][0]
        else:
            return self._quadrantes[1][1]

    def efetuarJogadaAgressiva(self,jogadaPassiva: JogadaPassiva,posX: int,posY: int,numQuadrante: int):
        jogadorDaVez = self.getJogadorDaVez()
        quadranteObjeto = self.getQuadrante(numQuadrante)
        quadranteObjeto.efetuarJogadaAgressiva(jogadaPassiva,posX,posY,jogadorDaVez)

    def haVencedor(self):
        for x in range(4):
            quadrante = self.getQuadrante(x)
            numBrancas = quadrante.getNumBrancas()
            numPretas = quadrante.getNumPretas()
            if (numBrancas == 0 or numPretas == 0):
                return True
        return False

    def getVencedor(self):
        if(self._jogador1.isVencedor()):
            return self._jogador1
        elif(self._jogador2.isVencedor()):
            return self._jogador2
        else:
            return None

    def finalizarPartida(self):
        jogador_da_vez = self.getJogadorDaVez()
        jogador_da_vez.setVencedor()
        self.setMatchStatus(0)

    def inverterVezDosJogadores(self):
        self._jogador1.inverterVezDoJogador()
        self._jogador2.inverterVezDoJogador()

    def getNumQuadrantesValidosParaAgressiva(self, quadrantePassiva: int):
        if(quadrantePassiva==0 or quadrantePassiva==1):
            return [2,3]
        else:
            return [0,1]

    def getGameState(self):
        game_state = GameState()
        game_state.setVezJogadorUm(self._jogador1.isDaVez())
        game_state.setMatchStatus(self.getMatchStatus())
        game_state.setVencedor(self.getVencedor())
        for x in range(4):
            quadrante = self.getQuadrante(x)
            map = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
            for i in range(4):
                for j in range(4):
                    jogador_pos = quadrante.getPos(i,j).getOcupante()
                    if(jogador_pos == self._jogador1):
                        map[i][j] = 1
                    elif(jogador_pos == self._jogador2):
                        map[i][j] = 2
            game_state.setMap(map,x)
        return game_state