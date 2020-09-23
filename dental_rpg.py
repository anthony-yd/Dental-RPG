##
# dental_rpg.py
# 24/08/20
# Anthony D


import random
import sys


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
    loop = True
    loop_choice = 0
    loop_valid_input = [1, 2]

    print("""Welcome to Dental RPG

Here are some notes before you play:
---------------------------------
Critical Attacks

Every move you have the choice of hitting a critical attack
There is a 1.5x multiplier for damage
Move 1 - 50% crit chance
Move 2 - 20% crit chance
Move 3 - 10% crit chance
But be careful!
If you don't hit your critical attack then you do not attack that round!
---------------------------------
Missing Attacks

Every move has a chance of missing
The miss chance is the same for every move
This means they all have a 5% chance of missing
---------------------------------""")
    print()
    while loop == True:
        # sets choice back to 0 if user wishes to play again
        choice = 0
        while not (choice in valid_input):
            choice = force_number("""Please choose an option:
(1) Start game in English
(2) Start game in Te Reo
(3) Quit
> """)
        print()
        
        if choice == 1:
            # 'translate = False' runs code in English
            translate = False
            characters = character_select(translate)
            health, ai_health = quiz(characters, translate)
            end(characters, health, ai_health, translate)        
                
        elif choice == 2:
            # 'translate = True' runs code in Te Reo
            translate = True
            characters = character_select(translate)
            health, ai_health = quiz(characters, translate)
            end(characters, health, ai_health, translate)        

        elif choice == 3:
            # exits the code as user would not like to keep playing
            print("Thank you for choosing this Dental RPG")
            sys.exit()

        while not (loop_choice in loop_valid_input):
            loop_choice = force_number("""Would you like to keep playing?
(1) Yes
(2) No
> """)
            if loop_choice == 1:
                loop = True
            elif loop_choice == 2:
                loop = False

    if loop == False:
        print("Thank you for choosing this Dental RPG")


def character_select(translate):
    """
    Allows the user to select their character
    Also rolls a random character for the user
    """
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
    user_answer = 0
    health = 100
    ai_health = 100
    valid_input = [1, 2]
    question_list = []
    answer_list = []
    randomised_questions = {}
    randomised_questions_translated = {}
    combined = []
    count = 0
    
    if translate == False:
        print("=================================")
        print("START")
        print("=================================")
        print("Your health         |  {:.0f}% HP".format(health))
        print("Opponent health     |  {:.0f}% HP".format(ai_health))
        print("=================================")
        print()

        # randomises the questions and answers of the quiz
        for original_question, original_answer in questions.items():
            question_list.append(original_question)
            answer_list.append(original_answer)
        combined = list(zip(question_list, answer_list))
        random.shuffle(combined)
        question_list, answer_list = list(zip(*combined))
        for number in question_list:
            randomised_questions[question_list[count]] = answer_list[count]
            count += 1

        for question, correct_answer in randomised_questions.items():
            if health > 0 and ai_health > 0:
                user_answer = force_number(question)
                while not (user_answer in valid_input):
                    print("Please answer with '1' or '2'")
                    user_answer = force_number(question)
                print()
                if user_answer == correct_answer:
                    print("You are correct")
                    ai_health = attacking(characters, health, ai_health, translate)
                    if ai_health > 0:
                        health = ai_attack(characters, health, ai_health, translate)
                    print()

                elif user_answer != correct_answer:
                    print("You are incorrect")
                    print("You cannot attack as you answered wrong :(")
                    print("The right answer was '{}'".format(correct_answer))
                    print()
                    if ai_health > 0:
                        health = ai_attack(characters, health, ai_health, translate)
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

        # randomises the questions and answers of the quiz
        for original_question, original_answer in questions_translated.items():
            question_list.append(original_question)
            answer_list.append(original_answer)
        combined = list(zip(question_list, answer_list))
        random.shuffle(combined)
        question_list, answer_list = list(zip(*combined))
        for number in question_list:
            randomised_questions[question_list[count]] = answer_list[count]
            count += 1

        for question, correct_answer in randomised_questions_translated.items():
            if health > 0 and ai_health > 0:
                user_answer = force_number(question)
                while not (user_answer in valid_input):
                    print("Please answer with '1' or '2'")
                    user_answer = force_number(question)
                print()
                if user_answer == correct_answer:
                    print("You are correct")
                    ai_health = attacking(characters, health, ai_health, translate)
                    if ai_health > 0:
                        health = ai_attack(characters, health, ai_health, translate)
                    print()

                elif user_answer != correct_answer:
                    print("You are incorrect")
                    print("You cannot attack as you answered wrong :(")
                    print("The right answer was '{}'".format(correct_answer))
                    print()
                    if ai_health > 0:
                        health = ai_attack(characters, health, ai_health, translate)
                    print()
            elif health <= 0 or ai_health <= 0:
                break

    return health, ai_health


def random_crit(choice, damage_value):
    """
    Randomises if attack is a miss or not
    """
    chance = 0
    valid_chance = 0
    new_damage = 0
    crit = False
   
    if choice == 0:
        chance = random.randint(1, 2)
        valid_chance = random.randint(1, 2)
        if chance == valid_chance:
            new_damage = damage_value * 1.5
            crit = True
        else:
            new_damage = damage_value
            
    elif choice == 1:
        chance = random.randint(1, 5)
        valid_chance = random.randint(1, 5)
        if chance == valid_chance:
            new_damage = damage_value * 1.5
            crit = True
        else:
            new_damage = damage_value
            
    elif choice == 2:
        chance = random.randint(1, 10)
        valid_chance = random.randint(1, 10)
        if chance == valid_chance:
            new_damage = damage_value * 1.5
            crit = True
        else:
            new_damage = damage_value

    return crit, new_damage


def random_miss(attack):
    """
    Randomises chances for a missed attack
    """
    chance = 0
    valid_chance = 0
    miss = False
            
    chance = random.randint(1, 20)
    valid_chance = random.randint(1, 20)
    if chance == valid_chance:
        attack = False
    else:
        attack = True

    return attack


def crit_miss_attacking(choice, ai_health, damage_value, characters):
    """
    Function which runs through randomised crit
    and randomised miss functions to give an attack
    """
    crit = False
    attack = True
    
    attack = random_miss(attack)
    if attack == True:
        crit, damage_value = random_crit(choice, damage_value)
        print("{} is attacking...".format(characters[0]))
        if crit == True:
            print("Critical hit!")
        ai_health -= damage_value          
    elif attack == False:
        print("You have missed your attack")

    return damage_value, attack, ai_health


def attacking(characters, health, ai_health, translate):
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
    damage_value = 0
    choice = 0
    count = 1
    move_list = []
    damage_list = []
    attack = True

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
                print()
            choice -= 1
            move_name = move_list[choice]
            damage_value = damage_list[choice]
            damage_value, attack, ai_health = crit_miss_attacking(choice,
                                                                  ai_health,
                                                                  damage_value,
                                                                  characters)

        elif characters[0] == "Floss":
            print("Choose a move:")
            for damage, move in sorted(floss.items()):
                print("({}) {} - {} DMG".format(count, move, damage))
                move_list.append(move)
                damage_list.append(damage)
                count += 1
            while not (choice in valid_input):
                choice = force_number("> ")
                print()
            choice -= 1
            move_name = move_list[choice]
            damage_value = damage_list[choice]
            damage_value, attack, ai_health = crit_miss_attacking(choice,
                                                                  ai_health,
                                                                  damage_value,
                                                                  characters)

        elif characters[0] == "Mouthwash":
            print("Choose a move:")
            for damage, move in sorted(mouthwash.items()):
                print("({}) {} - {} DMG".format(count, move, damage))
                move_list.append(move)
                damage_list.append(damage)
                count += 1
            while not (choice in valid_input):
                choice = force_number("> ")
                print()
            choice -= 1
            move_name = move_list[choice]
            damage_value = damage_list[choice]
            damage_value, attack, ai_health = crit_miss_attacking(choice,
                                                                  ai_health,
                                                                  damage_value,
                                                                  characters)
        if attack == True:
            print("{} is being attacked with '{}' for {:.0f} DMG".format(characters[1], move_name, damage_value))
            if ai_health > 0 and health > 0:
                print("=================================")
                print("Your health         |  {:.0f}% HP".format(health))
                print("Opponent health     |  {:.0f}% HP".format(ai_health))
                print("=================================")
                print()
        elif attack == False:
            if ai_health > 0 and health > 0:
                print("=================================")
                print("Your health         |  {:.0f}% HP".format(health))
                print("Opponent health     |  {:.0f}% HP".format(ai_health))
                print("=================================")
                print()

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
                print()
            choice -= 1
            move_name = move_list[choice]
            damage_value = damage_list[choice]
            damage_value, attack, ai_health = crit_miss_attacking(choice,
                                                                  ai_health,
                                                                  damage_value,
                                                                  characters)             

        elif characters[0] == "Miro":
            print("Choose a move:")
            for damage, move in sorted(floss_translated.items()):
                print("({}) {} - {} DMG".format(count, move, damage))
                move_list.append(move)
                damage_list.append(damage)
                count += 1
            while not (choice in valid_input):
                choice = force_number("> ")
                print()
            choice -= 1
            move_name = move_list[choice]
            damage_value = damage_list[choice]
            damage_value, attack, ai_health = crit_miss_attacking(choice,
                                                                  ai_health,
                                                                  damage_value,
                                                                  characters)

        elif characters[0] == "Horoi horoi mangai":
            print("Choose a move:")
            for damage, move in sorted(mouthwash_translated.items()):
                print("({}) {} - {} DMG".format(count, move, damage))
                move_list.append(move)
                damage_list.append(damage)
                count += 1
            while not (choice in valid_input):
                choice = force_number("> ")
                print()
            choice -= 1
            move_name = move_list[choice]
            damage_value = damage_list[choice]
            damage_value, attack, ai_health = crit_miss_attacking(choice,
                                                                  ai_health,
                                                                  damage_value,
                                                                  characters)
        if attack == True:
            print("{} is being attacked with '{}' for {:.0f} DMG".format(characters[1], move_name, damage_value))
            if ai_health > 0 and health > 0:
                print("=================================")
                print("Your health         |  {:.0f}% HP".format(health))
                print("Opponent health     |  {:.0f}% HP".format(ai_health))
                print("=================================")
                print()
        elif attack == False:
            if ai_health > 0 and health > 0:
                print("=================================")
                print("Your health         |  {:.0f}% HP".format(health))
                print("Opponent health     |  {:.0f}% HP".format(ai_health))
                print("=================================")
                print()

    return ai_health


def ai_crit_miss_attacking(choice, health, damage_value, characters):
    """
    Function which runs through the AI's crit and miss
    rates and calculates any change needed
    """
    crit = False
    attack = True

    attack = random_miss(attack)
    if attack == True:        
        crit, damage_value = random_crit(choice, damage_value)
        if crit == True:
            print("Critical hit!")
        health -= damage_value
    elif attack == False:
        print("{} has missed their attack".format(characters[1]))

    return damage_value, attack, health


def ai_attack(characters, health, ai_health, translate):
    """
    AI attacks the user
    """
    moveset = {10: "Poor Attack",
               20: "Good Attack",
               30: "Perfect Attack"}
    moveset_translated = {10: "Poor Whakaeke",
                          20: "Good Whakaeke",
                          30: "Perfect Whakaeke"}
    damage_list = []
    move_list = []
    damage = 0
    choice = 0
    move_name = ""
    damage_value = 0

    # randomly rolls a number which will
    # dictate the attack
    choice = random.randint(0, 2)

    # if user selected English
    if translate == False:
        for damage, move in sorted(moveset.items()):
            move_list.append(move)
            damage_list.append(damage)
        move_name = move_list[choice]
        damage_value = damage_list[choice]
        damage_value, attack, health = ai_crit_miss_attacking(choice,
                                                              health,
                                                              damage_value,
                                                              characters)
        if attack == True:
            print("{} is attacking...".format(characters[1]))
            print("{} is being attacked with '{}' for {:.0f} DMG".format(characters[0], move_name, damage_value))
            if ai_health > 0 and health > 0:
                print("=================================")
                print("Your health         |  {:.0f}% HP".format(health))
                print("Opponent health     |  {:.0f}% HP".format(ai_health))
                print("=================================")
        elif attack == False:
            if ai_health > 0 and health > 0:
                print("=================================")
                print("Your health         |  {:.0f}% HP".format(health))
                print("Opponent health     |  {:.0f}% HP".format(ai_health))
                print("=================================")

    # if user selected Te Reo
    elif translate == True:
        for damage, move in sorted(moveset_translated.items()):
            move_list.append(move)
            damage_list.append(damage)
        move_name = move_list[choice]
        damage_value = damage_list[choice]
        damage_value, attack, health = ai_crit_miss_attacking(choice,
                                                              health,
                                                              damage_value,
                                                              characters)
        if attack == True:
            print("{} is attacking...".format(characters[1]))
            print("{} is being attacked with '{}' for {:.0f} DMG".format(characters[0], move_name, damage_value))
            if ai_health > 0 and health > 0:
                print("=================================")
                print("Your health         |  {:.0f}% HP".format(health))
                print("Opponent health     |  {:.0f}% HP".format(ai_health))
                print("=================================")
        elif attack == False:
            if ai_health > 0 and health > 0:
                print("=================================")
                print("Your health         |  {:.0f}% HP".format(health))
                print("Opponent health     |  {:.0f}% HP".format(ai_health))
                print("=================================")       

    return health
            

def end(characters, health, ai_health, translate):
    """
    End statements which show the user what
    has happened/'aftermath' of game
    """

    print("---------------------------------")
    print("---------------------------------")
    print()
    
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


main()
