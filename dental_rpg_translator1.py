##
# dental_rpg.py
# 24/08/20
# Anthony D


def menu():
    """
    Menu allows user to choose what they
    would like to do
    """
    language_input = ["1", "2"]
    language = ""
    language_choice = ""
    menu_input = ["1", "2", "3"]
    menu_choice = ""

    print("Welcome to Dental RPG")
    while not(language_choice in language_input):
        language_choice = input("""Choose a language:
(1) English
(2) Maori
> """)
    print()

    # asks user for language they would
    # like to use for the program
    if language_choice == "1":
        language = "English"
    elif language_choice == "2":
        language = "Maori"

    # if English is chosen
    if language == "English":
        while not(menu_choice in menu_input):
            menu_choice = input("""Please choose an option:
(1) Start game
(2) Change language
(3) Quit
> """)
            if menu_choice == "1":
                start(language)
            elif menu_choice == "2":
                language = ""
                while not(language_choice in language_input):
                    language_choice = input("""Choose a language:
(1) English
(2) Maori
> """)
                print()
                if language_choice == "1":
                    language = "English"
                elif language_choice == "2":
                    language = "Maori"
            elif menu_choice == "3":
                break

    elif language == "Maori":
        while not(menu_choice in menu_input):
            menu_choice = input("""Tohua koa he kowhiringa:
(1) Timata kēmu
(2) Hurihia te reo
(3) Whakamutu
> """)
            if menu_choice == "1":
                start(language)
            elif menu_choice == "2":
                language = ""
                while not(language_choice in language_input):
                    language_choice = input("""Kōwhiria he reo:
(1) Ingarihi
(2) Maori
> """)
                print()
                if language_choice == "1":
                    language = "English"
                elif language_choice == "2":
                    language = "Maori"
            elif menu_choice == "3":
                break
    return language
    

def start(language):
    """
    Function which starts the rest of the code
    """
    characters = character_select(language)
    print()
    run_game(questions, characters, language)
        

def character_select(language):
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

    if language == "English":
        # asks user for name and error checks it
        username = input("Enter your name\n> ").lower().title().strip()
        while username == EMPTY:
            print("Please enter a name")
            username = input("Enter your name\n> ").lower().title().strip()

        # asks the user to input their favored
        # character
        print()
        for character in user_characters:
            print(character)
        while not(choice in valid_input):
            choice = input("Please choose a character\n> ")
        if choice == "1":
            user = "Toothbrush"
        elif choice == "2":
            user = "Floss"
        elif choice == "3":
            user = "Mouthwash"

        # randomly rolls a character that will
        # be used by the ai
        roll = random.randint(0, 2)
        if roll == 0:
            opponent = "Plaque"
        elif roll == 1:
            opponent = "Bad Breath"
        elif roll == 2:
            opponent = "Cavities"
        print("You have chosen {}".format(user))

    # sets characters in Maori instead of English
    elif language == "Maori":
        # asks user for name and error checks it
        username = input("Whakauruhia to ingoa\n> ").lower().title().strip()
        while username == EMPTY:
            print("Tomo koa he ingoa")
            username = input("Whakauruhia to ingoa\n> ").lower().title().strip()

        # asks the user to input their favored
        # character
        print()
        for character in user_characters:
            print(character)
        while not(choice in valid_input):
            choice = input("Tohua mai he tohu\n> ")
        if choice == "1":
            user = "Paraihe niho"
        elif choice == "2":
            user = "Miro"
        elif choice == "3":
            user = "Horoi"

        # randomly rolls a character that will
        # be used by the ai
        roll = random.randint(0, 2)
        if roll == 0:
            opponent = "Kaupapa"
        elif roll == 1:
            opponent = "Manawa kino"
        elif roll == 2:
            opponent = "Rongonui"        
        print("Kua whiriwhiria e koe {}".format(user))
        
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
    "How long should your floss be before using?\n(1) 46 cm\n(2) 41 cm\n> ",
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

# question prompts that have been translated
maori_question_prompts = [
    "\n"
    "Kia pehea te roa o to paraihe?\n(1) 1 meneti\n(2) 2 meneti\n> ",
    "\n"
    "He aha te tino whaihua mo te horoi o te mangai?\n(1) Manawa kino\n(2) Rongonui\n> ",
    "\n"
    "Kia pehea te roa o to floss i mua i te whakamahinga?\n(1) 46 cm\n(2) 41 cm\n> ",
    "\n"
    "He aha te take o te pirau niho?\n(1) Waikawa\n(2) Kawhe\n> ",
    "\n"
    "He aha te take mo te Halitosis?\n(1) Arero huruhuru mangu\n(2) Manawa kino\n> ",
    "\n"
    "He aha te huarahi pai hei aukati i te mate kapia?\n(1) Tango tohu\n(2) Kiriuta fluoride\n> ",
    "\n"
    "Ahea me whakakapi nga paraihe niho?\n(1) 2 ki te 3 marama\n(2) 4 ki te 5 marama\n> ",
    "\n"
    ]

# list which will be iterated through
questions_maori = [
    Question(maori_question_prompts[0], "2"),
    Question(maori_question_prompts[1], "1"),
    Question(maori_question_prompts[2], "1"),
    Question(maori_question_prompts[3], "1"),
    Question(maori_question_prompts[4], "2"),
    Question(maori_question_prompts[5], "1"),
    Question(maori_question_prompts[6], "1")
    ]
    
# shuffles the questions
import random
random.shuffle(questions)
random.shuffle(questions_maori)


def run_game(questions, characters, language):
    """
    Runs the quiz so the user can use it
    """
    answer = ""
    health = 100
    ai_health = 100

    if language == "English":
        print("""=================================
START
=================================
Your health         |  {}% HP
Opponent health     |  {}% HP
=================================""".format(health, ai_health))

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
                ai_health = attacking(characters, ai_health, language)
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
                health = ai_attacking(characters, health, language)
                # if statement so the program knows when to show
                # the status of the players
                if health > 0:
                    print("""=================================
Your health         |  {}% HP
Opponent health     |  {}% HP
=================================""".format(health, ai_health))

    # option for run_game to be translated to maori
    elif language == "Maori":
        print("""=================================
Timata
=================================
To hauora           |  {}% HP
Hauora whakahee     |  {}% HP
=================================""".format(health, ai_health))

        for question in questions_maori:
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
                ai_health = attacking(characters, ai_health, language)
                # if statement so the program knows when to show
                # the status of the players
                if ai_health > 0:
                    print()
                    print("""=================================
To hauora           |  {}% HP
Hauora whakahee     |  {}% HP
=================================""".format(health, ai_health))
            else:
                # AI attacking function
                health = ai_attacking(characters, health, language)
                # if statement so the program knows when to show
                # the status of the players
                if health > 0:
                    print("""=================================
To hauora           |  {}% HP
Hauora whakahee     |  {}% HP
=================================""".format(health, ai_health))
        
                
    ending(characters, health, ai_health, language)
    

def ending(characters, health, ai_health, language):
    """
    End statements that gives the user an
    idea of who has won
    """
    
    # end statements that indicate who
    # has won and the health of both
    # parties
    if language == "English":
        print()
        print("---------------------------------")
        print()
        if health > ai_health or ai_health <= 0:
            print("""=================================
Your health         |  {}% HP
Opponent health     |  0% HP
=================================
Congratulations, {}, you have conquered bad dental hygiene :)""".format(health,
                                                                        characters[2]))
            print()
            print("Game over")
            
        elif health < ai_health or health <= 0:
            print("""=================================
Your health         |  0% HP
Opponent health     |  {}% HP
=================================
Sadly, {}, you have not be able to conquer bad dental hygiene :(""".format(ai_health,
                                                                           characters[2]))
            print()
            print("Game over")
            
        elif health == ai_health:
            print("""=================================
Your health         |  {}% HP
Opponent health     |  {}% HP
=================================
Weirdly, {}, you have tied with {}""".format(health,
                                             ai_health,
                                             characters[2],
                                             characters[1]))
            print()
            print("Game over")
            
        elif health < 0 and ai_health < 0:
            print("""=================================
Your health         |  {}% HP
Opponent health     |  {}% HP
=================================
Sadly, no one wins""".format(health, ai_health, characters[2], characters[1]))
            print()
            print("Game over")

    # if language chosen is Maori
    # prints this version instead
    elif language == "Maori":
        print()
        print("---------------------------------")
        print()
        if health > ai_health or ai_health <= 0:
            print("""=================================
To hauora           |  {}% HP
Hauora whakahee     |  0% HP
=================================
Kia ora, {}, kua wikitoria e koe te akuaku niho kino :)""".format(health,
                                                                  characters[2]))
            print()
            print("Kua mutu te kemu")
            
        elif health < ai_health or health <= 0:
            print("""=================================
To hauora           |  0% HP
Hauora whakahee     |  {}% HP
=================================
Te mea oto, {}, kaore i taea e koe te wikitoria i aku aku niho kino :(""".format(ai_health,
                                                                                 characters[2]))
            print()
            print("Kua mutu te kemu")
            
        elif health == ai_health:
            print("""=================================
To hauora           |  {}% HP
Hauora whakahee     |  {}% HP
=================================
Ngawari, {}, kua herea e koe ki {}""".format(health,
                                             ai_health,
                                             characters[2],
                                             characters[1]))
            print()
            print("Kua mutu te kemu")
            
        elif health < 0 and ai_health < 0:
            print("""=================================
To hauora           |  {}% HP
Hauora whakahee     |  {}% HP
=================================
Te mea pouri, kaore tetahi e wikitoria""".format(health, ai_health, characters[2], characters[1]))
            print()
            print("Kua mutu te kemu")


def attacking(characters, ai_health, language):
    """
    If user gets the answer correct they may
    choose an attack to use against the AI
    """
    # character movesets
    toothbrush = {"Poor Brush": 10, "Good Brush": 20, "Perfect Brush": 30}
    floss = {"Poor Floss": 10, "Good Floss": 20, "Perfect Floss": 30}
    mouthwash = {"Poor Mouthwash": 10, "Good Mouthwash": 20, "Perfect Mouthwash": 30}

    # character movesets in maori
    toothbrush_maori = {"Paraihe Korekore": 10, "Paraihe Pai": 20, "Paraihe Tino": 30}
    floss_maori = {"Moni Kore Koretake": 10, "Momo Puawai Pai": 20, "Mino Puawai": 30}
    mouthwash_maori = {"Korekore Mangu": 10, "Maama Ngahuru": 20, "Ngutu Kaha": 30}
        
    valid_input = ["1", "2", "3"]
    count = 0
    damage = 0
    choice = ""

    # if character chosen was 'Toothbrush'
    if characters[0] == "Toothbrush":
        print()
        if language == "English":
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
                damage = toothbrush["Poor Brush"]
                ai_health -= damage
            elif choice == "2":
                damage = toothbrush["Good Brush"]
                ai_health -= damage
            elif choice == "3":
                damage = toothbrush["Perfect Brush"]
                ai_health -= damage
                
        elif language == "Maori":
            print("Kōwhirihia he nekehanga")
            for move, damage in toothbrush_maori.items():
                count += 1
                print("({}) {} - {} DMG".format(count, move, damage))
            choice = input("> ")
            while not (choice in valid_input):
                print("Tena koa whakahoki mai me te '1', '2', te '3' ranei")
                choice = input("> ")
            # depending on the choice the damage
            # will be applied
            if choice == "1":
                damage = toothbrush_maori["Paraihe Korekore"]
                ai_health -= damage
            elif choice == "2":
                damage = toothbrush_maori["Paraihe Pai"]
                ai_health -= damage
            elif choice == "3":
                damage = toothbrush_maori["Paraihe Tino"]
                ai_health -= damage

    # if character chosen was 'Floss'
    if characters[0] == "Floss":
        print()
        if language == "English":
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
                damage = floss["Poor Floss"]
                ai_health -= damage
            elif choice == "2":
                damage = floss["Good Floss"]
                ai_health -= damage
            elif choice == "3":
                damage = floss["Perfect Floss"]
                ai_health -= damage

        elif language == "Maori":
            print("Kōwhirihia he nekehanga")
            for move, damage in floss_maori.items():
                count += 1
                print("({}) {} - {} DMG".format(count, move, damage))
            choice = input("> ")
            while not (choice in valid_input):
                print("Tena koa whakahoki mai me te '1', '2', te '3' ranei")
                choice = input("> ")
            # depending on the choice the damage
            # will be applied
            if choice == "1":
                damage = floss_maori["Moni Kore Koretake"]
                ai_health -= damage
            elif choice == "2":
                damage = floss_maori["Momo Puawai Pai"]
                ai_health -= damage
            elif choice == "3":
                damage = floss_maori["Mino Puawai"]
                ai_health -= damage

    # if character chosen was 'Mouthwash'
    if characters[0] == "Mouthwash":
        print()
        if language == "English":
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
                damage = mouthwash["Poor Mouthwash"]
                ai_health -= damage
            elif choice == "2":
                damage = mouthwash["Good Mouthwash"]
                ai_health -= damage
            elif choice == "3":
                damage = mouthwash["Perfect Mouthwash"]
                ai_health -= damage

        elif language == "Maori":
            print("Kōwhirihia he nekehanga")
            for move, damage in mouthwash_maori.items():
                count += 1
                print("({}) {} - {} DMG".format(count, move, damage))
            choice = input("> ")
            while not (choice in valid_input):
                print("Tena koa whakahoki mai me te '1', '2', te '3' ranei")
                choice = input("> ")
            # depending on the choice the damage
            # will be applied
            if choice == "1":
                damage = mouthwash_maori["Korekore Mangu"]
                ai_health -= damage
            elif choice == "2":
                damage = mouthwash_maori["Maama Ngahuru"]
                ai_health -= damage
            elif choice == "3":
                damage = mouthwash_maori["Ngutu Kaha"]
                ai_health -= damage
                

    # end statement which shows who is being attacked
    # and for how much damage
    if language == "English":
        print("""{} is being cleaned
Your attack was successful and did {} DMG""".format(characters[1],
                                                       damage))
    elif language == "Maori":
        print("""{} kei te horoia
I angitu to whakaekenga i te pai {} DMG""".format(characters[1],
                                                       damage))
    return ai_health
    

def ai_attacking(characters, health, language):
    """
    AI attacks
    """
    import random
    moveset = {"Attack 1": 10,
                "Attack 2": 20,
                "Attack 3": 30}
    damage = 0
    roll = 0

    # randomly rolls a number which will
    # dictate the attack
    roll = random.randint(1, 3)
    if roll == 1:
        damage = moveset["Attack 1"]
        health -= damage
    elif roll == 2:
        damage = moveset["Attack 2"]
        health -= damage
    elif roll == 3:
        damage = moveset["Attack 3"]
        health -= damage

    # indicates to the user what has happened
    if language == "English":
        print("""Your attack was unsuccessful
{} has done {} DMG to your teeth""".format(characters[1],
                                           damage))
    elif language == "Maori":
        print("""Kare i angitu to whakaeke
{} kua mahi {} DMG ki o niho""".format(characters[1],
                                           damage))
    return health

    
def main():
    """
    Runs the code
    """
    menu()
