import random
text = """next weekend  the week after next  before too long  in two weeks' time  the day after tomorrow
later today  four years from now  in the near future  venue
publicity  so do I  nor do I  neither do I  draw up a guest list  pay a deposit
organise the food  decorate the room  choose a theme  get permission  choose a theme  get permission  hire a DJ   send out invitations
be responsible for  put something up  sorry about  think about  about 10 o'clock  what about you  forget about  about to  hologram  robot  transplant  technology  poverty"""
text = text.lower()
woorden = text.split("  ")
plaatjes = [

    """
________
""",
    """
    |
    |
    |
    |
____|____
""",
    """
    ______
    |
    |
    |
    |
____|____
""",
    """
    ______
    |    |
    |
    |
    |
____|____
""",
    """
    ______
    |    |
    |    o
    |
    |
____|____
""",
    """
    ______
    |    |
    |    o
    |   /|\\
    |   / \\
____|____
"""]


Answer_Galgje = woorden[random.randrange(len(woorden))]
print("Welcome to Hangman!")
All_correct = ""
Fouten = 0
klaar = 0
pogingen = []


def Display_galg():
    global Fouten, klaar

    print("Wrong! Try again.")
    print(plaatjes[Fouten])
    Fouten += 1
    if Fouten == len(plaatjes):
        print("GAME OVER!")
        klaar = 1
        print("The word was: " + Answer_Galgje)


while klaar == 0:
    soort_input = input(
        "Guess one letter or space or a whole word. For a letter type: a letter, for a word type: '?'")
    if soort_input != "?":
        guess = soort_input
        if len(guess) > 1:
            print("Not more than one at a time!")
        else:
            if guess in pogingen:
                print("You've already tried that!")
            else:
                pogingen.append(guess)
                allesgoed = True
                if guess in Answer_Galgje:
                    print("Nice!")
                    All_correct = All_correct + guess

                else:
                    Display_galg()

                # hier word het woord met streepjes getoont en kijkt hij naar de All_correct string om te kijken naar welke letters de speler al heeft geraden
                # hij kijkt of er nog letters niet geraden zijn, anders is alles goed en stopt hij het spel
                Display = ("")
                for letter in Answer_Galgje:
                    if letter in All_correct:
                        Display = Display + letter + " "
                    else:
                        Display = Display + "_" + " "
                        allesgoed = False
                print(Display)
                if allesgoed:
                    print("You WON!")
                    klaar = 1
    else:
        guess = input("What word?")
        if guess == Answer_Galgje:
            print("You WON!")
            klaar = 1
        else:
            Display_galg()