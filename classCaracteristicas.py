import random
#Importando para haver a funcionalidade de jogada de um bot caso seja a opção de jogo selecionada

class Caracteristicas:
    #Atributos seriam as características da matriz e o nome/símbolo correspondente ao jogador da vez
    def __init__(self, i = 6, j = 7): 
        self.i = i
        self.j = j
        self.tabuleiro = []
        self.jogador_atual = 'X'
        self.njogadas = 0
        self.nmaximo = 42
        
        #Preenche com espaços vazios todos os elementos da matriz
        e = 0 
        while e < i:
            linha = [' '] * j
            self.tabuleiro.append(linha)
            e += 1

    #Serve para imprimir a o tabuleiro do jogo
    def print_estrutura(self): 
        for linha in self.tabuleiro:
            print('|', end=' ')
            for cell in linha:
                print(cell, end=' | ')
            print()
            print('+---+---+---+---+---+---+---+')

    #Verifica se espaço selecionado pelo jogador está disponível e preenche
    def fazer_jogada(self, coluna):
        linha = 5
        while linha >= 0 and linha <= 6:
            if self.tabuleiro[linha][coluna] == ' ':
                self.tabuleiro[linha][coluna] = self.jogador_atual
                return True
            linha -= 1
        return False
    
    #Verifica caso haja uma ganhador em todas as rodadas
    def verificar_vitoria(self):
        
        #Verificação horizontal
        linha = 0
        while linha < self.i:
            coluna = 0
            while coluna < self.j - 3:
                v1 = self.tabuleiro[linha][coluna] == self.jogador_atual  
                v2 = self.tabuleiro[linha][coluna + 1] == self.jogador_atual  
                v3 =  self.tabuleiro[linha][coluna + 2] == self.jogador_atual  
                v4 = self.tabuleiro[linha][coluna + 3] == self.jogador_atual
                if v1 and v2 and v3 and v4:
                    return True
                coluna += 1
            linha += 1
            
        #Verificação vertical
        linha = 0
        while linha < self.i - 3:
            coluna = 0
            while coluna < self.j:
                v1 = self.tabuleiro[linha][coluna] == self.jogador_atual 
                v2 = self.tabuleiro[linha + 1][coluna] == self.jogador_atual  
                v3 = self.tabuleiro[linha + 2][coluna] == self.jogador_atual 
                v4 = self.tabuleiro[linha + 3][coluna] == self.jogador_atual
                if  v1 and v2 and v3 and v4:
                    return True
                coluna += 1
            linha += 1

        #Verificação diagonal E => D
        linha = 0
        while linha < self.i - 3:
            coluna = 0
            while coluna < self.j - 3:
                v1 = self.tabuleiro[linha][coluna] == self.jogador_atual 
                v2 = self.tabuleiro[linha + 1][coluna + 1] == self.jogador_atual  
                v3 = self.tabuleiro[linha + 2][coluna + 2] == self.jogador_atual 
                v4 = self.tabuleiro[linha + 3][coluna + 3] == self.jogador_atual
                if v1 and v2 and v3 and v4:
                    return True
                coluna += 1
            linha += 1

        #Verificação diagonal D => E
        linha = 3
        while linha < self.i:
            coluna = 0
            while coluna < self.j - 3:
                v1 = self.tabuleiro[linha][coluna] == self.jogador_atual 
                v2 = self.tabuleiro[linha - 1][coluna + 1] == self.jogador_atual 
                v3 = self.tabuleiro[linha - 2][coluna + 2] == self.jogador_atual 
                v4 = self.tabuleiro[linha - 3][coluna + 3] == self.jogador_atual
                if v1 and v2 and v3 and v4:
                    return True
                coluna += 1
            linha += 1

    #Verifica empate com base no número máximo de jogadas por partida: 6 linhas * 7 colunas 
    def verificar_empate (self):
        if self.njogadas == self.nmaximo:
            return True
    
    #A vez é passada quando o nome/símbolo do jogador atual é alterado ao fim da rodada
    def trocar_jogador(self):
        if self.jogador_atual == 'X':
            self.jogador_atual = 'O'
        else:
            self.jogador_atual = 'X'

    #Define como será preenchido o tabuleiro na jogada do Bot
    def jogada_computador(self):
        coluna = random.randint(0, 6)
        while not self.fazer_jogada(coluna):
            coluna = random.randint(0, 6)
