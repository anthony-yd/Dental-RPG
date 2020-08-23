##
# dental_rpg.py
# 24/08/20
# Anthony D


def character_select():
    user = "Toothbrush"
    opponent = "Plaque"
    characters = [user, opponent]

    return characters


def turns(characters):
    loop = True
    success = True
    user_count = 0
    opponent_count = 0
    attack = ""
    print("Welcome")

    for i in range(3):
        attack = input("Press ENTER to attack: ")
        if attack == "":
            print("{} has successfully brushed away {}.".format(characters[0],characters[1]))
            success = True
            user_count += 1
        elif attack != "":
            print("{} was not able to brush away {}.".format(characters[0],characters[1]))
            success = False

        if success == False:
            print("{} has done damage to your teeth!".format(characters[1]))
            opponent_count += 1
        elif success == True:
            print("{} was not able to harm your teeth.".format(characters[1]))
        print()
    
    if user_count > opponent_count:
        print("{} wins!".format(characters[0]))
    elif user_count < opponent_count:
        print("{} wins!".format(characters[1]))
    print()

def main():
    characters = character_select()
    turns(characters)
    print("Game Over")
        

main()
