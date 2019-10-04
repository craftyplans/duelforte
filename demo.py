from duel import duel
from characters import *

NPC1 = Character("RandoTank", RandomAI())
NPC1.hit_points = 7
NPC2 = Character("AggroHero", AggroAI())

PC = Character("Hero", HumanInput())

winner = duel(NPC1, PC)


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
