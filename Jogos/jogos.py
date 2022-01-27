import forca
import adivinhacao



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