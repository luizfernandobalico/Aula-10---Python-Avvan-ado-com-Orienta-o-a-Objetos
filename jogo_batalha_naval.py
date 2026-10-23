import random

tabuleiro = ["~"] * 10
navio = random.randint(0, 9)

print("🚢 BATALHA NAVAL 🚢")

for tentativa in range(3):
    posicao = int(input("Escolha uma posição (0-9): "))

    if posicao == navio:
        print("🎯 Acertou o navio!")
        break
    elif posicao < navio:
        print("O navio está mais à direita!")
    else:
        print("O navio está mais à esquerda!")

else:
    print("💥 Você perdeu! O navio estava na posição", navio)
#🎮 Como funciona
#O computador esconde um navio em uma posição de 0 a 9.
#Você tem 3 tentativas.
#O programa informa se o navio está à direita ou à esquerda.
#Se acertar, você vence!