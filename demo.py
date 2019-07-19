import random

# A card is ...

QUICK_ATTACK = 0
HARD_ATTACK = 1
PRECISE_ATTACK = 2

QUICK_BLOCK = 3
HARD_BLOCK = 4
PRECISE_ATTACK = 5
 
# A deck is a set of cards

basic_deck = [0,1,2,3,4,5]


# A character has a set of base hit points, a number of action points, and a deck.

class Character:
    hit_points = 2
    action_points = 2

    deck = basic_deck

    def sim(self, ai):
        return ai.play(self)

    
# A character can take an AI and become a simulation

class AI:
    def play(self, character):
        return None

class RandomAI(AI):
    def play(self, character):
        return random.sample(character.deck,
                             character.action_points)

#

NPC = Character()

print(NPC.sim(RandomAI()))
