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
    print(name, cards)

# A character has:
# - a name
# - a set of base hit points,
# - a number of action points, and
# - a deck.

class Character:
    name = "Steve"
    ai = None

    hit_points = 5
    action_points = 2

    deck = basic_deck

    def __init__(self,name, ai):
        self.name = name
        self.ai = ai

    def sim(self):
        return (self, self.ai.play(self))

    def take_hit(self):
        print(f"{self.name} takes a hit")
        self.hit_points -= 1

    def is_dead(self):
        return self.hit_points <= 0

    
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

        draw = random.choices(aggro_deck,
                              k=character.action_points)

        return draw
#

NPC1 = Character("RandoTank", RandomAI())
NPC1.hit_points = 7
NPC2 = Character("AggroHero", AggroAI())

### Combat rules
### One for each card.

def quick_attack_rule(target, target_hand):
    if 3 not in target_hand:
        target.take_hit()
    else:
        print(f"{target.name} blocks a Quick Attack")

def hard_attack_rule(target, target_hand):
    if 4 not in target_hand:
        target.take_hit()
    else:
        print(f"{target.name} blocks a Hard Attack")

def precise_attack_rule(target, target_hand):
    if 4 not in target_hand:
        target.take_hit()
    else:
        print(f"{target.name} blocks a Precise Attack")

rules = {
    0 : quick_attack_rule,
    1 : hard_attack_rule,
    2 : precise_attack_rule,
    3 : lambda x,y : None,
    4 : lambda x,y : None,
    5 : lambda x,y : None
}

def duel(character1, character2):
    ### Returns the winner

    while not character1.is_dead() and \
          not character2.is_dead():

        c1, d1 = character1.sim()
        c2, d2 = character2.sim()

        print_sim(c1, d1)
        print_sim(c2, d2)
        
        for d in d1:
            rules[d](c2,d2)

        for d in d2:
            rules[d](c1,d1)

    if character1.is_dead() and not character2.is_dead():
        print(f"{character1.name} is dead.")
        return character2
    elif character2.is_dead() and not character1.is_dead():
        print(f"{character2.name} is dead.")
        return character1
    else:
        print(f"Both characters are dead.")
        return None

winner = duel(NPC1, NPC2)

if winner:
    print(f"The winner is {winner.name}")

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
