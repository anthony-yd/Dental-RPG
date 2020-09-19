##
# dental_rpg.py
# 24/08/20
# Anthony D


def menu():
    """
    Menu function which allows user to choose
    what they would like to do
    """
    valid_input = ["1", "2", "3"]
    choice = ""
    translate = False

    print("Welcome to Dental RPG")
    while not(choice in valid_input):
        choice = input("""Please choose an option:
(1) Start game in English
(2) Start game in Te Reo
(3) Quit
> """)
    print()
    
    if choice == "1":
        characters = character_select(translate)
        print()
        health, ai_health = run_game(questions, characters, translate)
        end(characters, health, ai_health, translate)
        
    elif choice == "2":
        translate = True
        characters = character_select(translate)
        print()
        health, ai_health = run_game(questions, characters, translate)
        end(characters, health, ai_health, translate)
        
    elif choice == "3":
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
    choice = ""
    username = ""
    user = ""
    opponent = ""
    valid_input = ["1", "2", "3"]
    user_characters = ["(1) Toothbrush", "(2) Floss", "(3) Mouthwash"]
    user_characters_translated = ["(1) Paraihe niho", "(2) Miro", "(3) Horoi horoi mangai"]

    # asks user for name and error checks it
    if translate == False:
        username = input("Enter your name\n> ").lower().title().strip()
    elif translate == True:
        username = input("Enter your ingoa\n> ").lower().title().strip()
    while username == EMPTY:
        print("Please enter a name")
        username = input("Enter your name/ingoa\n> ").lower().title().strip()

    # asks the user to input their favored
    # character
    print()
    if translate == False:
        for character in user_characters:
            print(character)
    elif translate == True:
        for character in user_characters_translated:
            print(character)
    
    while not(choice in valid_input):
        if translate == False:
            choice = input("Please choose a character\n> ")
        elif translate == True:
            choice = input("Please choose a pūāhua\n> ")
    if translate == False:
        if choice == "1":
            user = "Toothbrush"
        elif choice == "2":
            user = "Floss"
        elif choice == "3":
            user = "Mouthwash"
            
    elif translate == True:
        if choice == "1":
            user = "Paraihe niho"
        elif choice == "2":
            user = "Miro"
        elif choice == "3":
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

    print("You have chosen {}".format(user))
    characters = [user, opponent, username]
    return characters


class Question:
    def __init__(self, prompt, answer):
        # creates attributes for questions
        # in this case the prompt/question
        # and the answer
        self.prompt = prompt
        self.answer = answer

# questions prompts that the user will be asked
question_prompts = [
    "\n"
    "How long should you brush your teeth?\n(1) 1 minute\n(2) 2 minutes\n> ",
    "\n"
    "What is mouthwash most effective against?\n(1) Bad breath\n(2) Cavities\n> ",
    "\n"
    "How long should your floss be before using?\n(1) 18 inches\n(2) 16 inches\n> ",
    "\n"
    "What causes tooth decay?\n(1) Acid\n(2) Caffeine\n> ",
    "\n"
    "What is Halitosis the medical term for?\n(1) Black hairy tongue\n(2) Bad breath\n> ",
    "\n"
    "What is the best way prevent gum disease?\n(1) Remove plaque\n(2) Flouride toothpaste\n> ",
    "\n"
    "When should toothbrushes be replaced?\n(1) 2 to 3 months\n(2) 4 to 5 months\n> ",
    "\n"
    ]

translated_question_prompts = [
    "\n"
    "How long should you PARAIHE/brush your NIHO/teeth?\n(1) 1 meneti\n(2) 2 meneti\n> ",
    "\n"
    "What is HOROI HOROI MANGAI/mouthwash most effective against?\n(1) Manawa kino\n(2) Rongonui\n> ",
    "\n"
    "How long should your NGARU/floss be before using?\n(1) 46 cm\n(2) 41 cm\n> ",
    "\n"
    "What causes TOTI TE TAI/tooth decay?\n(1) Waikawa\n(2) Kawhe\n> ",
    "\n"
    "What is Halitosis the medical term for?\n(1) Arero huruhuru mangu\n(2) Manawa kino\n> ",
    "\n"
    "What is the best way prevent MATE KAPIA/gum disease?\n(1) Tango tohu\n(2) Kiriuta fluoride\n> ",
    "\n"
    "When should your PARAIHE NIHO/toothbrush be replaced?\n(1) 2 ki te 3 marama\n(2) 4 ki te 5 marama\n> ",
    "\n"
    ]

# list will will be iterated through
questions = [
    Question(question_prompts[0], "2"),
    Question(question_prompts[1], "1"),
    Question(question_prompts[2], "1"),
    Question(question_prompts[3], "1"),
    Question(question_prompts[4], "2"),
    Question(question_prompts[5], "1"),
    Question(question_prompts[6], "1")
    ]

# list will will be iterated through
translated_questions = [
    Question(translated_question_prompts[0], "2"),
    Question(translated_question_prompts[1], "1"),
    Question(translated_question_prompts[2], "1"),
    Question(translated_question_prompts[3], "1"),
    Question(translated_question_prompts[4], "2"),
    Question(translated_question_prompts[5], "1"),
    Question(translated_question_prompts[6], "1")
    ]

# shuffles the questions
import random
random.shuffle(questions)
random.shuffle(translated_questions)


def run_game(questions, characters, translate):
    """
    Runs the quiz so the user can use it
    """
    answer = ""
    health = 100
    ai_health = 100

    if translate == False:
        print("""=================================
START
=================================
Your health         |  {}% HP
Opponent health     |  {}% HP
=================================""".format(health, ai_health))
    elif translate == True:
        print("""=================================
Timata
=================================
Your hauora         |  {}% HP
Opponent hauora     |  {}% HP
=================================""".format(health, ai_health)) 

    if translate == False:
        for question in questions:
            # breaks the loop if user or AI has reached
            # 0 health
            if ai_health < 0 or ai_health == 0:
                break
            answer = input(question.prompt).lower().strip()
            while answer != "1" and answer != "2":
                print("Please answer with '1' or '2'")
                print()
                answer = input(question.prompt).lower().strip()
            if answer == question.answer:
                # user attacking function which allows them to
                # select the move they would like to use
                ai_health = attacking(characters, ai_health, translate)
                # if statement so the program knows when to show
                # the status of the players
                if ai_health > 0:
                    print()
                    print("""=================================
Your health         |  {}% HP
Opponent health     |  {}% HP
=================================""".format(health, ai_health))

            else:
                # AI attacking function
                health = ai_attacking(characters, health, translate)
            # if statement so the program knows when to show
            # the status of the players
            if health > 0:
                print("""=================================
Your health         |  {}% HP
Opponent health     |  {}% HP
=================================""".format(health, ai_health))

    elif translate == True:
        for question in translated_questions:
            # breaks the loop if user or AI has reached
            # 0 health
            if ai_health < 0 or ai_health == 0:
                    break
            answer = input(question.prompt).lower().strip()
            while answer != "1" and answer != "2":
                print("Please answer with '1' or '2'")
                print()
                answer = input(question.prompt).lower().strip()
            if answer == question.answer:
                # user attacking function which allows them to
                # select the move they would like to use
                ai_health = attacking(characters, ai_health, translate)
                # if statement so the program knows when to show
                # the status of the players
                if ai_health > 0:
                    print()
                    print("""=================================
Your hauora         |  {}% HP
Opponent hauora     |  {}% HP
=================================""".format(health, ai_health))

            else:
                # AI attacking function
                health = ai_attacking(characters, health, translate)
            # if statement so the program knows when to show
            # the status of the players
            if health > 0:
                print("""=================================
Your hauora         |  {}% HP
Opponent hauora     |  {}% HP
=================================""".format(health, ai_health))
            
    print()
    print("---------------------------------")
    print()

    return health, ai_health


def end(characters, health, ai_health, translate):
    """
    End statements which gives indications
    of who has won and lost
    """

    # end statements that indicate who
    # has won and the health of both
    # parties

    if translate == False:
        if health > ai_health:
            if ai_health < 0:
                print("""=================================
Your health         |  {}% HP
Opponent health     |  0% HP
=================================
Congratulations, {}, you have conquered bad dental hygiene :)""".format(health,
                                                                        characters[2]))
            else:
                print("""=================================
Your health         |  {}% HP
Opponent health     |  {}% HP
=================================
Congratulations, {}, you have conquered bad dental hygiene :)""".format(health,
                                                                        ai_health,
                                                                        characters[2]))
        elif health < ai_health:
            if health < 0:
                print("""=================================
Your health         |  0% HP
Opponent health     |  {}% HP
=================================
Sadly, {}, you have not be able to conquer bad dental hygiene :(""".format(ai_health,
                                                                           characters[2]))
            else:
                print("""=================================
Your health         |  {}% HP
Opponent health     |  {}% HP
=================================
Sadly, {}, you have not be able to conquer bad dental hygiene :(""".format(health,
                                                                           ai_health,
                                                                           characters[2]))
        elif health == ai_health:
            print("""=================================
Your health         |  {}% HP
Opponent health     |  {}% HP
=================================
Weirdly, {}, you have tied with {}""".format(health,
                                             ai_health,
                                             characters[2],
                                             characters[1]))
        print("Game Over")

    elif translate == True:
        if health > ai_health:
            if ai_health < 0:
                print("""=================================
Your hauora         |  {}% HP
Opponent hauora     |  0% HP
=================================
Congratulations, {}, you have conquered kino akuaku niho :)""".format(health,
                                                                        characters[2]))
            else:
                print("""=================================
Your hauora         |  {}% HP
Opponent hauora     |  {}% HP
=================================
Congratulations, {}, you have conquered kino akuaku niho :)""".format(health,
                                                                        ai_health,
                                                                        characters[2]))
        elif health < ai_health:
            if health < 0:
                print("""=================================
Your hauora         |  0% HP
Opponent hauora     |  {}% HP
=================================
Sadly, {}, you have not be able to conquer kino akuaku niho :(""".format(ai_health,
                                                                           characters[2]))
            else:
                print("""=================================
Your hauora         |  {}% HP
Opponent hauora     |  {}% HP
=================================
Sadly, {}, you have not be able to conquer kino akuaku niho :(""".format(health,
                                                                           ai_health,
                                                                           characters[2]))
        elif health == ai_health:
            print("""=================================
Your hauora         |  {}% HP
Opponent hauora     |  {}% HP
=================================
Weirdly, {}, you have herea with {}""".format(health,
                                             ai_health,
                                             characters[2],
                                             characters[1]))
        print("Kua mutu te kemu")


def attacking(characters, ai_health, translate):
    """
    If user gets the answer correct they may
    choose an attack to use against the AI
    """
    # character movesets
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
    valid_input = ["1", "2", "3"]
    move = ""
    count = 0
    damage = 0
    choice = ""

    # if character chosen was 'Toothbrush'
    if characters[0] == "Toothbrush":
        print()
        
        if translate == False:
            print("Choose a move")
            for move, damage in toothbrush.items():
                count += 1
                print("({}) {} - {} DMG".format(count, move, damage))
            choice = input("> ")
            while not (choice in valid_input):
                print("Please answer with '1', '2', or '3'")
                choice = input("> ")
            # depending on the choice the damage
            # will be applied
            if choice == "1":
                move = "Poor Toothbrush"
                damage = toothbrush["Poor Brush"]
                ai_health -= damage
            elif choice == "2":
                move = "Good Toothbrush"
                damage = toothbrush["Good Brush"]
                ai_health -= damage
            elif choice == "3":
                move = "Perfect Toothbrush"
                damage = toothbrush["Perfect Brush"]
                ai_health -= damage

        elif translate == True:
            print("Choose a neke")
            for move, damage in toothbrush_translated.items():
                count += 1
                print("({}) {} - {} DMG".format(count, move, damage))
            choice = input("> ")
            while not (choice in valid_input):
                print("Please whakautu with '1', '2', or '3'")
                choice = input("> ")
            # depending on the choice the damage
            # will be applied
            if choice == "1":
                move = "Poor Paraihe"
                damage = toothbrush["Poor Paraihe"]
                ai_health -= damage
            elif choice == "2":
                move = "Good Paraihe"
                damage = toothbrush["Good Paraihe"]
                ai_health -= damage
            elif choice == "3":
                move = "Perfect Paraihe"
                damage = toothbrush["Perfect Paraihe"]
                ai_health -= damage

    # if character chosen was 'Floss'
    if characters[0] == "Floss":
        print()

        if translate == False:
            print("Choose a move")
            for move, damage in floss.items():
                count += 1
                print("({}) {} - {} DMG".format(count, move, damage))
            choice = input("> ")    
            while not (choice in valid_input):
                print("Please answer with '1', '2', or '3'")
                choice = input("> ")
            # depending on the choice the damage
            # will be applied
            if choice == "1":
                move = "Poor Floss"
                damage = floss["Poor Floss"]
                ai_health -= damage
            elif choice == "2":
                move = "Good Floss"
                damage = floss["Good Floss"]
                ai_health -= damage
            elif choice == "3":
                move = "Perfect Floss"
                damage = floss["Perfect Floss"]
                ai_health -= damage

        elif translate == True:
            print("Choose a neke")
            for move, damage in floss_translated.items():
                count += 1
                print("({}) {} - {} DMG".format(count, move, damage))
            choice = input("> ")    
            while not (choice in valid_input):
                print("Please whakautu with '1', '2', or '3'")
                choice = input("> ")
            # depending on the choice the damage
            # will be applied
            if choice == "1":
                move = "Poor Miro"
                damage = floss["Poor Miro"]
                ai_health -= damage
            elif choice == "2":
                move = "Good Miro"
                damage = floss["Good Miro"]
                ai_health -= damage
            elif choice == "3":
                move = "Perfect Miro"
                damage = floss["Perfect Miro"]
                ai_health -= damage

    # if character chosen was 'Mouthwash'
    if characters[0] == "Mouthwash":
        print()

        if translate == False:
            print("Choose a move")
            for move, damage in mouthwash.items():
                count += 1
                print("({}) {} - {} DMG".format(count, move, damage))
            choice = input("> ")
            while not (choice in valid_input):
                print("Please answer with '1', '2', or '3'")
                choice = input("> ")
            # depending on the choice the damage
            # will be applied
            if choice == "1":
                move = "Poor Mouthwash"
                damage = mouthwash["Poor Mouthwash"]
                ai_health -= damage
            elif choice == "2":
                move = "Good Mouthwash"
                damage = mouthwash["Good Mouthwash"]
                ai_health -= damage
            elif choice == "3":
                move = "Perfect Mouthwash"
                damage = mouthwash["Perfect Mouthwash"]
                ai_health -= damage

        elif translate == True:
            print("Choose a neke")
            for move, damage in mouthwash.items():
                count += 1
                print("({}) {} - {} DMG".format(count, move, damage))
            choice = input("> ")
            while not (choice in valid_input):
                print("Please whakautu with '1', '2', or '3'")
                choice = input("> ")
            # depending on the choice the damage
            # will be applied
            if choice == "1":
                move = "Poor Horoi horoi mangai"
                damage = mouthwash["Poor Horoi horoi mangai"]
                ai_health -= damage
            elif choice == "2":
                move = "Good Horoi horoi mangai"
                damage = mouthwash["Good Horoi horoi mangai"]
                ai_health -= damage
            elif choice == "3":
                move = "Perfect Horoi horoi mangai"
                damage = mouthwash["Perfect Horoi horoi mangai"]
                ai_health -= damage

    # end statement which shows who is being attacked
    # and for how much damage
    print("""{} is being cleaned with '{}'
Your attack was successful and did {} DMG""".format(characters[1],
                                                    move,
                                                    damage))
    return ai_health
    

def ai_attacking(characters, health, translate):
    """
    AI attacks
    """
    import random
    moveset = {"Poor Attack": 10,
               "Good Attack": 20,
               "Perfect Attack": 30}
    move = ""
    damage = 0
    roll = 0

    # randomly rolls a number which will
    # dictate the attack
    roll = random.randint(1, 3)
    if translate == False:
        if roll == 1:
            move = "Poor Attack"
            damage = moveset["Poor Attack"]
            health -= damage
        elif roll == 2:
            move = "Good Attack"
            damage = moveset["Good Attack"]
            health -= damage
        elif roll == 3:
            move = "Perfect Attack"
            damage = moveset["Perfect Attack"]
            health -= damage

    elif translate == True:
        if roll == 1:
            move = "Poor Whakaeke"
            damage = moveset["Poor Attack"]
            health -= damage
        elif roll == 2:
            move = "Good Whakaeke"
            damage = moveset["Good Attack"]
            health -= damage
        elif roll == 3:
            move = "Perfect Whakaeke"
            damage = moveset["Perfect Attack"]
            health -= damage

    # indicates to the user what has happened
    print("""Your attack was unsuccessful
{} has done {} DMG to your teeth using '{}'""".format(characters[1],
                                                      damage,
                                                      move))
    return health

    
def main():
    """
    Runs the code
    """
    menu()
