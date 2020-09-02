##
# dental_rpg.py
# 24/08/20
# Anthony D


def character_select():
    """
    Lets the user select their character
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

    # Asks the user for their name
    username = input("Enter your name: ").lower().title().strip()
    while username == EMPTY:
        print("Please enter a name")
        username = input("Enter your name: ").lower().title().strip()
    print()

    # Function which displays all the characters and moves they have
    # available
    user_moveset = moveset(user_characters)

    # Asks the user to choose their character which they will use
    while not(choice in valid_input):
        choice = input("Please choose a character [1, 2, 3]: ")
    if choice == "1":
        user = "Toothbrush"
    elif choice == "2":
        user = "Floss"
    elif choice == "3":
        user = "Mouthwash"

    # Randomly rolls a character for the opponent
    roll = random.randint(0, 2)
    if roll == 0:
        opponent = "Plaque"
    elif roll == 1:
        opponent = "Bad Breath"
    elif roll == 2:
        opponent = "Cavities"        

    print("You have chosen: {}".format(user))
    characters = [user, opponent, username]
    return characters, user_moveset


def moveset(user_characters):
    """
    Displays the moves that each different character can use
    along with the damages
    """
    toothbrush_moveset = ["Mindless Brushing - 25 DMG",
                          "Back and Forth Strokes - 50 DMG",                          
                          "Circular Brushing Method - 60 DMG"]
    floss_moveset = ["Agressively Floss - 20 DMG",
                     "Gently Floss - 40 DMG",
                     "Carefully Floss with Great Technique - 50 DMG"]
    mouthwash_moveset = ["10 second Clean - 15 DMG",
                         "Gargle - 30 DMG",
                         "Swish - 50 DMG"]
    user_moveset = [toothbrush_moveset,
                    floss_moveset,
                    mouthwash_moveset]    
    character_moveset = {}

    for i in range(0, 3):
        character_moveset[user_characters[i]] = user_moveset[i]

    for character, moveset in sorted(character_moveset.items()):
        print("Character:", character)
        for moves in moveset:
            print("Move:", moves)
        print()
    return user_moveset


def ai_moveset():
    """
    AI moveset that will be used to combat the user's character
    """
    plaque_moveset = {"Yellowing" : 15,
                      "Discomfort" : 30,
                      "Tooth Decay" : 35}
    bad_breath_moveset = {"Stinky" : 10,
                          "Bacterial Growth" : 20,
                          "Ketone Buildup" : 25}
    cavities_moveset = {"Toothache" : 20,
                        "Infection" : 25,
                        "Tooth Loss" : 35}
    
    return plaque_moveset, bad_breath_moveset, cavities_moveset

    
def turns(characters, user_moveset):
    """
    Turns in between the character and the opponent where they
    can attack
    """
    import random
    success = True
    user_health = 100
    opponent_health = 100
    turn = 0
    start = "enter"
    
    print("Welcome {} the {}".format(characters[2], characters[0]))
    print("{} is about to ruin your teeth!".format(characters[1]))
    print()

    # Randomises who starts
    while start != "":
        start = input("Press ENTER to start: ")
    if start == "":
        print("===========")
        turn = random.randint(1, 2)
        while user_health > 0 and opponent_health > 0:
            if turn == 1:
                if characters[0] == "Toothbrush":
                    opponent_health = user_attack(characters, opponent_health)
                    turn = 2
                    print()
                elif characters[0] == "Floss":
                    opponent_health = user_attack(characters, opponent_health)
                    turn = 2
                    print()
                elif characters[0] == "Mouthwash":
                    opponent_health = user_attack(characters, opponent_health)
                    turn = 2
                    print()

            elif turn == 2:
                if characters[1] == "Plaque":
                    user_health = ai_attack(characters, user_health)
                    turn = 1
                    print()
                elif characters[1] == "Bad Breath":
                    user_health = ai_attack(characters, user_health)
                    turn = 1
                    print()
                elif characters[1] == "Cavities":
                    user_health = ai_attack(characters, user_health)
                    turn = 1
                    print()

    if user_health > opponent_health:
        print("{} wins! You have conquered dental problems :)".format(characters[0]))
    elif opponent_health > user_health:
        print("{} wins! You now have oral cancer :(".format(characters[1]))
        

def ai_attack(characters, user_health):
    """
    AI movesets they will use to attack the user's character
    """
    import random
    plaque_moveset, bad_breath_moveset, cavities_moveset = ai_moveset()
    
    if characters[1] == "Plaque":
        if user_health > 0:
            attack = random.randint(1, 3)
            if attack == 1:
                user_health -= plaque_moveset["Yellowing"]
                print("{} has used Yellowing!".format(characters[1]))
                print("{} is now at {} health".format(characters[0], user_health))
            elif attack == 2:
                user_health -= plaque_moveset["Discomfort"]
                print("{} has used Discomfort!".format(characters[1]))
                print("{} is now at {} health".format(characters[0], user_health))
            elif attack == 3:
                user_health -= plaque_moveset["Tooth Decay"]
                print("{} has used Tooth Decay!".format(characters[1]))
                print("{} is now at {} health".format(characters[0], user_health))

    elif characters[1] == "Bad Breath":
        if user_health > 0:
            attack = random.randint(1, 3)
            if attack == 1:
                user_health -= bad_breath_moveset["Stinky"]
                print("{} has used Stinky!".format(characters[1]))
                print("{} is now at {} health".format(characters[0], user_health))
            elif attack == 2:
                user_health -= bad_breath_moveset["Bacterial Growth"]
                print("{} has used Bacterial Growth!".format(characters[1]))
                print("{} is now at {} health".format(characters[0], user_health))
            elif attack == 3:
                user_health -= bad_breath_moveset["Ketone Buildup"]
                print("{} has used Ketone Buildup!".format(characters[1]))
                print("{} is now at {} health".format(characters[0], user_health))

    elif characters[1] == "Cavities":
        if user_health > 0:
            attack = random.randint(1, 3)
            if attack == 1:
                user_health -= cavities_moveset["Toothache"]
                print("{} has used Toothache!".format(characters[1]))
                print("{} is now at {} health".format(characters[0], user_health))
            elif attack == 2:
                user_health -= cavities_moveset["Infection"]
                print("{} has used Infection!".format(characters[1]))
                print("{} is now at {} health".format(characters[0], user_health))
            elif attack == 3:
                user_health -= cavities_moveset["Tooth Loss"]
                print("{} has used Tooth Loss!".format(characters[1]))
                print("{} is now at {} health".format(characters[0], user_health))
                
    return user_health
            

def user_attack(characters, opponent_health):
    """
    Attacking between the user and the opponent
    """
    loop = True
    toothbrush_moves = {"(1) Mindless Brushing" : 25,
                        "(2) Back and Forth Strokes" : 30,
                        "(3) Circular Brushing Method" : 35}
    floss_moves = {"(1) Agressively Floss" : 15,
                   "(2) Gently Floss" : 20,
                   "(3) Carefully Floss with Great Technique" : 30}
    mouthwash_moves = {"(1) 10 second Clean" : 10,
                       "(2) Gargle" : 25,
                       "(3) Swish" : 30}

    # If user uses Toothbrush then its moves will be used
    if characters[0] == "Toothbrush":
        for move, damage in sorted(toothbrush_moves.items()):
            print("{} - DMG: {}".format(move, damage))
        while loop == True:
            attack = input("Choose a move to use: [1, 2, 3]: ")
            print()
            if attack == "1":
                opponent_health -= toothbrush_moves["(1) Mindless Brushing"]
                print("{} has used Mindless Brushing!".format(characters[0]))
                print("{} is now at {} health".format(characters[1], opponent_health))
                loop = False
            elif attack == "2":
                opponent_health -= toothbrush_moves["(2) Back and Forth Strokes"]
                print("{} has used Back and Forth Strokes!".format(characters[0]))
                print("{} is now at {} health".format(characters[1], opponent_health))
                loop = False
            elif attack == "3":
                opponent_health -= toothbrush_moves["(3) Circular Brushing Method"]
                print("{} has used Circular Brushing Method!".format(characters[0]))
                print("{} is now at {} health".format(characters[1], opponent_health))
                loop = False

    # If user uses Floss then its moves will be used
    elif characters[0] == "Floss":
        for move, damage in sorted(floss_moves.items()):
            print("{} - DMG: {}".format(move, damage))
        print()
        while loop == True:
            attack = input("Choose a move to use: [1, 2, 3]: ")
            if attack == "1":
                opponent_health -= floss_moves["(1) Agressively Floss"]
                print("{} has used Agressively Floss!".format(characters[0]))
                print("{} is now at {} health".format(characters[1], opponent_health))
                loop = False
            elif attack == "2":
                opponent_health -= floss_moves["(2) Gently Floss"]
                print("{} has used Gently Floss!".format(characters[0]))
                print("{} is now at {} health".format(characters[1], opponent_health))
                loop = False
            elif attack == "3":
                opponent_health -= floss_moves["(3) Carefully Floss with Great Technique"]
                print("{} has used Carefully Floss with Great Technique!".format(characters[0]))
                print("{} is now at {} health".format(characters[1], opponent_health))
                loop = False

    # If user uses Mouthwash then its moves will be used
    elif characters[0] == "Mouthwash":
        for move, damage in sorted(mouthwash_moves.items()):
            print("{} - DMG: {}".format(move, damage))
        print()
        while loop == True:
            attack = input("Choose a move to use: [1, 2, 3]: ")
            if attack == "1":
                opponent_health -= mouthwash_moves["(1) 10 second Clean"]
                print("{} has used 10 second Clean!".format(characters[0]))
                print("{} is now at {} health".format(characters[1], opponent_health))
                loop = False
            elif attack == "2":
                opponent_health -= mouthwash_moves["(2) Gargle"]
                print("{} has used Gargle!".format(characters[0]))
                print("{} is now at {} health".format(characters[1], opponent_health))
                loop = False
            elif attack == "3":
                opponent_health -= mouthwash_moves["(3) Swish"]
                print("{} has used Swish!".format(characters[0]))
                print("{} is now at {} health".format(characters[1], opponent_health))
                loop = False

    return opponent_health
    

def main():
    print("Welcome to the Dental RPG")
    characters, user_moveset = character_select()
    print()
    turns(characters, user_moveset)
    print()
    print("Game Over")
