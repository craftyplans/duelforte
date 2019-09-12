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

    def sim(self, ai):
        return (self.name, ai.play(self))

    
# A character can take an AI and become a simulation

class AI:
    def play(self, character):
        return None

class RandomAI(AI):
    def play(self, character):
        draw = random.sample(character.deck,
                             character.action_points)

        return [cards[d] for d in draw]
#

NPC = Character()

print(NPC.sim(RandomAI()))
