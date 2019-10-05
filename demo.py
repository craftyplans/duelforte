from duel import duel
from characters import *

NPC1 = Character("AggroBaddy", AggroAI())

NPC2 = Character("RandoTank", RandomAI())
NPC2.hit_points = 7

opponents = {
    1: NPC1,
    2: NPC2
}

print("Choose your opponent (Enter number):\n1 : AggroBaddy\n2 : RandoTank")

opponent = opponents[int(input())]

PC = Character("Hero", HumanInput())
PC.deck.append(6)

winner = duel(opponent, PC)


#wins1 = 0
#wins2 = 0
#for i in range(30):
#    winner = duel(NPC1, NPC2)
#
#    if winner == NPC1:
#        wins1+=1
#
#    if winner == NPC2:
#        wins2+=1
#
#print(f"{NPC1.name} wins: {wins1}")
#print(f"{NPC2.name} wins: {wins2}")
