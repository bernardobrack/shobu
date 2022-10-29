import array
from JogadaPassiva import JogadaPassiva
from Jogador import Jogador
from Posicao import Posicao


class Quadrante:
    def __init__(self):
        self._posicoes = []
        for i in range(4):
            linha = []
            for j in range(4):
                linha.append(Posicao())
            self._posicoes.append(linha)
        self._numPretas = 4
        self._numBrancas = 4

    def initialize(self, jogador1: Jogador, jogador2: Jogador):
        for i in range(4):
            for j in range(4):
                if (j == 0):
                    self.getPos(i,j).initialize(jogador1)
                elif (j == 3):
                    self.getPos(i,j).initialize(jogador2)
                else:
                    self.getPos(i,j).initialize(None)

    def reiniciarContagemDePecas(self):
        self._numBrancas = 4
        self._numPretas = 4

    def reiniciarPosicoes(self):
        for i in range(4):
            for j in range(4):
                self._posicoes[i][j].reiniciarPosicao()


    def getPos(self, x: int, y: int):
        return self._posicoes[x][y]

    def isPosOcupadaPor(self,posX: int,posY: int,jogador: Jogador):
        pos = self.getPos(posX,posY)
        if (pos.getOcupante() == jogador):
            return True
        else:
            return False


    def isPosOcupada(self, posX: int, posY: int):
        pos = self.getPos(posX,posY)
        return pos.isOcupada()

    def caminhoPassivoValido(self,xInicial: int,yInicial: int,xFinal: int,yFinal: int):
        moduloDeltaX = self.calcularModuloDelta(xFinal,xInicial)
        moduloDeltaY = self.calcularModuloDelta(yFinal,yInicial)
        if(moduloDeltaX == 0 and moduloDeltaY == 0):
            return False
        if(moduloDeltaX != 0 and moduloDeltaY != 0 and moduloDeltaX != moduloDeltaY):
            return False
        deltaX = self.calcularDelta(xFinal,xInicial)
        deltaY = self.calcularDelta(yFinal,yInicial)
        xAuxiliar = xInicial
        yAuxiliar = yInicial
        ocupada = False
        while((deltaX != 0 or deltaY != 0) and (ocupada == False)):
            if(deltaX > 0 and deltaY < 0):
                xAuxiliar+=1
                yAuxiliar-=1
                posicao = self.getPos(xAuxiliar,yAuxiliar)
                ocupada = posicao.isOcupada()
            elif(deltaX > 0 and deltaY == 0):
                xAuxiliar += 1
                posicao = self.getPos(xAuxiliar,yAuxiliar)
                ocupada = posicao.isOcupada()
            elif(deltaX > 0 and deltaY > 0):
                xAuxiliar+=1
                yAuxiliar+=1
                posicao = self.getPos(xAuxiliar,yAuxiliar)
                ocupada = posicao.isOcupada()
            elif(deltaX == 0 and deltaY < 0):
                yAuxiliar-=1
                posicao = self.getPos(xAuxiliar,yAuxiliar)
                ocupada = posicao.isOcupada()
            elif(deltaX == 0 and deltaY > 0):
                yAuxiliar+=1
                posicao = self.getPos(xAuxiliar,yAuxiliar)
                ocupada = posicao.isOcupada()
            elif(deltaX < 0 and deltaY < 0):
                xAuxiliar-=1
                yAuxiliar-=1
                posicao = self.getPos(xAuxiliar,yAuxiliar)
                ocupada = posicao.isOcupada()
            elif(deltaX < 0 and deltaY == 0):
                xAuxiliar-=1
                posicao = self.getPos(xAuxiliar,yAuxiliar)
                ocupada = posicao.isOcupada()
            elif(deltaX < 0 and deltaY > 0):
                xAuxiliar-=1
                yAuxiliar+=1
                posicao = self.getPos(xAuxiliar,yAuxiliar)
                ocupada = posicao.isOcupada()
            if(deltaX > 0):
                deltaX-=1
            elif(deltaX < 0):
                deltaX+=1
            if(deltaY > 0):
                deltaY-=1
            elif(deltaY < 0):
                deltaY +=1
        return (not ocupada)

    def efetuarJogadaAgressiva(self,jogadaPassiva: JogadaPassiva,posX: int,posY: int,jogadorDaVez: Jogador,):
        posicaoInicial = self.getPos(posX,posY)
        posicaoInicial.desocuparPosicao()
        deltaX = jogadaPassiva.getDeltaX()
        deltaY = jogadaPassiva.getDeltaY()
        xFinal = posX + deltaX
        yFinal = posY + deltaY
        pecasInimigas = self.haPecaInimigaNoCaminho(posX,posY,xFinal,yFinal,jogadorDaVez)
        if(pecasInimigas):
            posPecaInimiga = self.getPecaInimigaNoCaminho(posX,posY,xFinal,yFinal,jogadorDaVez)
            jogadorInimigo = posPecaInimiga.getOcupante()
            posPecaInimiga.desocuparPosicao()
            xFinalMaisUm = xFinal
            yFinalMaisUm = yFinal
            if(deltaX>0):
                xFinalMaisUm+=1
            elif(deltaX<0):
                xFinalMaisUm-=1
            if(deltaY>0):
                yFinalMaisUm+=1
            elif(deltaY<0):
                yFinalMaisUm-=1
            posFinalMaisUmNosLimites = self.isNosLimites(xFinalMaisUm,yFinalMaisUm)
            if(posFinalMaisUmNosLimites):
                posFinalMaisUm = self.getPos(xFinalMaisUm,yFinalMaisUm)
                posFinalMaisUm.ocuparPosicao(jogadorInimigo)
            else:
                corInimigo = jogadorInimigo.getCor()
                if(corInimigo==0):
                    self._numBrancas-=1
                else:
                    self._numPretas-=1
        ultimaPos = self.getPos(xFinal,yFinal)
        ultimaPos.ocuparPosicao(jogadorDaVez)

    def calcularModuloDelta(self, coordenadaFinal: int, coordenadaInicial: int):
        return abs(coordenadaFinal - coordenadaInicial)

    def calcularDelta(self, coordenadaFinal: int, coordenadaInicial: int):
        return coordenadaFinal - coordenadaInicial

    def passivaReplicavelEmAgressiva(self,ultimaJogadaPassiva: JogadaPassiva,jogadorDaVez: Jogador):
        agressivaPossivel = False
        for x in range(4):
            for y in range(4):
                if(agressivaPossivel):
                    return True
                ocupadaDaVez = self.isPosOcupadaPor(x,y,jogadorDaVez)
                if(ocupadaDaVez):
                    agressivaPossivel = self.isAgressivaPossivel(ultimaJogadaPassiva,x,y,jogadorDaVez)

    def isAgressivaPossivel(self,ultimaJogadaPassiva: JogadaPassiva,xInicial: int,yInicial: int,jogadorDaVez: Jogador):
        deltaX = ultimaJogadaPassiva.getDeltaX()
        deltaY = ultimaJogadaPassiva.getDeltaY()
        nosLimites = self.isNosLimites(xInicial+deltaX,yInicial+deltaY)
        if(nosLimites):
            haPecaDaVezNoCaminho = self.haPecaJogadorDaVezNoCaminho(xInicial,yInicial,xInicial+deltaX,yInicial+deltaY,jogadorDaVez)
            if(haPecaDaVezNoCaminho):
                return False
            haPecaInimiga = self.haPecaInimigaNoCaminho(xInicial,yInicial,xInicial+deltaX,yInicial+deltaY,jogadorDaVez)
            if(haPecaInimiga):
                pecasInimigas = self.contarPecasInimigasNoCaminho(xInicial,yInicial,xInicial+deltaX,yInicial+deltaY,jogadorDaVez)
                if(pecasInimigas>1):
                    return False
                if(deltaX>0):
                    xFinalMaisUm = xInicial+deltaX+1
                elif(deltaX<0):
                    xFinalMaisUm = xInicial+deltaX-1
                else:
                    xFinalMaisUm = xInicial+deltaX
                if (deltaY > 0):
                    yFinalMaisUm = yInicial + deltaY + 1
                elif (deltaY < 0):
                    yFinalMaisUm = yInicial + deltaY - 1
                else:
                    yFinalMaisUm = yInicial + deltaY
                posMaisUmNosLimites = self.isNosLimites(xFinalMaisUm,yFinalMaisUm)
                if(posMaisUmNosLimites):
                    posMaisUm = self.getPos(xFinalMaisUm,yFinalMaisUm)
                    posMaisUmOcupada = posMaisUm.isOcupada()
                    if(posMaisUmOcupada):
                        return False
                    else:
                        return True
                return True
            return True
        return False




    def isNosLimites(self, x: int, y: int):
        if (x>=0 and x<4):
            if (y>=0 and y<4):
                return True
            return False
        return False

    def haPecaInimigaNoCaminho(self,xInicial: int,yInicial: int,xFinal: int,yFinal: int,jogadorDaVez: Jogador):
        deltaX = xFinal-xInicial
        deltaY = yFinal-yInicial
        xAuxiliar = xInicial
        yAuxiliar = yInicial
        while(deltaX != 0 or deltaY != 0):
            if(deltaX > 0):
                xAuxiliar+=1
                deltaX-=1
            elif(deltaX < 0):
                xAuxiliar-=1
                deltaX+=1
            if(deltaY > 0):
                yAuxiliar+=1
                deltaY-=1
            elif(deltaY < 0):
                yAuxiliar-=1
                deltaY+=1
            posicao = self.getPos(xAuxiliar,yAuxiliar)
            ocupada = posicao.isOcupada()
            if(ocupada):
                ocupadaPorDaVez = posicao.isPosOcupadaPor(jogadorDaVez)
                if(not ocupadaPorDaVez):
                    return True
        return False

    def contarPecasInimigasNoCaminho(self,xInicial: int,yInicial: int,xFinal: int,yFinal: int,jogadorDaVez: Jogador):
        deltaX = xFinal - xInicial
        deltaY = yFinal - yInicial
        xAuxiliar = xInicial
        yAuxiliar = yInicial
        auxiliarContagem = 0
        while (deltaX != 0 or deltaY != 0):
            if (deltaX > 0):
                xAuxiliar += 1
                deltaX -= 1
            elif (deltaX < 0):
                xAuxiliar -= 1
                deltaX += 1
            if (deltaY > 0):
                yAuxiliar += 1
                deltaY -= 1
            elif (deltaY < 0):
                yAuxiliar -= 1
                deltaY += 1
            posicao = self.getPos(xAuxiliar, yAuxiliar)
            ocupada = posicao.isOcupada()
            if (ocupada):
                ocupadaPorDaVez = posicao.isPosOcupadaPor(jogadorDaVez)
                if (not ocupadaPorDaVez):
                    auxiliarContagem+=1
        return auxiliarContagem

    '''No diagrama de classes o yFinal tem tipo unt kkkkkkkkkkkkkkkkkkkkkkkk'''
    def haPecaJogadorDaVezNoCaminho(self,xInicial: int,yInicial: int,xFinal: int,yFinal: int,jogadorDaVez: Jogador):
        deltaX = xFinal - xInicial
        deltaY = yFinal - yInicial
        xAuxiliar = xInicial
        yAuxiliar = yInicial
        while (deltaX != 0 or deltaY != 0):
            if (deltaX > 0):
                xAuxiliar += 1
                deltaX -= 1
            elif (deltaX < 0):
                xAuxiliar -= 1
                deltaX += 1
            if (deltaY > 0):
                yAuxiliar += 1
                deltaY -= 1
            elif (deltaY < 0):
                yAuxiliar -= 1
                deltaY += 1
            posicao = self.getPos(xAuxiliar, yAuxiliar)
            ocupada = posicao.isOcupada()
            if (ocupada):
                ocupadaPorDaVez = posicao.isPosOcupadaPor(jogadorDaVez)
                if (ocupadaPorDaVez):
                    return True
        return False

    def efetuarJogadaPassiva(self,xInicial: int,yInicial: int,xFinal: int,yFinal: int,jogadorDaVez: Jogador):
        posInicial = self.getPos(xInicial,yInicial)
        posInicial.desocuparPosicao()
        posFinal = self.getPos(xFinal,yFinal)
        posFinal.ocuparPosicao(jogadorDaVez)

    def getPecaInimigaNoCaminho(self,xInicial: int,yInicial: int,xFinal: int,yFinal: int,jogadorDaVez: Jogador):
        deltaX = xFinal - xInicial
        deltaY = yFinal - yInicial
        xAuxiliar = xInicial
        yAuxiliar = yInicial
        while deltaX != 0 or deltaY != 0:
            if(deltaX>0):
                xAuxiliar = xAuxiliar + 1
                deltaX = deltaX - 1
            elif(deltaX<0):
                xAuxiliar -= 1
                deltaX +=1
            if(deltaY>0):
                yAuxiliar+=1
                deltaY+=1
            elif(deltaY<0):
                yAuxiliar-=1
                deltaY+=1
            posicao = self.getPos(xAuxiliar,yAuxiliar)
            ocupada = posicao.isOcupada()
            if(ocupada):
                OcupadaPorDaVez = posicao.isPosOcupadaPor(jogadorDaVez)
                if(not OcupadaPorDaVez):
                    return posicao
        return None


    def getNumBrancas(self):
        return self._numBrancas

    def getNumPretas(self):
        return self._numPretas
