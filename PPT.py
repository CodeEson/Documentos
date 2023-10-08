import random
import os

move_list = ["papel", "pedra", "tesoura"]
player_count = 0
computer_count = 0

print("==========")
print("Bem vindo ao jogo Pedra, Papel e Tesoura")


def main_print():
    print("==========")
    print("\nPlacar:")
    print("Voce: {}".format(player_count))
    print("Computador: {}".format(computer_count))
    print("\n")
    print("Escolha seu lance:")
    print("0- PAPEL | 1- PEDRA | 2 - TESOURA")

def select_movel():
    return random.choice(move_list)
    
def get_player_move():
    while True:
        try:
            player_move = int(input())
            if player_move not in [0,1,2]:
                raise
            return move_list[player_move]
        
        except Exception as e:
                print(e)

def select_winner(p_move, c_move):
        global player_count, computer_count
        if p_move == "papel":
            if c_move == "pedra":
                player_count += 1
                return "p"
            elif c_move == "tesoura":
                computer_count += 1
                return "c"               
            else: 
                return "d"
            
        if p_move == "pedra":
            if c_move == "tesoura":
                player_count += 1
                return "p"
            elif c_move == "papel":
                computer_count += 1
                return "c"               
            else: 
                return "d"

        if p_move == "tesoura":
            if c_move == "papel":
                player_count += 1
                return "p"
            elif c_move == "pedra":
                computer_count += 1
                return "c"               
            else: 
                return "d"        
            
again = 1
while again ==1:            
        main_print()
        player_move = get_player_move()
        computer_move = select_movel()
        winner = select_winner(player_move, computer_move)

        print("")
        print("==========")
        print("Sua jogada: {}".format(player_move.upper()))
        print("Jogada do computador: {}".format(computer_move.upper()))

        if winner == "p":
            print("Voce venceu")
        elif winner == "c":
            print("Voce perdeu")
        else:
            print("Empate")
            print("==========")

        while True:
            print("Jogar novamente: 0- SIM  |  1-NÃO")
            next = int(input()) 
            if next == 0:
                break
            elif next == 1:
                again = 0
                break
        os.system("clear")    