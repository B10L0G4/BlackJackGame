import random
import os # limpar tela 

def escolheNumJogador(): # pegar o numero de jogadores
    numero = [0,1,2,3]
    numJoadores = int(input('Quantos jogadores irão jogar nesta partida (1,2 ou 3): \n '))
    while numJoadores >=4:
        print('Números de jogadores invalido,você pode jogar com 1,2 ou 3 jogadores, tente novamente \n')
        numJoadores = int(input('Quantos jogadores irão jogar nesta partida (1,2 ou 3): \n '))
    else:
        if numJoadores in numero:     
            return(numJoadores)


# definir a quantidade de cartas
def distribuicartas():
    jogadores = escolheNumJogador() #verifica o numero de jogadores na partida
    jogadores += 1
    cropier = 0
    cartas = [1,2,3,4,5,6,7,8,9,10,'@','#','$','%','A']
    random.shuffle(cartas)# Embaralha as cartas

    if jogadores < 2 or jogadores > 4:
        print("Número inválido de jogadores. O jogo suporta de 1,2 ou 3 jogadores.")
    else:
        cartasJogadores = [[] for _ in range(jogadores -1)]  # Lista de listas para armazenar as cartas de cada jogador
        cropier = []
        for _ in range(2):  # Cada jogador recebe 2 cartas
            for jogador in cartasJogadores:
                carta = cartas.pop(0)  # Retira a carta do topo do baralho
                jogador.append(carta)  # Distribui a carta para cada jogador
    
            cartas_croupier = cartas.pop(0)  # A carta do croupier é a próxima do baralho
            cropier.append(cartas_croupier)  # Distribui a carta do croupier
        os.system("cls")
        for i, jogador in enumerate(cartasJogadores, start=1):
            print("Jogador", i, ":", jogador)
        print(f"Croupier: {cropier}")
        
        
distribuicartas()