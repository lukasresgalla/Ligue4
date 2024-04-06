from classCaracteristicas import Caracteristicas

#O jogo em si feito na sequência
class Jogo (Caracteristicas):
    def __init__ (self):
        super().__init__()
    
    #Método utilizado para iniciar o jogo
    def jogar(self):
        #Verificando se ninguém venceu 
        while not self.verificar_vitoria(): 
            
            print()
            self.print_estrutura()
            
            #Modo de 2 jogadores
            if modo == '2jogadores':
                coluna = int(input(f'Jogador {self.jogador_atual}, escolha uma coluna (0-6): '))
                while coluna < 0 or coluna > 6 or self.fazer_jogada(coluna) == False:
                    print('Jogada inválida. Tente novamente.')
                    coluna = int(input(f'Jogador {self.jogador_atual}, escolha uma coluna (0-6): '))
              
            #Modo de um jogador vs computador
            elif modo == 'Bot':
                if self.jogador_atual == 'X':
                    coluna = int(input(f'Jogador {self.jogador_atual}, escolha uma coluna (0-6): '))
                    while coluna < 0 or coluna > 6 or self.fazer_jogada(coluna) == False:
                        print('Jogada inválida. Tente novamente.')
                        coluna = int(input(f'Jogador {self.jogador_atual}, escolha uma coluna (0-6): '))
                        
                else:
                    print('Vez do Computador (O)')
                    self.jogada_computador()
                    if self.verificar_vitoria():
                        self.print_estrutura()
                        return 'O Computador venceu!'
             
            #Controle 
            self.njogadas += 1
            if self.verificar_vitoria():
                self.print_estrutura()
                print(f'Jogador {self.jogador_atual} venceu!')
                return False
            else:
                if self.verificar_empate():
                    print ('Empate')
                    return False
    
            self.trocar_jogador()
            
        
jogo = Jogo()
modo = input('Escolha o modo de jogo ==> 2jogadores ou Bot: ')
while modo != "2jogadores" and modo != "Bot":
    modo = input('Escolha o modo de jogo ==> 2jogadores ou Bot: ')
jogo.jogar()