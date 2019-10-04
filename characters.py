import cards as c
import random

def name_cards(draw):
    return [c.cards[d] for d in draw]

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

    deck = c.basic_deck

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


##################


# A character can take an AI and become a simulation

class AI:
    def play(self, character):
        return None

class HumanInput(AI):
    def play(self, character):
        draw = []
        for a in range(character.action_points):
            available_cards = set(character.deck) - set(draw)
            print(f"Cards Available: {available_cards}")

            action = None
            while action is None:
                print("Choose a card for your action:")
                try:
                    action = int(input())
                except:
                    print("Invalid choice.")

            draw.append(action)

        return draw           

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
