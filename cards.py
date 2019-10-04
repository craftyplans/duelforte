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
