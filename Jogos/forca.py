def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo de forca!***")
    print("*********************************")

    palavra_secreta = "banana".upper()
    letras_acertadas = ["_" for letra in palavra_secreta]

    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)

    while(not enforcou and not acertou):
        
        chute = input("Digite uma letra: ").strip().upper()
        print(" ")
   

        if (chute in palavra_secreta):
            posicao = 0
            for letra in palavra_secreta:
                if(chute == letra):
                    letras_acertadas[posicao] = letra.upper()
                posicao = posicao + 1
        
        else:
            erros += 1

        print(letras_acertadas)
        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        

    if(acertou):
        print("Voce ganhou!!!")
        print(" ")
    else:
        print("Voce perdeu!!!")
        print(" ")

    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar() 