##
# dental_rpg.py
# 24/08/20
# Anthony D


def character_select():
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
    
    print(user_characters)
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
    loop = True
    success = True
    user_count = 0
    opponent_count = 0
    attack = ""
    print("Welcome {} the {}".format(characters[2], characters[0]))
    print("{} is about to ruin your teeth!".format(characters[1]))

    for i in range(3):
        attack = input("Press ENTER to attack: ")
        if attack == "":
            print("{} has successfully cleaned away {}.".format(characters[0],characters[1]))
            success = True
            user_count += 1
        elif attack != "":
            print("{} was not able to clean away {}.".format(characters[0],characters[1]))
            success = False

        if success == False:
            print("{} has done damage to your teeth!".format(characters[1]))
            opponent_count += 1
        elif success == True:
            print("{} was not able to harm your teeth.".format(characters[1]))
        print()
    
    if user_count > opponent_count:
        print("{} wins! You have conquered dental problems :)".format(characters[0]))
    elif user_count < opponent_count:
        print("{} wins! You now have oral cancer :(".format(characters[1]))
    print()

def main():
    characters = character_select()
    print()
    turns(characters)
    print("Game Over")
