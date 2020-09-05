##
# dental_rpg.py
# 24/08/20
# Anthony D


def character_select():
    """
    Function which allows the user to select their character
    """
    import random
    roll = 0
    EMPTY = ""
    choice = ""
    username = ""
    user = ""
    opponent = ""
    valid_input = ["1", "2", "3"]
    user_characters = ["(1) Toothbrush", "(2) Floss", "(3) Mouthwash"]

    username = input("Enter your name: ").lower().title().strip()
    while username == EMPTY:
        print("Please enter a name")
        username = input("Enter your name: ").lower().title().strip()
    
    for character in user_characters:
        print(character)
    while not(choice in valid_input):
        choice = input("Please choose a character: ")
    if choice == "1":
        user = "Toothbrush"
    elif choice == "2":
        user = "Floss"
    elif choice == "3":
        user = "Mouthwash"

    roll = random.randint(0, 2)
    if roll == 0:
        opponent = "Plaque"
    elif roll == 1:
        opponent = "Bad Breath"
    elif roll == 2:
        opponent = "Cavities"        

    print("You have chosen {}".format(user))
    characters = [user, opponent, username]
    return characters


def turns(characters):
    """
    Function which starts the turns between the user
    and opponent
    """
    stats = []
    user_rounds = 0
    opponent_rounds = 0
    attack = ""
    user_health = 100
    opponent_health = 100
    health_difference = 0

    turn = 1
    print("Welcome {} the {}".format(characters[2], characters[0]))
    print("{} is about to ruin your teeth!".format(characters[1]))
    print()
    print("=================")
    
    while user_health > 0 and opponent_health > 0:
        if turn == 1:
            attack = input("Press ENTER to attack: ")
            if attack == "":
                opponent_health, health_difference = user_attack(opponent_health)
                print("{} has cleaned {} for {} health.".format(characters[0],
                                                                characters[1],
                                                                health_difference))
                user_rounds += 1
                turn = 2
                print()
                
            elif attack != "":
                print("{} was not able to clean {}.".format(characters[0],
                                                            characters[1]))
                turn = 2
                print()
                
        elif turn == 2:
            user_health, health_difference = opponent_attack(user_health)
            print("{} has done {} damage to your teeth!".format(characters[1],
                                                                health_difference))
            opponent_rounds += 1
            turn = 1
            print()

            
        print("{} is now on {} health".format(characters[1],
                                              opponent_health))
        print("{} is now on {} health".format(characters[0],
                                              user_health))
        print("=================")

    stats = [user_health, user_rounds, opponent_health, opponent_rounds]
    return stats


def end_dialogue(characters, stats):
    if stats[0] > stats[2]:
        print("{} has lasted against {} for {} rounds".format(characters[1],
                                                           characters[0],
                                                           stats[3]))
        print("{} wins! You have conquered dental problems :)".format(characters[0]))
    elif stats[0] < stats[2]:
        print("{} has lasted against {} for {} rounds".format(characters[0],
                                                           characters[1],
                                                           stats[1]))
        print("{} wins! You now have oral cancer :(".format(characters[1]))
    print()


def user_attack(opponent_health):
    import random
    attack_point = 0

    attack_point = random.randint(0, 25)
    opponent_health -= attack_point
    difference = attack_point

    return opponent_health, difference
    

def opponent_attack(user_health):
    import random
    attack_point = 0

    attack_point = random.randint(0, 25)
    user_health -= attack_point
    difference = attack_point

    return user_health, difference
    

def main():
    characters = character_select()
    print()
    stats = turns(characters)
    print()
    end_dialogue(characters, stats)
    print("Game Over")
