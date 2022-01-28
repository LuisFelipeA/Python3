def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo de forca!***")
    print("*********************************")

    palavra_secreta = "felipe"
    letras_acertadas = ["_","_","_","_","_","_"]

    enforcou = False
    acertou = False

    print(letras_acertadas)

    while(not enforcou and not acertou):
        
        chute = input("Digite uma letra: ").strip()

        posicao = 0
        for letra in palavra_secreta:
            if(chute.upper() == letra.upper()):
                letras_acertadas[posicao] = letra.upper()
            posicao = posicao + 1
        
        print(letras_acertadas)
        
        print("Jogando...")



    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar() 