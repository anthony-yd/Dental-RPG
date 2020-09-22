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
    loop = True
    loop_choice = ""
    valid_input = [1, 2, 3]

    while loop == True:
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

        loop_choice = force_number("Would you like to play again?\n(1) Yes\n(2) No\n> ")
        if loop == 1:
            loop = True
        elif loop == 2:
            loop = False
            print("Thanks for playing!")


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
        username = input("Enter your ingoa/name\n> ").lower().title().strip()
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
            choice = force_number("Please choose a pūāhua/character\n> ")
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
    questions_translated = {"How long should you paraihe/brush your niho/teeth?\n(1) 1 meneti/minute\n(2) 2 meneti/minute\n> ": 2,
                            "What is horoi horoi mangai/mouthwash most effective against?\n(1) Manawa kino/Bad breath\n(2) Rongonui/Cavities\n> ": 1,
                            "How long should your ngaru/floss be before using?\n(1) 46 cm\n(2) 41 cm\n> ": 1,
                            "What causes toti te tai/tooth decay?\n(1) Waikawa/Acid\n(2) Kawhe/Caffiene\n> ": 1,
                            "What is Halitosis the wā hauora/medical term for?\n(1) Arero huruhuru mangu/Black hairy tongue\n(2) Manawa kino/Bad breath\n> ": 2,
                            "What is the best way prevent mate kapia/gum disease?\n(1) Tango tohu/Remove plaque\n(2) Kiriuta fluoride/Flouride toothpaste\n> ": 1,
                            "When should your paraihe niho/toothbrush be replaced?\n(1) 2 ki te 3 marama/month\n(2) 4 ki te 5 marama/month\n> ": 1,
                            "Poor dental health is linked to many serious diseases and conditions.\n(1) Hape/True\n(2) Pono/False\n> ": 2,
                            "Which of the following usually precede(s) mate kapia/gum disease?\n(1) Dentures\n(2) Gingivitis\n> ": 2,
                            "Which of these is best for your niho/teeth?\n(1) Tiihi/Cheese\n(2) Parāoa ngohengohe/Soft bread\n> ": 1}
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
        print("START/Timata")
        print("=================================")
        print("Your hauora         |  {:.0f}% HP".format(health))
        print("Opponent hauora     |  {:.0f}% HP".format(ai_health))
        print("=================================")
        print()
        print("Every move has a chance of hitting a critical attack")
        print("There is a 1.5x multiplier for damage")
        print("Move 1 - 20% crit chance")
        print("Move 2 - 15% crit chance")
        print("Move 3 - 10% crit chance")
        print()

        for question, correct_answer in questions_translated.items():
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
    toothbrush = {10: "Poor Brush",
                  20: "Good Brush",
                  30: "Perfect Brush"}
    toothbrush_translated = {10: "Poor Paraihe",
                             20: "Good Paraihe",
                             30: "Perfect Paraihe"}
    floss = {10: "Poor Floss",
             20: "Good Floss",
             30: "Perfect Floss"}
    floss_translated = {10: "Poor Miro",
                        20: "Good Miro",
                        30: "Perfect Miro"}
    mouthwash = {10: "Poor Mouthwash",
                 20: "Good Mouthwash",
                 30: "Perfect Mouthwash"}
    mouthwash_translated = {10: "Poor Horoi horoi mangai",
                            20: "Good Horoi horoi mangai",
                            30: "Perfect Horoi horoi mangai"}
    valid_input = [1, 2, 3]
    move_name = ""
    damage = 0
    choice = 0
    count = 1
    move_list = []
    damage_list = []
    crit = False

    if translate == False:
        if characters[0] == "Toothbrush":
            print("Choose a move:")
            for damage, move in sorted(toothbrush.items()):
                print("({}) {} - {} DMG".format(count, move, damage))
                move_list.append(move)
                damage_list.append(damage)
                count += 1
            while not (choice in valid_input):
                choice = force_number("> ")
                
            if choice == 1:
                move_name = move_list[0]
                damage = damage_list[0]
                crit, damage = random_crit(choice, damage)
                if crit == True:
                    print("Critical hit!")
                ai_health -= damage
            elif choice == 2:
                move_name = move_list[1]
                damage = damage_list[1]
                crit, damage = random_crit(choice, damage)
                if crit == True:
                    print("Critical hit!")
                ai_health -= damage
            elif choice == 3:
                move_name = move_list[2]
                damage = damage_list[3]
                crit, damage = random_crit(choice, damage)
                if crit == True:
                    print("Critical hit!")
                ai_health -= damage

        elif characters[0] == "Floss":
            print("Choose a move:")
            for damage, move in sorted(floss.items()):
                print("({}) {} - {} DMG".format(count, move, damage))
                move_list.append(move)
                damage_list.append(damage)
                count += 1
            while not (choice in valid_input):
                choice = force_number("> ")
            
            if choice == 1:
                move_name = move_list[0]
                damage = damage_list[0]
                crit, damage = random_crit(choice, damage)
                if crit == True:
                    print("Critical hit!")
                ai_health -= damage
            elif choice == 2:
                move_name = move_list[1]
                damage = damage_list[1]
                crit, damage = random_crit(choice, damage)
                if crit == True:
                    print("Critical hit!")
                ai_health -= damage
            elif choice == 3:
                move_name = move_list[2]
                damage = damage_list[2]
                crit, damage = random_crit(choice, damage)
                if crit == True:
                    print("Critical hit!")
                ai_health -= damage

        elif characters[0] == "Mouthwash":
            print("Choose a move:")
            for damage, move in sorted(mouthwash.items()):
                print("({}) {} - {} DMG".format(count, move, damage))
                move_list.append(move)
                damage_list.append(damage)
                count += 1
            while not (choice in valid_input):
                choice = force_number("> ")
            
            if choice == 1:
                move_name = move_list[0]
                damage = damage_list[0]
                crit, damage = random_crit(choice, damage)
                if crit == True:
                    print("Critical hit!")
                ai_health -= damage
            elif choice == 2:
                move_name = move_list[1]
                damage = damage_list[1]
                crit, damage = random_crit(choice, damage)
                if crit == True:
                    print("Critical hit!")
                ai_health -= damage
            elif choice == 3:
                move_name = move_list[2]
                damage = damage_list[2]
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
            print("Choose a move:")
            for damage, move in sorted(toothbrush_translated.items()):
                print("({}) {} - {} DMG".format(count, move, damage))
                move_list.append(move)
                damage_list.append(damage)
                count += 1
            while not (choice in valid_input):
                choice = force_number("> ")
            
            if choice == 1:
                move_name = move_list[0]
                damage = damage_list[0]
                crit, damage = random_crit(choice, damage)
                if crit == True:
                    print("Critical hit!")
                ai_health -= damage
            elif choice == 2:
                move_name = move_list[1]
                damage = damage_list[1]
                crit, damage = random_crit(choice, damage)
                if crit == True:
                    print("Critical hit!")
                ai_health -= damage
            elif choice == 3:
                move_name = move_list[2]
                damage = damage_list[2]
                crit, damage = random_crit(choice, damage)
                if crit == True:
                    print("Critical hit!")
                ai_health -= damage


        elif characters[0] == "Miro":
            print("Choose a move:")
            for damage, move in sorted(floss_translated.items()):
                print("({}) {} - {} DMG".format(count, move, damage))
                move_list.append(move)
                damage_list.append(damage)
                count += 1
            while not (choice in valid_input):
                choice = force_number("> ")
            
            if choice == 1:
                move_name = move_list[0]
                damage = damage_list[0]
                crit, damage = random_crit(choice, damage)
                if crit == True:
                    print("Critical hit!")
                ai_health -= damage
            elif choice == 2:
                move_name = move_list[1]
                damage = damage_list[1]
                crit, damage = random_crit(choice, damage)
                if crit == True:
                    print("Critical hit!")
                ai_health -= damage
            elif choice == 3:
                move_name = move_list[2]
                damage = damage_list[2]
                crit, damage = random_crit(choice, damage)
                if crit == True:
                    print("Critical hit!")
                ai_health -= damage

        elif characters[0] == "Horoi horoi mangai":
            print("Choose a move:")
            for damage, move in sorted(mouthwash_translated.items()):
                print("({}) {} - {} DMG".format(count, move, damage))
                move_list.append(move)
                damage_list.append(damage)
                count += 1
            while not (choice in valid_input):
                choice = force_number("> ")
            
            if choice == 1:
                move_name = move_list[0]
                damage = damage_list[0]
                crit, damage = random_crit(choice, damage)
                if crit == True:
                    print("Critical hit!")
                ai_health -= damage
            elif choice == 2:
                move_name = move_list[1]
                damage = damage_list[1]
                crit, damage = random_crit(choice, damage)
                if crit == True:
                    print("Critical hit!")
                ai_health -= damage
            elif choice == 3:
                move_name = move_list[2]
                damage = damage_list[2]
                crit, damage = random_crit(choice, damage)
                if crit == True:
                    print("Critical hit!")
                ai_health -= damage

        print()
        print("{} is attacked...".format(characters[0]))
        print("{} is being cleaned with '{}' for {:.0f} DMG".format(characters[1], move_name, damage))
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
    moveset = {10: "Poor Attack",
               20: "Good Attack",
               30: "Perfect Attack"}
    moveset_translated = {10: "Poor Whakaeke",
                          20: "Good Whakaeke",
                          30: "Perfect Whakaeke"}
    damage_list = []
    move_list = []
    move_name = ""
    damage = 0
    choice = 0
    crit = False

    # randomly rolls a number which will
    # dictate the attack
    choice = random.randint(1, 3)
    
    if translate == False:
        for damage, move in sorted(moveset.items()):
            move_list.append(move)
            damage_list.append(damage)
            
        if choice == 1:
            move_name = move_list[0]
            damage = damage_list[0]
            crit, damage = random_crit(choice, damage)
            if crit == True:
                print("Critical hit!")
            health -= damage
        elif choice == 2:
            move_name = move_list[1]
            damage = damage_list[1]
            crit, damage = random_crit(choice, damage)
            if crit == True:
                print("Critical hit!")
            health -= damage                
        elif choice == 3:
            move_name = move_list[2]
            damage = damage_list[2]
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
        for damage, move in sorted(moveset_translated.items()):
            move_list.append(move)
            damage_list.append(damage)
            
        if choice == 1:
            move_name = move_list[0]
            damage = damage_list[0]
            crit, damage = random_crit(choice, damage)
            if crit == True:
                print("Critical hit!")
            health -= damage
        elif choice == 2:
            move_name = move_list[1]
            damage = damage_list[1]
            crit, damage = random_crit(choice, damage)
            if crit == True:
                print("Critical hit!")
            health -= damage                
        elif choice == 3:
            move_name = move_list[2]
            damage = damage_list[2]
            crit, damage = random_crit(choice, damage)
            if crit == True:
                print("Critical hit!")
            health -= damage                

        print("{} is attacking...".format(characters[1]))
        print("{} is being attacked with '{}' for {:.0f} DMG".format(characters[0], move_name, damage))
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

    elif translate == True:
        if health > ai_health:
            if ai_health < 0:
                print("=================================")
                print("Your hauora         |  {:.0f}% HP".format(health))
                print("Opponent hauora     |  0% HP")
                print("=================================")
                print("Congratulations, {}, you have conquered kino akuaku niho/bad dental hygiene :)".format(characters[2]))
                print()
            else:
                print("=================================")
                print("Your hauora         |  {:.0f}% HP".format(health))
                print("Opponent hauora     |  {:.0f}% HP".format(ai_health))
                print("=================================")
                print("Congratulations, {}, you have conquered kino akuaku niho/bad dental hygiene :)".format(characters[2]))
                print()

        elif health < ai_health:
            if health < 0:
                print("=================================")
                print("Your hauora         |  0% HP")
                print("Opponent hauora     |  {:.0f}% HP".format(ai_health))
                print("=================================")
                print("Sadly, {}, you have not be able to conquer kino akuaku niho/bad dental hygiene :(".format(characters[2]))
                print()
            else:
                print("=================================")
                print("Your hauora         |  {:.0f}% HP".format(health))
                print("Opponent hauora     |  {:.0f}% HP".format(ai_health))
                print("=================================")
                print("Sadly, {}, you have not be able to conquer kino akuaku niho/bad dental hygiene :(".format(characters[2]))
                print()

        elif health == ai_health:
            print("=================================")
            print("Your hauora         |  {:.0f}% HP".format(health))
            print("Opponent hauora     |  {:.0f}% HP".format(ai_health))
            print("=================================")
            print("Weirdly, {}, you have tied with {}".format(characters[2], characters[1]))
            print()


def main():
    """
    Runs the code
    """
    menu()
