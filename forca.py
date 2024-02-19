import random

def jogo():
    mensagem_inicial()
    palavra_secreta = gerar_palavra_secreta()
    letras_acertadas = ["_" for letra in palavra_secreta]
    print(letras_acertadas)

    enforcou = acertou = False
    chutes_errados = 0
    tentativas = 7

    while not enforcou and not acertou:
        chute = escolha_uma_letra()

        if chute in palavra_secreta:
            verifica_se_o_chute_esta_na_palavra_secreta(palavra_secreta, chute, letras_acertadas)
        else:
            chutes_errados = chutes_errados + 1
            tentativas = tentativas - 1
            if tentativas > 0:
                print(f"Você ainda possui {tentativas} tentativas")
            desenha_forca(chutes_errados)

        if chutes_errados == 7:
            enforcou = True
        if "_" not in letras_acertadas:
            acertou = True
        print(letras_acertadas)

    if acertou:
        mensagem_quando_ganhar()
    else:
        mensagem_quando_perder(palavra_secreta)


# ---------------------- # ------------------ # ------ FUNÇÕES ------- # -------------------- # ---------------


def mensagem_inicial():
    print("-------------------------------------")
    print("     Bem vindo ao jogo da Forca!     ")
    print("-------------------------------------")

def gerar_palavra_secreta():
    arquivo = open("palavras.txt", "r")
    nomes = []
    for linha in arquivo:
        linha = linha.strip()
        nomes.append(linha)
    arquivo.close()
    numero = random.randrange(0, len(nomes))
    palavra_secreta = nomes[numero].upper()
    return palavra_secreta

def escolha_uma_letra():
    chute = input("Escolha uma letra: ")
    chute = chute.strip().upper()
    return chute

def verifica_se_o_chute_esta_na_palavra_secreta(palavra_secreta, chute, letras_acertadas):
    index = 0
    for letra in palavra_secreta:
        if chute == letra:
            letras_acertadas[index] = letra
        index = index + 1

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

def mensagem_quando_ganhar():
    print("-------------------------------")
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")
    print("-------------------------------")

def mensagem_quando_perder(palavra_secreta):
    print("--------------------------------")
    print("Poxa, você foi enforcado! x.x")
    print(f"A palavra era [{palavra_secreta}]")
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")


if __name__ == "__main__":
    jogo()
