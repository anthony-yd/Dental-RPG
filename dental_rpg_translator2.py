##
# dental_rpg.py
# 24/08/20
# Anthony D


def force_number(question):
    """
    Function which error checks user number inputs so they
    are a valid number and not a string/word
    """
    while True:
        try:
            number = int(input(question))
            break
        except ValueError:
            print("\nEnter a number not a word or letter")
    return number


def menu():
    """
    Menu function which allows user to choose
    what they would like to do
    """
    choice = 0
    translate = False
    valid_input = [1, 2, 3]

    print("Welcome to Dental RPG")
    while not (choice in valid_input):
        choice = force_number("""Please choose an option:
(1) Start game in English
(2) Start game in Te Reo
(3) Quit
> """)
        print()
    
    if choice == 1:
        characters = character_select(translate)
        health, ai_health = quiz(characters, translate)
        end(characters, health, ai_health, translate)        
        
    elif choice == 2:
        translate = True
        characters = character_select(translate)
        health, ai_health = quiz(characters, translate)
        end(characters, health, ai_health, translate)        

    elif choice == 3:
        quit


def character_select(translate):
    """
    Allows the user to select their character
    Also rolls a random character for the user
    """
    # variables that will be used
    import random
    roll = 0
    EMPTY = ""
    choice = 0
    username = ""
    user = ""
    opponent = ""
    characters = ["(1) Toothbrush", "(2) Floss", "(3) Mouthwash"]
    characters_te_reo = ["(1) Paraihe niho", "(2) Miro", "(3) Horoi horoi mangai"]
    valid_input = [1, 2, 3]

    # asks user for name and error checks it
    if translate == False:
        username = input("Enter your name\n> ").lower().title().strip()
    elif translate == True:
        username = input("Enter your ingoa\n> ").lower().title().strip()
    while username == EMPTY:
        print("Please enter a name/ingoa")
        username = input("> ").lower().title().strip()

    # asks the user to input their favored
    # character
    print()
    if translate == False:
        for character in characters:
            print(character)
        
        choice = force_number("Please choose a character\n> ")
        if choice == 1:
            user = "Toothbrush"
        elif choice == 2:
            user = "Floss"
        elif choice == 3:
            user = "Mouthwash"
            
    elif translate == True:
        for character in characters_te_reo:
            print(character)
            
        choice = force_number("Please choose a pūāhua\n> ")
        if choice == 1:
            user = "Paraihe niho"
        elif choice == 2:
            user = "Miro"
        elif choice == 3:
            user = "Horoi horoi mangai"
        

    # randomly rolls a character that will
    # be used by the ai
    roll = random.randint(0, 2)
    if translate == False:
        if roll == 0:
            opponent = "Plaque"
        elif roll == 1:
            opponent = "Bad Breath"
        elif roll == 2:
            opponent = "Cavities"
            
    elif translate == True:
        if roll == 0:
            opponent = "Kaupapa"
        elif roll == 1:
            opponent = "Manawa kino"
        elif roll == 2:
            opponent = "Rongonui"  

    print("You have chosen {}\n".format(user))
    characters = [user, opponent, username]
    return characters


def quiz(characters, translate):
    """
    Runs a quiz which the user will play
    """
    questions = {"How long should you brush your teeth?\n(1) 1 minute\n(2) 2 minutes\n> ": 2,
                 "What is mouthwash most effective against?\n(1) Bad breath\n(2) Cavities\n> ": 1,
                 "How long should your floss be before using?\n(1) 46 cm\n(2) 41 cm\n> ": 1,
                 "What causes tooth decay?\n(1) Acid\n(2) Caffeine\n> ": 1,
                 "What is Halitosis the medical term for?\n(1) Black hairy tongue\n(2) Bad breath\n> ": 2,
                 "What is the best way prevent gum disease?\n(1) Remove plaque\n(2) Flouride toothpaste\n> ": 1,
                 "When should toothbrushes be replaced?\n(1) 2 to 3 months\n(2) 4 to 5 months\n> ": 1}
    questions_translated = {"How long should you PARAIHE/brush your NIHO/teeth?\n(1) 1 meneti\n(2) 2 meneti\n> ": 2,
                            "What is HOROI HOROI MANGAI/mouthwash most effective against?\n(1) Manawa kino\n(2) Rongonui\n> ": 1,
                            "How long should your NGARU/floss be before using?\n(1) 46 cm\n(2) 41 cm\n> ": 1,
                            "What causes TOTI TE TAI/tooth decay?\n(1) Waikawa\n(2) Kawhe\n> ": 1,
                            "What is Halitosis the medical term for?\n(1) Arero huruhuru mangu\n(2) Manawa kino\n> ": 2,
                            "What is the best way prevent MATE KAPIA/gum disease?\n(1) Tango tohu\n(2) Kiriuta fluoride\n> ": 1,
                            "When should your PARAIHE NIHO/toothbrush be replaced?\n(1) 2 ki te 3 marama\n(2) 4 ki te 5 marama\n> ": 1}
    user_answer = 0
    health = 100
    ai_health = 100
    valid_input = [1, 2]
    turn = 1
    
    if translate == False:
        print("=================================")
        print("START")
        print("=================================")
        print("Your health         |  {}% HP".format(health))
        print("Opponent health     |  {}% HP".format(ai_health))
        print("=================================")
        print()

        for question, correct_answer in questions.items():
            user_answer = force_number(question)
            print()
            if user_answer == correct_answer:
                print("You are correct")
                ai_health = attack(characters, ai_health, translate)
                print()
                health = ai_attack(characters, health, translate)
                print()

            elif user_answer != correct_answer:
                print("You are incorrect")
                print("The right answer was '{}'".format(correct_answer))
                print("You cannot attack as you answered wrong :(")
                print()
                health = ai_attack(characters, health, translate)
                print()

    elif translate == True:
        print("=================================")
        print("Timata")
        print("=================================")
        print("Your hauora         |  {}% HP".format(health))
        print("Opponent hauora     |  {}% HP".format(ai_health))
        print("=================================")
        print()

        for question, correct_answer in questions_translated.items():
            user_answer = force_number(question)
            print()
            if user_answer == correct_answer:
                print("You are whakatika")
                ai_health = attack(characters, ai_health, translate)
                print()
                health = ai_attack(characters, health, translate)
                print()

            elif user_answer != correct_answer:
                print("You are hē")
                print("The right answer was '{}'".format(correct_answer))
                print("You cannot whakaeke as you answered hē :(")
                print()
                health = ai_attack(characters, health, translate)
                print()

                
def attack(characters, ai_health, translate):
    """
    If user gets the answer correct they may
    choose an attack to use against the AI
    """
    toothbrush = {"Poor Brush": 10,
                  "Good Brush": 20,
                  "Perfect Brush": 30}
    toothbrush_translated = {"Poor Paraihe": 10,
                             "Good Paraihe": 20,
                             "Perfect Paraihe": 30}
    floss = {"Poor Floss": 10,
             "Good Floss": 20,
             "Perfect Floss": 30}
    floss_translated = {"Poor Miro": 10,
                         "Good Miro": 20,
                         "Perfect Miro": 30}
    mouthwash = {"Poor Mouthwash": 10,
                 "Good Mouthwash": 20,
                 "Perfect Mouthwash": 30}
    mouthwash_translated = {"Poor Horoi horoi mangai": 10,
                            "Good Horoi horoi mangai": 20,
                            "Perfect Horoi horoi mangai": 30}
    valid_input = [1, 2, 3]
    move = ""
    count = 0
    damage = 0
    choice = 0
    move_list = []

    if translate == False:
        if characters[0] == "Toothbrush":
            print("Choose a move")
            for move, damage in toothbrush.items():
                count += 1
                print("({}) {} - {} DMG".format(count, move, damage))
            while not (choice in valid_input):
                choice = force_number("> ")
            move_list = list(toothbrush)
            if choice == 1:
                move = move_list[0]
                damage = toothbrush["Poor Brush"]
                ai_health -= damage
            elif choice == 2:
                move = move_list[1]
                damage = toothbrush["Good Brush"]
                ai_health -= damage
            elif choice == 3:
                move = move_list[2]
                damage = toothbrush["Perfect Brush"]
                ai_health -= damage

        elif characters[0] == "Floss":
            print("Choose a move")
            for move, damage in floss.items():
                count += 1
                print("({}) {} - {} DMG".format(count, move, damage))
            while not (choice in valid_input):
                choice = force_number("> ")
            move_list = list(floss)
            if choice == 1:
                move = move_list[0]
                damage = floss["Poor Floss"]
                ai_health -= damage
            elif choice == 2:
                move = move_list[1]
                damage = floss["Good Floss"]
                ai_health -= damage
            elif choice == 3:
                move = move_list[2]
                damage = floss["Perfect Floss"]
                ai_health -= damage

        elif characters[0] == "Mouthwash":
            print("Choose a move")
            for move, damage in mouthwash.items():
                count += 1
                print("({}) {} - {} DMG".format(count, move, damage))
            while not (choice in valid_input):
                choice = force_number("> ")
            move_list = list(floss)
            if choice == 1:
                move = move_list[0]
                damage = mouthwash["Poor Mouthwash"]
                ai_health -= damage
            elif choice == 2:
                move = move_list[1]
                damage = mouthwash["Good Mouthwash"]
                ai_health -= damage
            elif choice == 3:
                move = move_list[2]
                damage = mouthwash["Perfect Mouthwash"]
                ai_health -= damage

        print("{} is being cleaned with '{}' for {} DMG".format(characters[1], move, damage))
        print("{} is now at {} health".format(characters[1], ai_health))

    # if user wants to translate to Te Reo
    elif translate == True:
        if characters[0] == "Paraihe niho":
            print("Choose a neke")
            for move, damage in toothbrush_translated.items():
                count += 1
                print("({}) {} - {} DMG".format(count, move, damage))
            while not (choice in valid_input):
                choice = force_number("> ")
            move_list = list(toothbrush_translated)
            if choice == 1:
                move = move_list[0]
                damage = toothbrush_translated["Poor Paraihe"]
                ai_health -= damage
            elif choice == 2:
                move = move_list[1]
                damage = toothbrush_translated["Good Paraihe"]
                ai_health -= damage
            elif choice == 3:
                move = move_list[2]
                damage = toothbrush_translated["Perfect Paraihe"]
                ai_health -= damage

        elif characters[0] == "Miro":
            print("Choose a neke")
            for move, damage in floss_translated.items():
                count += 1
                print("({}) {} - {} DMG".format(count, move, damage))
            while not (choice in valid_input):
                choice = force_number("> ")
            move_list = list(floss_translated)
            if choice == 1:
                move = move_list[0]
                damage = floss_translated["Poor Miro"]
                ai_health -= damage
            elif choice == 2:
                move = move_list[1]
                damage = floss_translated["Good Miro"]
                ai_health -= damage
            elif choice == 3:
                move = move_list[2]
                damage = floss_translated["Perfect Miro"]
                ai_health -= damage

        elif characters[0] == "Horoi horoi mangai":
            print("Choose a neke")
            for move, damage in mouthwash_translated.items():
                count += 1
                print("({}) {} - {} DMG".format(count, move, damage))
            while not (choice in valid_input):
                choice = force_number("> ")
            move_list = list(mouthwash_translated)
            if choice == 1:
                move = move_list[0]
                damage = mouthwash_translated["Poor Horoi horoi mangai"]
                ai_health -= damage
            elif choice == 2:
                move = move_list[1]
                damage = mouthwash_translated["Good Horoi horoi mangai"]
                ai_health -= damage
            elif choice == 3:
                move = move_list[2]
                damage = mouthwash_translated["Perfect Horoi horoi mangai"]
                ai_health -= damage

        print("{} is being horoia with '{}' for {} DMG".format(characters[1], move, damage))
        print("{} is now at {} hauora".format(characters[1], ai_health))

    return ai_health


def ai_attack(characters, health, translate):
    """
    AI attacks the user
    """
    import random
    moveset = {"Poor Attack": 10,
               "Good Attack": 20,
               "Perfect Attack": 30}
    moveset_translated = {"Poor Whakaeke": 10,
                          "Good Whakaeke": 20,
                          "Perfect Whakaeke": 30}
    move = ""
    damage = 0
    roll = 0

    # randomly rolls a number which will
    # dictate the attack
    roll = random.randint(1, 3)
    
    if translate == False:
        move_list = list(moveset)
        if roll == 1:
            move = move_list[0]
            damage = moveset["Poor Attack"]
            health -= damage
        elif roll == 2:
            move = move_list[1]
            damage = moveset["Good Attack"]
            health -= damage
        elif roll == 3:
            move = move_list[2]
            damage = moveset["Perfect Attack"]
            health -= damage

        print("{} is being cleaned with '{}' for {} DMG".format(characters[0], move, damage))
        print("{} is now at {} health".format(characters[0], health))

    elif translate == True:
        move_list = list(moveset_translated)
        if roll == 1:
            move = move_list[0]
            damage = moveset_translated["Poor Whakaeke"]
            health -= damage
        elif roll == 2:
            move = move_list[1]
            damage = moveset_translated["Good Whakaeke"]
            health -= damage
        elif roll == 3:
            move = move_list[2]
            damage = moveset_translated["Perfect Whakaeke"]
            health -= damage

        print("{} is being horoia with '{}' for {} DMG".format(characters[0], move, damage))
        print("{} is now at {} hauora".format(characters[0], health))

    return health


def end(characters, health, ai_health, translate):
    """

    """

    if translate == False:
        if health > ai_health:
            if ai_health < 0:
                print("=================================")
                print("Your health         |  {}% HP".format(health))
                print("Opponent health     |  0% HP")
                print("=================================")
                print("Congratulations, {}, you have conquered bad dental hygiene :)".format(characters[2]))
                print()
            else:
                print("=================================")
                print("Your health         |  {}% HP".format(health))
                print("Opponent health     |  {}% HP".format(ai_health))
                print("=================================")
                print("Congratulations, {}, you have conquered bad dental hygiene :)".format(characters[2]))
                print()

        elif health < ai_health:
            if health < 0:
                print("=================================")
                print("Your health         |  0% HP")
                print("Opponent health     |  {}% HP".format(ai_health))
                print("=================================")
                print("Sadly, {}, you have not be able to conquer bad dental hygiene :(".format(characters[2]))
                print()
            else:
                print("=================================")
                print("Your health         |  {}% HP".format(health))
                print("Opponent health     |  {}% HP".format(ai_health))
                print("=================================")
                print("Sadly, {}, you have not be able to conquer bad dental hygiene :(".format(characters[2]))
                print()

        elif health == ai_health:
            print("=================================")
            print("Your health         |  {}% HP".format(health))
            print("Opponent health     |  {}% HP".format(ai_health))
            print("=================================")
            print("Weirdly, {}, you have tied with {}".format(characters[2], characters[1]))
            print()

        print("Game Over")


    elif translate == True:
        if health > ai_health:
            if ai_health < 0:
                print("=================================")
                print("Your hauora         |  {}% HP".format(health))
                print("Opponent hauora     |  0% HP")
                print("=================================")
                print("Congratulations, {}, you have conquered kino akuaku niho :)".format(characters[2]))
                print()
            else:
                print("=================================")
                print("Your hauora         |  {}% HP".format(health))
                print("Opponent hauora     |  {}% HP".format(ai_health))
                print("=================================")
                print("Congratulations, {}, you have conquered kino akuaku niho :)".format(characters[2]))
                print()

        elif health < ai_health:
            if health < 0:
                print("=================================")
                print("Your hauora         |  0% HP")
                print("Opponent hauora     |  {}% HP".format(ai_health))
                print("=================================")
                print("Sadly, {}, you have not be able to conquer kino akuaku niho :(".format(characters[2]))
                print()
            else:
                print("=================================")
                print("Your hauora         |  {}% HP".format(health))
                print("Opponent hauora     |  {}% HP".format(ai_health))
                print("=================================")
                print("Sadly, {}, you have not be able to conquer kino akuaku niho :(".format(characters[2]))
                print()

        elif health == ai_health:
            print("=================================")
            print("Your hauora         |  {}% HP".format(health))
            print("Opponent hauora     |  {}% HP".format(ai_health))
            print("=================================")
            print("Weirdly, {}, you have herea with {}".format(characters[2], characters[1]))
            print()

        print("Kua mutu te kemu")


def main():
    """
    Runs the code
    """
    menu()
