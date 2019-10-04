import cards as c

def name_cards(draw):
    return [c.cards[d] for d in draw]

def print_sim(character, play):
    name = character.name
    cards = name_cards(play)
    print(name, cards)

def duel(character1, character2):
    ### Returns the winner

    while not character1.is_dead() and \
          not character2.is_dead():

        c1, d1 = character1.sim()
        c2, d2 = character2.sim()

        print_sim(c1, d1)
        print_sim(c2, d2)
        
        for d in d1:
            c.rules[d](c2,d2)

        for d in d2:
            c.rules[d](c1,d1)

    if character1.is_dead() and not character2.is_dead():
        print(f"{character1.name} is dead.")
        return character2
    elif character2.is_dead() and not character1.is_dead():
        print(f"{character2.name} is dead.")
        return character1
    else:
        print(f"Both characters are dead.")
        return None
