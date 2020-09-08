##
# dental_rpg.py
# 24/08/20
# Anthony D


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
    username = input("Enter your name\n>>> ").lower().title().strip()
    while username == EMPTY:
        print("Please enter a name")
        username = input("Enter your name\n>>> ").lower().title().strip()

    # asks the user to input their favored
    # character
    print()
    for character in user_characters:
        print(character)
    while not(choice in valid_input):
        choice = input("Please choose a character\n>>> ")
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

question_prompts = [
    "How long should you brush your teeth?\n(a) 1 minute\n(b) 2 minutes\n>>> ",
    "\n"
    "What is mouthwash most effective against?\n(a) Bad breath\n(b) Cavities\n>>> ",
    "\n"
    "How long should your floss be before using?\n(a) 18 inches\n(b) 16 inches\n>>> ",
    "\n"
    ]

questions = [
    Question(question_prompts[0], "b"),
    Question(question_prompts[1], "a"),
    Question(question_prompts[2], "a")
    ]


def run_quiz(questions, characters):
    """
    Runs the quiz so the user can use it
    """
    score = 0
    ai_score = 0
    # health of both user and ai is based on
    # the length of the quiz
    # whoever wins the most rounds wins
    health = len(questions)
    ai_health = len(questions)

    print("START\n")
    
    for question in questions:
        answer = input(question.prompt).lower().strip()
        if answer == question.answer:
            print("You are correct")
            ai_health -= 1
            print("""\n{1} is being cleaned
{0}({2}) is on {4} health
{1} is on {3} health""".format(characters[0], characters[1], characters[2], ai_health, health))
            score += 1
        else:
            print("You are incorrect")
            health -= 1
            print("""\nYour teeth have been damaged
{0}({2}) is on {4} health
{1} is on {3} health""".format(characters[0], characters[1], characters[2], ai_health, health))
            ai_score += 1

    print("\nYou scored {} out of {}".format(score, len(questions)))

    if score > ai_score:
        print("{}, you have conquered bad dental hygiene".format(characters[2]))
    elif score < ai_score:
        print("{}, you have not been able to conquer bad dental hygiene :(".format(characters[2]))

    return score


def main():
    """
    Runs the code
    """
    characters = character_select()
    print()
    run_quiz(questions, characters)
    print()
    print("Game Over")
