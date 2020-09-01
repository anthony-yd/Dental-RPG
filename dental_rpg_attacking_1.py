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
    user_moveset = moves(user_characters)

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

    print("You have chosen {}".format(user))
    characters = [user, opponent, username]
    return characters, user_moveset


def moves(user_characters):
    """
    Displays the moves that each different character can use
    along with the damages
    """
    toothbrush_moveset = ["Mindless Brushing - 25 ATK",
                          "Back and Forth Strokes - 50 ATK",                          
                          "Circular Brushing Method - 60 ATK"]
    floss_moveset = ["Agressively Floss - 20 ATK",
                     "Gently Floss - 40 ATK",
                     "Carefully Floss with Great Technique - 50 ATK"]
    mouthwash_moveset = ["10 second Clean - 15 ATK",
                         "Gargle - 30 ATK",
                         "Swish - 50 ATK"]
    user_moveset = [toothbrush_moveset, floss_moveset, mouthwash_moveset]    
    character_moveset = {}

    for i in range(0, 3):
        character_moveset[user_characters[i]] = user_moveset[i]

    for character, moveset in sorted(character_moveset.items()):
        print("Character:", character)
        for moves in moveset:
            print("Move:", moves)
        print()
    return user_moveset
    
    
def turns(characters, user_moveset):
    """
    Turns in between the character and the opponent where they
    can attack
    """
    success = True
    user_count = 0
    opponent_count = 0
    attack = ""
    move_1 = {}
    move_2 = {}
    move_3 = {}

    # Starting health points for the user and the opponent
    user_health = 100
    opponent_health = 100
    
    print("Welcome {} the {}".format(characters[2], characters[0]))
    print("{} is about to ruin your teeth!".format(characters[1]))

    if characters[0] == "Toothbrush":
        moves = {"(1) Mindless Brushing" : 25,
                 "(2) Back and Forth Strokes" : 50,
                 "(3) Circular Brushing Method" : 60}
        for move, damage in sorted(moves.items()):
            print("Move: {} DMG: {}".format(move, damage))
        print()
        while opponent_health > 0:
            attack = input("Choose a move to use: [1, 2, 3]: ")
            if attack == "1":
                opponent_health -= 25
                print("{} is now at {}".format(characters[1], opponent_health))
                print()
            elif attack == "2":
                opponent_health -= 50
                print("{} is now at {}".format(characters[1], opponent_health))
                print()
            elif attack == "3":
                opponent_health -= 60
                print("{} is now at {}".format(characters[1], opponent_health))
                print()

# TURN INTO FUNCTION                    
"""
    elif characters[0] == "Floss":
        move_1 = {"(1) Agressively Floss" : 20}
        move_2 = {"(2) Gently Floss" : 40}
        move_3 = {"(3) Carefully Floss with Great Technique" : 50}
        print("Moves available: {}, {}, {}".format(move_1, move_2, move_3))
        while opponent_health > 0:
            attack = input("Choose a move to use: [1, 2, 3]: ")
            if attack == "1":
                opponent_health -= 20
                print("{} is now at {}".format(characters[1], opponent_health))
                print()
            elif attack == "2":
                opponent_health -= 40
                print("{} is now at {}".format(characters[1], opponent_health))
                print()
            elif attack == "3":
                opponent_health -= 50
                print("{} is now at {}".format(characters[1], opponent_health))
                print()


    elif characters[0] == "Mouthwash":
        move_1 = {"(1) 10 second Clean" : 25}
        move_2 = {"(2) Gargle" : 50}
        move_3 = {"(3) Swish" : 75}
        print("Moves available: {}, {}, {}".format(move_1, move_2, move_3))
        while opponent_health > 0:
            attack = input("Choose a move to use: [1, 2, 3]: ")
            if attack == "1":
                opponent_health -= 15
                print("{} is now at {}".format(characters[1], opponent_health))
                print()
            elif attack == "2":
                opponent_health -= 30
                print("{} is now at {}".format(characters[1], opponent_health))
                print()
            elif attack == "3":
                opponent_health -= 50
                print("{} is now at {}".format(characters[1], opponent_health))
                print()
"""

def main():
    characters, user_moveset = character_select()
    print()
    turns(characters, user_moveset)
    print("Game Over")
