import random

# A card is ...
cards = {
    0 : 'Quick Attack',
    1 : 'Hard Attack',
    2 : 'Precise Attack',
    3 : 'Quick Block',
    4 : 'Hard Block',
    5 : 'Precise Attack'

}
# A deck is a set of cards

basic_deck = [0,1,2,3,4,5]

def name_cards(draw):
    return [cards[d] for d in draw]

def print_sim(character, play):
    name = character.name
    cards = name_cards(play)
    return name, cards

# A character has:
# - a name
# - a set of base hit points,
# - a number of action points, and
# - a deck.

class Character:
    name = "Steve"
    hit_points = 2
    action_points = 2

    deck = basic_deck

    def __init__(self,name):
        self.name = name

    def sim(self, ai):
        return (self, ai.play(self))

    
# A character can take an AI and become a simulation

class AI:
    def play(self, character):
        return None

class RandomAI(AI):
    def play(self, character):
        draw = random.sample(character.deck,
                             character.action_points)

        return draw

class AggroAI(AI):
    def play(self, character):
        attacks = [0,1,2]

        aggro_deck = [c for c in character.deck if c in attacks]

        draw = random.sample(aggro_deck,
                             character.action_points)

        return draw
#

NPC1 = Character("NPC1")
NPC2 = Character("NPC2")

print(print_sim(*NPC1.sim(RandomAI())))
print(print_sim(*NPC2.sim(AggroAI())))
