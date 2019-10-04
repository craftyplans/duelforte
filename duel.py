import cards as c

def name_cards(draw):
    return [c.cards[d] for d in draw]

def print_sim(character, play):
    name = character.name
    cards = name_cards(play)
    print(name, cards)

def duel(character1, character2):
    ### Returns the winner
    r = 0
    winner = None

    print(f"{character1.name} battles {character2.name}.")

    while not character1.is_dead() and \
          not character2.is_dead():

        r += 1
        print(f"Combat Round {r}")

        print(f"{character1.name} : {character1.hit_points} HP")
        print(f"{character2.name} : {character2.hit_points} HP")

        c1, d1 = character1.sim()
        c2, d2 = character2.sim()

        print_sim(c1, d1)
        print_sim(c2, d2)
        
        for d in d1:
            c.rules[d](c2,d2)

        for d in d2:
            c.rules[d](c1,d1)

        ## line break
        print("")

    if character1.is_dead() and not character2.is_dead():
        print(f"{character1.name} is dead.")
        winner = character2
    elif character2.is_dead() and not character1.is_dead():
        print(f"{character2.name} is dead.")
        winner = character1
    else:
        print(f"Both characters are dead.")

    if winner:
        print(f"The winner is {winner.name}.")

    return winner
