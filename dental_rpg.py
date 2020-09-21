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
        while not (choice in valid_input):
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
        while not (choice in valid_input):
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
                 "When should toothbrushes be replaced?\n(1) 2 to 3 months\n(2) 4 to 5 months\n> ": 1,
                 "Poor dental health is linked to many serious diseases and conditions.\n(1) False\n(2) True\n> ": 2,
                 "Which of the following usually precede(s) gum disease?\n(1) Dentures\n(2) Gingivitis\n> ": 2,
                 "Which of these is best for your teeth?\n(1) Cheese\n(2) Soft bread\n> ": 1}
    questions_translated = {"How roa should you paraihe your niho?\n(1) 1 meneti\n(2) 2 meneti\n> ": 2,
                            "What is horoi horoi mangai most effective against?\n(1) Manawa kino\n(2) Rongonui\n> ": 1,
                            "How roa should your ngaru be before using?\n(1) 46 cm\n(2) 41 cm\n> ": 1,
                            "What causes toti te tai?\n(1) Waikawa\n(2) Kawhe\n> ": 1,
                            "What is Halitosis the wā hauora for?\n(1) Arero huruhuru mangu\n(2) Manawa kino\n> ": 2,
                            "What is the best way prevent mate kapia?\n(1) Tango tohu\n(2) Kiriuta fluoride\n> ": 1,
                            "When should your paraihe niho be replaced?\n(1) 2 ki te 3 marama\n(2) 4 ki te 5 marama\n> ": 1,
                            "Te koretake o te hauora niho is hono to many mate kino and tikanga.\n(1) Hape\n(2) Pono\n> ": 2,
                            "Which of the e whai ake nei usually precede(s) mate kapia?\n(1) Dentures\n(2) Gingivitis\n> ": 2,
                            "Which of these is pai rawa atu for your niho?\n(1) Tiihi\n(2) Parāoa ngohengohe\n> ": 1}
    question_list = []
    user_answer = 0
    health = 100
    ai_health = 100
    valid_input = [1, 2]
    
    
    if translate == False:
        print("=================================")
        print("START")
        print("=================================")
        print("Your health         |  {:.0f}% HP".format(health))
        print("Opponent health     |  {:.0f}% HP".format(ai_health))
        print("=================================")
        print()
        print("Every move has a chance of hitting a critical attack")
        print("There is a 1.5x multiplier for damage")
        print("Move 1 - 20% crit chance")
        print("Move 2 - 15% crit chance")
        print("Move 3 - 10% crit chance")
        print()

        for question, correct_answer in questions.items():
            if health > 0 and ai_health > 0:
                user_answer = force_number(question)
                while not (user_answer in valid_input):
                    print("Please answer with '1' or '2'")
                    user_answer = force_number(question)
                print()
                if user_answer == correct_answer:
                    print("You are correct")
                    ai_health = attack(characters, health, ai_health, translate)
                    print()
                    print("---------------------------------")
                    print()
                    if ai_health > 0:
                        health = ai_attack(characters, health, ai_health, translate)
                    print()
                    print("---------------------------------")
                    print()

                elif user_answer != correct_answer:
                    print("You are incorrect")
                    print("The right answer was '{}'".format(correct_answer))
                    print("You cannot attack as you answered wrong :(")
                    print()
                    print("---------------------------------")
                    print()
                    if ai_health > 0:
                        health = ai_attack(characters, health, ai_health, translate)
                    print()
                    print("---------------------------------")
                    print()
            elif health <= 0 or ai_health <= 0:
                break

    elif translate == True:
        print("=================================")
        print("Timata")
        print("=================================")
        print("Your hauora         |  {:.0f}% HP".format(health))
        print("Opponent hauora     |  {:.0f}% HP".format(ai_health))
        print("=================================")
        print()
        print("Every neke has a tupono noa of hitting a arohaehae whakaeke")
        print("There is a 1.5x multiplier for tūkino")
        print("Neke 1 - 20% crit tupono noa")
        print("Neke 2 - 15% crit tupono noa")
        print("Neke 3 - 10% crit tupono noa")
        print()

        for question, correct_answer in questions_translated.items():
            if health > 0 and ai_health > 0:
                user_answer = force_number(question)
                while not (user_answer in valid_input):
                    print("Please whakautu with '1' or '2'")
                    user_answer = force_number(question)
                print()
                if user_answer == correct_answer:
                    print("You are whakatika")
                    ai_health = attack(characters, health, ai_health, translate)
                    print()
                    print("---------------------------------")
                    print()
                    if ai_health > 0:
                        health = ai_attack(characters, health, ai_health, translate)
                    print()
                    print("---------------------------------")
                    print()

                elif user_answer != correct_answer:
                    print("You are hē")
                    print("The right answer was '{}'".format(correct_answer))
                    print("You cannot whakaeke as you answered hē :(")
                    print()
                    print("---------------------------------")
                    print()
                    if ai_health > 0:
                        health = ai_attack(characters, health, ai_health, translate)
                    print()
                    print("---------------------------------")
                    print()
            elif health <= 0 or ai_health <= 0:
                break

    return health, ai_health


def random_crit(choice, damage):
    """
    Randomises if attack is a miss or not
    """
    import random
    chance = 0
    valid_chance = 0
    crit = False

    if choice == 1:
        chance = random.randint(1, 10)
        valid_chance = random.randint(1, 10)
        if chance == valid_chance:
            new_damage = damage * 1.5
            crit = True
        else:
            new_damage = damage
            
    elif choice == 2:
        chance = random.randint(1, 15)
        valid_chance = random.randint(1, 15)
        if chance == valid_chance:
            new_damage = damage * 1.5
            crit = True
        else:
            new_damage = damage
            
    elif choice == 3:
        chance = random.randint(1, 20)
        valid_chance = random.randint(1, 20)
        if chance == valid_chance:
            new_damage = damage * 1.5
            crit = True
        else:
            new_damage = damage

    return crit, new_damage


def attack(characters, health, ai_health, translate):
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
    move_name = ""
    count = 0
    damage = 0
    choice = 0
    move_list = []
    crit = False

    if translate == False:
        if characters[0] == "Toothbrush":
            print("Choose a move:")
            for move, damage in toothbrush.items():
                count += 1
                print("({}) {} - {} DMG".format(count, move, damage))
            while not (choice in valid_input):
                choice = force_number("> ")
                
            for move in toothbrush:
                move_list.append(move)
                
            if choice == 1:
                move_name = move_list[0]
                damage = toothbrush["Poor Brush"]
                crit, damage = random_crit(choice, damage)
                if crit == True:
                    print("Critical hit!")
                ai_health -= damage
            elif choice == 2:
                move_name = move_list[1]
                damage = toothbrush["Good Brush"]
                crit, damage = random_crit(choice, damage)
                if crit == True:
                    print("Critical hit!")
                ai_health -= damage
            elif choice == 3:
                move_name = move_list[2]
                damage = toothbrush["Perfect Brush"]
                crit, damage = random_crit(choice, damage)
                if crit == True:
                    print("Critical hit!")
                ai_health -= damage

        elif characters[0] == "Floss":
            print("Choose a move:")
            for move, damage in floss.items():
                count += 1
                print("({}) {} - {} DMG".format(count, move, damage))
            while not (choice in valid_input):
                choice = force_number("> ")
                
            for move in floss:
                move_list.append(move)
            
            if choice == 1:
                move_name = move_list[0]
                damage = floss["Poor Floss"]
                crit, damage = random_crit(choice, damage)
                if crit == True:
                    print("Critical hit!")
                ai_health -= damage
            elif choice == 2:
                move_name = move_list[1]
                damage = floss["Good Floss"]
                crit, damage = random_crit(choice, damage)
                if crit == True:
                    print("Critical hit!")
                ai_health -= damage
            elif choice == 3:
                move_name = move_list[2]
                damage = floss["Perfect Floss"]
                crit, damage = random_crit(choice, damage)
                if crit == True:
                    print("Critical hit!")
                ai_health -= damage

        elif characters[0] == "Mouthwash":
            print("Choose a move:")
            for move, damage in mouthwash.items():
                count += 1
                print("({}) {} - {} DMG".format(count, move, damage))
            while not (choice in valid_input):
                choice = force_number("> ")
                
            for move in mouthwash:
                move_list.append(move)
            
            if choice == 1:
                move_name = move_list[0]
                damage = mouthwash["Poor Mouthwash"]
                crit, damage = random_crit(choice, damage)
                if crit == True:
                    print("Critical hit!")
                ai_health -= damage
            elif choice == 2:
                move_name = move_list[1]
                damage = mouthwash["Good Mouthwash"]
                crit, damage = random_crit(choice, damage)
                if crit == True:
                    print("Critical hit!")
                ai_health -= damage
            elif choice == 3:
                move_name = move_list[2]
                damage = mouthwash["Perfect Mouthwash"]
                crit, damage = random_crit(choice, damage)
                if crit == True:
                    print("Critical hit!")
                ai_health -= damage

        print()
        print("{} is attacking...".format(characters[0]))
        print("{} is being cleaned with '{}' for {:.0f} DMG".format(characters[1], move_name, damage))
        print()
        if ai_health > 0 and health > 0:
            print("=================================")
            print("Your health         |  {:.0f}% HP".format(health))
            print("Opponent health     |  {:.0f}% HP".format(ai_health))
            print("=================================")

    # if user wants to translate to Te Reo
    elif translate == True:
        if characters[0] == "Paraihe niho":
            print("Choose a neke")
            for move, damage in toothbrush_translated.items():
                count += 1
                print("({}) {} - {} DMG".format(count, move, damage))
            while not (choice in valid_input):
                choice = force_number("> ")
                
            for move in toothbrush_translated:
                move_list.append(move)
            
            if choice == 1:
                move_name = move_list[0]
                damage = toothbrush_translated["Poor Paraihe"]
                crit, damage = random_crit(choice, damage)
                if crit == True:
                    print("Arohaehae hit!")
                ai_health -= damage
            elif choice == 2:
                move_name = move_list[1]
                damage = toothbrush_translated["Good Paraihe"]
                crit, damage = random_crit(choice, damage)
                if crit == True:
                    print("Arohaehae hit!")
                ai_health -= damage
            elif choice == 3:
                move_name = move_list[2]
                damage = toothbrush_translated["Perfect Paraihe"]
                crit, damage = random_crit(choice, damage)
                if crit == True:
                    print("Arohaehae hit!")
                ai_health -= damage


        elif characters[0] == "Miro":
            print("Choose a neke")
            for move, damage in floss_translated.items():
                count += 1
                print("({}) {} - {} DMG".format(count, move, damage))
            while not (choice in valid_input):
                choice = force_number("> ")
                
            for move in floss_translated:
                move_list.append(move)
            
            if choice == 1:
                move_name = move_list[0]
                damage = floss_translated["Poor Miro"]
                crit, damage = random_crit(choice, damage)
                if crit == True:
                    print("Arohaehae hit!")
                ai_health -= damage
            elif choice == 2:
                move_name = move_list[1]
                damage = floss_translated["Good Miro"]
                crit, damage = random_crit(choice, damage)
                if crit == True:
                    print("Arohaehae hit!")
                ai_health -= damage
            elif choice == 3:
                move_name = move_list[2]
                damage = floss_translated["Perfect Miro"]
                crit, damage = random_crit(choice, damage)
                if crit == True:
                    print("Arohaehae hit!")
                ai_health -= damage

        elif characters[0] == "Horoi horoi mangai":
            print("Choose a neke")
            for move, damage in mouthwash_translated.items():
                count += 1
                print("({}) {} - {} DMG".format(count, move, damage))
            while not (choice in valid_input):
                choice = force_number("> ")
                
            for move in mouthwash_translated:
                move_list.append(move)
            
            if choice == 1:
                move_name = move_list[0]
                damage = mouthwash_translated["Poor Horoi horoi mangai"]
                crit, damage = random_crit(choice, damage)
                if crit == True:
                    print("Arohaehae hit!")
                ai_health -= damage
            elif choice == 2:
                move_name = move_list[1]
                damage = mouthwash_translated["Good Horoi horoi mangai"]
                crit, damage = random_crit(choice, damage)
                if crit == True:
                    print("Arohaehae hit!")
                ai_health -= damage
            elif choice == 3:
                move_name = move_list[2]
                damage = mouthwash_translated["Perfect Horoi horoi mangai"]
                crit, damage = random_crit(choice, damage)
                if crit == True:
                    print("Arohaehae hit!")
                ai_health -= damage

        print()
        print("{} is whakaeke...".format(characters[0]))
        print("{} is being horoia with '{}' for {:.0f} DMG".format(characters[1], move_name, damage))
        print()
        if ai_health > 0 and health > 0:
            print("=================================")
            print("Your hauora         |  {:.0f}% HP".format(health))
            print("Opponent hauora     |  {:.0f}% HP".format(ai_health))
            print("=================================")

    return ai_health


def ai_attack(characters, health, ai_health, translate):
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
    move_list = []
    move_name = ""
    damage = 0
    choice = 0
    crit = False

    # randomly rolls a number which will
    # dictate the attack
    choice = random.randint(1, 3)
    
    if translate == False:
        for move in moveset:
            move_list.append(move)            
        if choice == 1:
            move_name = move_list[0]
            damage = moveset["Poor Attack"]
            crit, damage = random_crit(choice, damage)
            if crit == True:
                print("Critical hit!")
            health -= damage
        elif choice == 2:
            move_name = move_list[1]
            damage = moveset["Good Attack"]
            crit, damage = random_crit(choice, damage)
            if crit == True:
                print("Critical hit!")
            health -= damage                
        elif choice == 3:
            move_name = move_list[2]
            damage = moveset["Perfect Attack"]
            crit, damage = random_crit(choice, damage)
            if crit == True:
                print("Critical hit!")
            health -= damage

        print("{} is attacking...".format(characters[1]))
        print("{} is being attacked with '{}' for {:.0f} DMG".format(characters[0], move_name, damage))
        print()
        if ai_health > 0 and health > 0:
            print("=================================")
            print("Your health         |  {:.0f}% HP".format(health))
            print("Opponent health     |  {:.0f}% HP".format(ai_health))
            print("=================================")

    elif translate == True:
        for move in moveset_translated:
            move_list.append(move)            
        if choice == 1:
            move_name = move_list[0]
            damage = moveset_translated["Poor Whakaeke"]
            crit, damage = random_crit(choice, damage)
            if crit == True:
                print("Arohaehae hit!")
            health -= damage
        elif choice == 2:
            move_name = move_list[1]
            damage = moveset_translated["Good Whakaeke"]
            crit, damage = random_crit(choice, damage)
            if crit == True:
                print("Arohaehae hit!")
            health -= damage                
        elif choice == 3:
            move_name = move_list[2]
            damage = moveset_translated["Perfect Whakaeke"]
            crit, damage = random_crit(choice, damage)
            if crit == True:
                print("Arohaehae hit!")
            health -= damage                

        print("{} is whakaeke...".format(characters[1]))
        print("{} is being whakaekehia with '{}' for {:.0f} DMG".format(characters[0], move_name, damage))
        print()
        if ai_health > 0 and health > 0:
            print("=================================")
            print("Your hauora         |  {:.0f}% HP".format(health))
            print("Opponent hauora     |  {:.0f}% HP".format(ai_health))
            print("=================================")

    return health


def end(characters, health, ai_health, translate):
    """

    """

    if translate == False:
        if health > ai_health:
            if ai_health < 0:
                print("=================================")
                print("Your health         |  {:.0f}% HP".format(health))
                print("Opponent health     |  0% HP")
                print("=================================")
                print("Congratulations, {}, you have conquered bad dental hygiene :)".format(characters[2]))
                print()
            else:
                print("=================================")
                print("Your health         |  {:.0f}% HP".format(health))
                print("Opponent health     |  {:.0f}% HP".format(ai_health))
                print("=================================")
                print("Congratulations, {}, you have conquered bad dental hygiene :)".format(characters[2]))
                print()

        elif health < ai_health:
            if health < 0:
                print("=================================")
                print("Your health         |  0% HP")
                print("Opponent health     |  {:.0f}% HP".format(ai_health))
                print("=================================")
                print("Sadly, {}, you have not be able to conquer bad dental hygiene :(".format(characters[2]))
                print()
            else:
                print("=================================")
                print("Your health         |  {:.0f}% HP".format(health))
                print("Opponent health     |  {:.0f}% HP".format(ai_health))
                print("=================================")
                print("Sadly, {}, you have not be able to conquer bad dental hygiene :(".format(characters[2]))
                print()

        elif health == ai_health:
            print("=================================")
            print("Your health         |  {:.0f}% HP".format(health))
            print("Opponent health     |  {:.0f}% HP".format(ai_health))
            print("=================================")
            print("Weirdly, {}, you have tied with {}".format(characters[2], characters[1]))
            print()

        print("Game Over")


    elif translate == True:
        if health > ai_health:
            if ai_health < 0:
                print("=================================")
                print("Your hauora         |  {:.0f}% HP".format(health))
                print("Opponent hauora     |  0% HP")
                print("=================================")
                print("Congratulations, {}, you have conquered kino akuaku niho :)".format(characters[2]))
                print()
            else:
                print("=================================")
                print("Your hauora         |  {:.0f}% HP".format(health))
                print("Opponent hauora     |  {:.0f}% HP".format(ai_health))
                print("=================================")
                print("Congratulations, {}, you have conquered kino akuaku niho :)".format(characters[2]))
                print()

        elif health < ai_health:
            if health < 0:
                print("=================================")
                print("Your hauora         |  0% HP")
                print("Opponent hauora     |  {:.0f}% HP".format(ai_health))
                print("=================================")
                print("Sadly, {}, you have not be able to conquer kino akuaku niho :(".format(characters[2]))
                print()
            else:
                print("=================================")
                print("Your hauora         |  {:.0f}% HP".format(health))
                print("Opponent hauora     |  {:.0f}% HP".format(ai_health))
                print("=================================")
                print("Sadly, {}, you have not be able to conquer kino akuaku niho :(".format(characters[2]))
                print()

        elif health == ai_health:
            print("=================================")
            print("Your hauora         |  {:.0f}% HP".format(health))
            print("Opponent hauora     |  {:.0f}% HP".format(ai_health))
            print("=================================")
            print("Weirdly, {}, you have herea with {}".format(characters[2], characters[1]))
            print()

        print("Kua mutu te kemu")


def main():
    """
    Runs the code
    """
    menu()
