# Feito por João Pedro Plinta

import random
import os
from colorama import Fore, Back, Style


def imprimir_tabuleiro(tabuleiro):
    os.system('cls' if os.name == 'nt' else 'clear') # Limpa a tela do console
    print(Back.WHITE + Fore.BLACK + '    ' + '   '.join([f'{i} ' for i in range(len(tabuleiro))]) + Style.RESET_ALL) # Imprime a numeração das colunas
    for i, linha in enumerate(tabuleiro):
        print(Back.WHITE + Fore.BLACK + f'{i}  ' + Style.RESET_ALL + Back.RESET + ' | '.join(linha) + ' |') # Imprime a linha do tabuleiro, unindo os elementos com ' | ' entre eles

        if i != len(tabuleiro)-1:
            print(Back.WHITE + Fore.BLACK + '   ' + '-' * (4 * len(linha) - 1) + Style.RESET_ALL) # Imprime uma linha de separação com base no tamanho da linha do tabuleiro

def verificar_vencedor(tabuleiro, jogador):
    tamanho = len(tabuleiro)
    # Verifica linhas e colunas
    for i in range(tamanho):
        if all(tabuleiro[i][j] == jogador for j in range(tamanho)):
            return True
        if all(tabuleiro[j][i] == jogador for j in range(tamanho)):
            return True
    # Verifica diagonais
    if all(tabuleiro[i][i] == jogador for i in range(tamanho)):
        return True
    if all(tabuleiro[i][tamanho - i - 1] == jogador for i in range(tamanho)):
        return True
    return False

def obter_jogadas_validas(tabuleiro):
    tamanho = len(tabuleiro) # Obtém o tamanho do tabuleiro
    jogadas_validas = [] # Inicializa uma lista vazia para armazenar as jogadas válidas
    for i in range(tamanho):
        for j in range(tamanho):
            if tabuleiro[i][j] == ' ': # Verifica se a posição atual está vazia
                jogadas_validas.append((i, j)) # Se estiver vazia, adiciona a jogada válida na lista
    return jogadas_validas # Retorna a lista de jogadas válidas
    
def obter_jogada_jogador(tabuleiro):
    while True: # Continua pedindo uma jogada até que seja válida
        try:
            jogada = input(Fore.CYAN + 'Digite a posição (linha, coluna): ' + Style.RESET_ALL) # Solicita ao jogador uma jogada
            linha, coluna = map(int, jogada.split(',')) # Divide a jogada em linha e coluna
            if tabuleiro[linha][coluna] == ' ': # Verifica se a posição está vazia
                return linha, coluna # Retorna a linha e coluna escolhidas pelo jogador
            else:
                print(Fore.RED + 'Posição inválida. Tente novamente.' + Style.RESET_ALL) # Exibe uma mensagem de erro se a posição já estiver ocupada
        except (ValueError, IndexError): # Captura erros de conversão de tipo ou índice fora do intervalo
            print(Fore.RED + 'Entrada inválida. Tente novamente.' + Style.RESET_ALL) # Exibe uma mensagem de erro se a entrada não for válida

def obter_jogada_computador(tabuleiro):
    jogadas_validas = obter_jogadas_validas(tabuleiro) # Obtém as jogadas válidas no tabuleiro
    return random.choice(jogadas_validas) # Escolhe aleatoriamente uma das jogadas válidas

def jogar(size, modo):
    tabuleiro = [[' ' for _ in range(size)] for _ in range(size)]
    jogadores = ['X', 'O']

    if modo == '1':
        print('Modo: Jogador vs. Jogador')
    elif modo == '2':
        print('Modo: Jogador vs. Computador')
    else:
        print('Modo inválido. Encerrando o jogo.')
        return

    jogador_atual = 0
    jogo_terminado = False

    while not jogo_terminado:
        imprimir_tabuleiro(tabuleiro)
        print(Fore.BLUE + f"É a vez do jogador {jogadores[jogador_atual]}" + Style.RESET_ALL)

        if modo == '1' or (modo == '2' and jogador_atual == 0):
            linha, coluna = obter_jogada_jogador(tabuleiro)
        else:
            linha, coluna = obter_jogada_computador(tabuleiro)
            print(Fore.BLUE + f"A máquina jogou: {linha}, {coluna}" + Style.RESET_ALL)

        tabuleiro[linha][coluna] = jogadores[jogador_atual]

        if verificar_vencedor(tabuleiro, jogadores[jogador_atual]):
            imprimir_tabuleiro(tabuleiro)
            print(f"Parabens❗ 🎉 o jogador {jogadores[jogador_atual]} venceu!")
            jogo_terminado = True
        elif all(tabuleiro[i][j] != ' ' for i in range(size) for j in range(size)):
            imprimir_tabuleiro(tabuleiro)
            print("Empate!")
            jogo_terminado = True

        jogador_atual = (jogador_atual + 1) % 2


def principal():
    print(Fore.BLUE +"Bem-vindo ao Jogo da Velha!" + Style.RESET_ALL)

    while True:
        print(Fore.MAGENTA + "Escolha o tamanho do tabuleiro:" + Style.RESET_ALL)
        print(Fore.MAGENTA + "1. 3x3" + Style.RESET_ALL)
        print(Fore.MAGENTA + "2. 5x5" + Style.RESET_ALL)
        print(Fore.MAGENTA + "3. 7x7" + Style.RESET_ALL)
        print(Fore.MAGENTA + "4. 9x9" + Style.RESET_ALL)
        print(Fore.MAGENTA + "0. Sair" + Style.RESET_ALL)

        escolha = input(Fore.CYAN + "Digite o número da opção desejada: " + Style.RESET_ALL)

        if escolha == '0':
            print(Fore.BLUE + "Até logo!" + Style.RESET_ALL)
            break

        if escolha in ['1', '2', '3', '4']:
            modo = input(Fore.CYAN + "Escolha o modo de jogo (1 - Jogador vs. Jogador, 2 - Jogador vs. Computador): " + Style.RESET_ALL)
            if modo in ['1', '2']:
                tamanho = int(escolha) * 2 + 1
                jogar(tamanho, modo)
            else:
                print(Fore.RED + "Modo inválido. Tente novamente." + Style.RESET_ALL)
        else:
            print(Fore.RED + "Opção inválida. Tente novamente." + Style.RESET_ALL)

if __name__ == "__main__":
    principal()