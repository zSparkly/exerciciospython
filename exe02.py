"""
crie um algoritmo que receba um número à ser advinhado por um jogador
se ele acertar parabenizá-lo pelo acerto caso contrário
diga que ele errou.

"""
import random
num = random.randrange(1,10)
print(num)

tentativas = 10

while resp == "s":
    chute = int(input("Chute um número de 1 a 10"))

    if num == chute:

        print("Parabéns!! vc acertou")
        resp="n"

    else:
        print("")
        print("Que burro da zero pra ele")
        tentativas= tentativas+1
        print("")
        cont = str(input("quer continuar? "))

