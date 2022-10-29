import array
from tkinter import *
from GameState import GameState
from Tabuleiro import Tabuleiro

class AtorJogador:
    def __init__(self):
        self._mainWindow = Tk()
        self._mainWindow.title("SHOBU - Game")
        self._mainWindow.geometry("1280x720")
        self._mainWindow.resizable(False, False)
        self._mainWindow["bg"] = "white"
        self.fillMainWindow()
        self._tabuleiro = Tabuleiro()
        self._mainWindow.mainloop()

    def fillMainWindow(self):

        #DIVISAO DOS FRAMES
        self._menuFrame = Frame(self._mainWindow, padx=0, pady=0,height=40,width=1280)
        self._menuFrame.grid(row=0,column=0,sticky="W")
        self._tableFrame = Frame(self._mainWindow,width=1080,height=720, bg="white",pady=14)
        self._tableFrame.grid(row=1,column=0)
        self._messageFrame = Frame(self._mainWindow,bg="red")
        self._messageFrame.grid(row=2, column=0,sticky="W")

        #PREENCHIMENTO DO FRAME MENU
        self._startGameLabel = Label(self._menuFrame,padx=230,pady=10,text="Iniciar Jogo",bg="white",fg="black",font="Times 20",borderwidth=2,relief="solid")
        self._startGameLabel.grid(row=0,column=0,sticky="NW",)
        self._startGameLabel.bind("<Button-1>", lambda event: self.startMatch(event))
        self._menuGameLogoLabel = Label(self._menuFrame,text="SHOBU", padx=277,pady=3,bg="white",fg="magenta",font="Arial 30",borderwidth=2,relief="solid")
        self._menuGameLogoLabel.grid(row=0,column=3, sticky="N")

        #PREENCHIMENTO DO FRAME DO TABULEIRO
        altura_quadrante = 292
        largura_quadrante = 352
        quadrante1 = Frame(self._tableFrame, bg="cyan", width=largura_quadrante, height=altura_quadrante,borderwidth=2,relief="solid")
        quadrante1.grid(row=0,column=0)
        quadrante2 = Frame(self._tableFrame, bg="cyan", width=largura_quadrante, height=altura_quadrante,borderwidth=2, relief="solid")
        quadrante2.grid(row=0,column=1)
        quadrante3 = Frame(self._tableFrame, bg="magenta", width=largura_quadrante, height=altura_quadrante,borderwidth=2, relief="solid")
        quadrante3.grid(row=1, column=0)
        quadrante4 = Frame(self._tableFrame, bg="magenta", width=largura_quadrante, height=altura_quadrante,borderwidth=2, relief="solid")
        quadrante4.grid(row=1, column=1)
        self.cyan_square_empty_image = PhotoImage(file="azul.png")
        self.pink_square_empty_image = PhotoImage(file="rosa.png")
        self.cyan_square_black_image = PhotoImage(file="azul_preta.png")
        self.cyan_square_white_image = PhotoImage(file="azul_branca_contorno.png")
        self.pink_square_black_image = PhotoImage(file="rosa_preta.png")
        self.pink_square_white_image = PhotoImage(file="rosa_branca_contorno.png")
        self._quadrante1 = []
        self._quadrante2 = []
        self._quadrante3 = []
        self._quadrante4 = []
        for x in range(4):
            a_column = []
            for y in range(4):
                aLabel = Label(quadrante1, bd=0, image=self.cyan_square_empty_image)
                aLabel.grid(row=x,column=y)
                aLabel.bind("<Button-1>",lambda event, seux=x, seuy=y, seuquadrante=0: self.clicarPosicao(event, seux, seuy,seuquadrante))
                a_column.append(aLabel)
            self._quadrante1.append(a_column)
        for x in range(4):
            a_column = []
            for y in range(4):
                aLabel = Label(quadrante2, bd=0, image=self.cyan_square_empty_image)
                aLabel.grid(row=x,column=y)
                aLabel.bind("<Button-1>",lambda event, seux=x, seuy=y, seuquadrante=1: self.clicarPosicao(event, seux, seuy,seuquadrante))
                a_column.append(aLabel)
            self._quadrante2.append(a_column)
        for x in range(4):
            a_column = []
            for y in range(4):
                aLabel = Label(quadrante3, bd=0, image=self.pink_square_empty_image)
                aLabel.grid(row=x,column=y)
                aLabel.bind("<Button-1>",lambda event, seux=x, seuy=y, seuquadrante=2: self.clicarPosicao(event, seux, seuy,seuquadrante))
                a_column.append(aLabel)
            self._quadrante3.append(a_column)
        for x in range(4):
            a_column = []
            for y in range(4):
                aLabel = Label(quadrante4, bd=0, image=self.pink_square_empty_image)
                aLabel.grid(row=x,column=y)
                aLabel.bind("<Button-1>", lambda event, seux=x, seuy=y, seuquadrante=3: self.clicarPosicao(event,seux,seuy,seuquadrante))
                a_column.append(aLabel)
            self._quadrante4.append(a_column)

        #PREENCHIMENTO DO FRAME DE MENSAGEM
        self._messageLabel = Label(self._messageFrame, bg="red", bd=0, text="Sem Jogo em Andamento",fg="white",padx=412,pady=5,font="Courier 30")
        self._messageLabel.grid(row=0, column=1,sticky="S")
    
    def atualizarInterface(self, gameState: GameState):
        mapa1 = gameState.getMap(0)
        for x in range(4):
            for y in range(4):
                if (mapa1[x][y] == 0):
                    self._quadrante1[x][y].configure(image=self.cyan_square_empty_image)
                if(mapa1[x][y] == 1):
                    self._quadrante1[x][y].configure(image=self.cyan_square_white_image)
                if(mapa1[x][y] == 2):
                    self._quadrante1[x][y].configure(image=self.cyan_square_black_image)
        mapa2 = gameState.getMap(1)
        for x in range(4):
            for y in range(4):
                if (mapa2[x][y] == 0):
                    self._quadrante2[x][y].configure(image=self.cyan_square_empty_image)
                if (mapa2[x][y] == 1):
                    self._quadrante2[x][y].configure(image=self.cyan_square_white_image)
                if (mapa2[x][y] == 2):
                    self._quadrante2[x][y].configure(image=self.cyan_square_black_image)
        mapa3 = gameState.getMap(2)
        for x in range(4):
            for y in range(4):
                if (mapa3[x][y] == 0):
                    self._quadrante3[x][y].configure(image=self.pink_square_empty_image)
                if (mapa3[x][y] == 1):
                    self._quadrante3[x][y].configure(image=self.pink_square_white_image)
                if (mapa3[x][y] == 2):
                    self._quadrante3[x][y].configure(image=self.pink_square_black_image)
        mapa4 = gameState.getMap(3)
        for x in range(4):
            for y in range(4):
                if(mapa4[x][y] == 0):
                    self._quadrante4[x][y].configure(image=self.pink_square_empty_image)
                if (mapa4[x][y] == 1):
                    self._quadrante4[x][y].configure(image=self.pink_square_white_image)
                if (mapa4[x][y] == 2):
                    self._quadrante4[x][y].configure(image=self.pink_square_black_image)
        if(gameState.getVezJogadorUm() == True):
            corDaVez = "BRANCAS"
        else:
            corDaVez = "PRETAS"
        if(gameState.getVencedor() != None):
            if(gameState.getVencedor().getCor() == 0):
                vencedor="BRANCAS"
            else:
                vencedor="PRETAS"
            self._messageLabel.configure(text="Jogador de {} venceu".format(vencedor),padx=400)
            if(vencedor=="BRANCAS"):
                self._messageLabel.configure(padx=364)
            else:
                self._messageLabel.configure(padx=376)
        elif(gameState.getMatchStatus()==0):
            self._messageLabel.configure(text="Sem Jogo em Andamento")
        elif(gameState.getMatchStatus()==1):
            self._messageLabel.configure(text="Clique 1 das {}".format(corDaVez),padx=424)
            if(corDaVez=="BRANCAS"):
                self._messageLabel.configure(padx=424)
            else:
                self._messageLabel.configure(padx=436)
        elif(gameState.getMatchStatus()==2):
            self._messageLabel.configure(text="Clique 2 das {}".format(corDaVez),padx=424)
            if(corDaVez=="BRANCAS"):
                self._messageLabel.configure(padx=424)
            else:
                self._messageLabel.configure(padx=436)
        elif(gameState.getMatchStatus()==3):
            self._messageLabel.configure(text="Agressiva das {}".format(corDaVez),padx=412)
            if(corDaVez=="BRANCAS"):
                self._messageLabel.configure(padx=412)
            else:
                self._messageLabel.configure(padx=424)


    def startMatch(self,event):
        self._tabuleiro.startMatch()
        gameState = self._tabuleiro.getGameState()
        self.atualizarInterface(gameState)

    def clicarPosicao(self,event,posX: int,posY: int,quadrante: int):
        matchStatus = self._tabuleiro.getMatchStatus()
        if(matchStatus==1 or matchStatus==2 or matchStatus==3):
            self._tabuleiro.clicarPosicao(posX,posY,quadrante)
            gameState = self._tabuleiro.getGameState()
            self.atualizarInterface(gameState)