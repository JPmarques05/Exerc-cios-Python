import random
print("VAMOS JOGAR JOKENPÔ!!!")
print("PEDRA=0 \nPAPEL=1\nTESOURA=2")
print("FAÇA SUA ESCOLHA: ")
player=int(input())
print("VEZ DO COMPUTADOR: ")
pc=random.randint(0,2)
print(pc)
if player==2 and pc==1:
    print("O jogador jogou tesoura e o computador jogou papel!")
    print("JOGADOR VENCEU!!!")

elif player==0 and pc==1:
    print("O jogador jogou pedra e o computador jogou papel!")
    print("COMPUTADOR VENCEU")

elif player ==0 and pc ==2:
    print("O jogador jogou pedra e o computador jogou tesoura!")
    print("JOGADOR VENCEU!!!")

elif player==1 and pc==0:
    print("O jogador jogou papel e o computador jogou pedra!")
    print("JOGADOR VENCEU!!!")

elif player==1 and pc==2:
    print("O jogador jogou papel e o computador jogou tesoura!")
    print("COMPUTADOR VENCEU!!!")

elif player==2 and pc==0:
    print("O jogador jogou tesoura e o computador jogou pedra!")
    print("COMPUTADOR VENCEU!!!")

else: 
    print("O jogador e o computador fizeram escolhas iguais!")
    print("EMPATE!!!")





