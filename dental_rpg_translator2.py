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

    print("Welcome to Dental RPG")
    while not(choice in valid_input):
        choice = input("""Please choose an option:
(1) Start game
(2) Translate keywords to Te Reo
(3) Quit
> """)

    if choice == "1":
        characters = character_select()
        print()
        run_game(questions, characters)
    elif choice == "2":
        print("bruh")
    elif choice == "3":
        quit
        
    

def character_select():
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
    "How long should you brush your teeth?\n(a) 1 minute\n(b) 2 minutes\n> ",
    "\n"
    "What is mouthwash most effective against?\n(a) Bad breath\n(b) Cavities\n> ",
    "\n"
    "How long should your floss be before using?\n(a) 18 inches\n(b) 16 inches\n> ",
    "\n"
    "What causes tooth decay?\n(a) Acid\n(b) Caffeine\n> ",
    "\n"
    "What is Halitosis the medical term for?\n(a) Black hairy tongue\n(b) Bad breath\n> ",
    "\n"
    "What is the best way prevent gum disease?\n(a) Remove plaque\n(b) Flouride toothpaste\n> ",
    "\n"
    "When should toothbrushes be replaced?\n(a) 2 to 3 months\n(b) 4 to 5 months\n> ",
    "\n"
    ]

translated_question_prompts = [
    "\n"
    "How long should you PARAIHE/brush your NIHO/teeth?\n(a) 1 meneti\n(b) 2 meneti\n> ",
    "\n"
    "What is HOROI HOROI MANGAI/mouthwash most effective against?\n(a) Manawa kino\n(b) Rongonui\n> ",
    "\n"
    "How long should your NGARU/floss be before using?\n(a) 46 cm\n(b) 41 cm\n> ",
    "\n"
    "What causes TOTI TE TAI/tooth decay?\n(a) Waikawa\n(b) Kawhe\n> ",
    "\n"
    "What is Halitosis the medical term for?\n(a) Arero huruhuru mangu\n(b) Manawa kino\n> ",
    "\n"
    "What is the best way prevent MATE KAPIA/gum disease?\n(a) Tango tohu\n(b) Kiriuta fluoride\n> ",
    "\n"
    "When should your PARAIHE NIHO/toothbrush be replaced?\n(a) 2 ki te 3 marama\n(b) 4 ki te 5 marama\n> ",
    "\n"
    ]

# list will will be iterated through
questions = [
    Question(question_prompts[0], "b"),
    Question(question_prompts[1], "a"),
    Question(question_prompts[2], "a"),
    Question(question_prompts[3], "a"),
    Question(question_prompts[4], "b"),
    Question(question_prompts[5], "a"),
    Question(question_prompts[6], "a")
    ]

# list will will be iterated through
translated_questions = [
    Question(translated_question_prompts[0], "b"),
    Question(translated_question_prompts[1], "a"),
    Question(translated_question_prompts[2], "a"),
    Question(translated_question_prompts[3], "a"),
    Question(translated_question_prompts[4], "b"),
    Question(translated_question_prompts[5], "a"),
    Question(translated_question_prompts[6], "a")
    ]

# shuffles the questions
import random
random.shuffle(questions)
random.shuffle(translated_questions)


def run_game(questions, characters):
    """
    Runs the quiz so the user can use it
    """
    answer = ""
    health = 100
    ai_health = 100

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
        while answer != "a" and answer != "b":
            print("Please answer with 'a' or 'b'")
            print()
            answer = input(question.prompt).lower().strip()
        if answer == question.answer:
            # user attacking function which allows them to
            # select the move they would like to use
            ai_health = attacking(characters, ai_health)
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
            health = ai_attacking(characters, health)
            # if statement so the program knows when to show
            # the status of the players
            if health > 0:
                print("""=================================
Your health         |  {}% HP
Opponent health     |  {}% HP
=================================""".format(health, ai_health))
                
    # end statements that indicate who
    # has won and the health of both
    # parties
    print()
    print("---------------------------------")
    print()
    if health > ai_health and (ai_health < 0 or ai_health == 0):
        print("""=================================
Your health         |  {}% HP
Opponent health     |  0% HP
=================================
Congratulations, {}, you have conquered bad dental hygiene :)""".format(health,
                                                                        characters[2]))
    elif health < ai_health and (health < 0 or health == 0):
        print("""=================================
Your health         |  0% HP
Opponent health     |  {}% HP
=================================
Sadly, {}, you have not be able to conquer bad dental hygiene :(""".format(ai_health,
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
    elif health < 0 and ai_health < 0:
        print("""=================================
Your health         |  {}% HP
Opponent health     |  {}% HP
=================================
Sadly, no one wins""".format(health, ai_health, characters[2], characters[1]))


def attacking(characters, ai_health):
    """
    If user gets the answer correct they may
    choose an attack to use against the AI
    """
    # character movesets
    toothbrush = {"Poor Brush": 10,
                  "Good Brush": 20,
                  "Perfect Brush": 30}
    floss = {"Poor Floss": 10,
             "Good Floss": 20,
             "Perfect Floss": 30}
    mouthwash = {"Poor Mouthwash": 10,
                 "Good Mouthwash": 20,
                 "Perfect Mouthwash": 30}
    valid_input = ["1", "2", "3"]
    count = 0
    damage = 0
    choice = ""

    # if character chosen was 'Toothbrush'
    if characters[0] == "Toothbrush":
        print()
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

    # if character chosen was 'Floss'
    if characters[0] == "Floss":
        print()
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

    # if character chosen was 'Mouthwash'
    if characters[0] == "Mouthwash":
        print()
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

    # end statement which shows who is being attacked
    # and for how much damage
    print("""{} is being cleaned
Your attack was successful and did {} DMG""".format(characters[1],
                                                       damage))
    return ai_health
    

def ai_attacking(characters, health):
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
    print("""Your attack was unsuccessful
{} has done {} DMG to your teeth""".format(characters[1],
                                           damage))
    return health

    
def main():
    """
    Runs the code
    """
    menu()
    print()
    print("Game Over")
