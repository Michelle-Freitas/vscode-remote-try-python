from random import randint
#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------

# from flask import Flask
# app = Flask(__name__)

# @app.route("/")
# def hello():
#     return app.send_static_file("index.html")

#-----------------------------------------------------------------------------------------
def init_game():
    print("Jokenpô \n pedra \n papel \n tesoura")
    player_choice = input("Escolha sua jogada: ").strip().lower()

    if player_choice == "pedra" or player_choice == "papel" or player_choice == "tesoura":
        print ('ok')
    else:
        player_choice = ''
        print("jogada inválida - tente novamente")
        game()

    return player_choice


def computer_player():
    sorteio_computador = randint(1,3)
    if sorteio_computador == 1:
        pc = "pedra"
    elif sorteio_computador == 2:
        pc = "papel"
    elif sorteio_computador == 3:
        pc = "tesoura"
    return pc


def verify_winner(player, computer):
    if player == computer:
        print("Empate!")
    elif player == "pedra" and computer == "papel":
        print("PC ganhou - Papel embrulha a pedra")
    elif player == "pedra" and computer == "tesoura":
        print("Você ganhou - Pedra quebrou a tesoura")
    elif player == "papel" and computer == "pedra":
        print("Você ganhou - Papel embrulha a pedra")
    elif player == "papel" and computer == "tesoura":
        print("PC ganhou - Tesoura corta o papel")
    elif player == "tesoura" and computer == "pedra":
        print("PC ganhou - Pedra quebrou a tesoura")
    elif player == "tesoura" and computer == "papel":
        print("Você ganhou - Tesoura corta o papel")


def verify_play_again():
    play_again = input("Deseja jogar novamente? (s/n)").strip().lower()
    if play_again == "s":
        game()
    elif play_again == "n":
        print("Obrigado por jogar!")
        exit()
    else:
        print("Opção inválida - tente novamente")
        verify_play_again()


def game():
    computer = computer_player()
    player = init_game()
    print("Jogador: " + player)
    print("PC: " + computer)
    verify_winner(player, computer)
    verify_play_again()


game()
