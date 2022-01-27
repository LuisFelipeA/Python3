import forca
import adivinhacao


def escolha_jogo():
    print("*********************************")
    print("*********Escolha um jogo!********")
    print("*********************************")

    print("[1] Forca [2]Advinhação")

    jogo = int(input("Qual jogo quer jogar? "))

    if(jogo == 1):
        print("forca")
        forca.jogar()
    elif(jogo == 2):
        print("Adivinhação")
        adivinhacao.jogar()

if(__name__ == "__main__"):
    escolha_jogo()