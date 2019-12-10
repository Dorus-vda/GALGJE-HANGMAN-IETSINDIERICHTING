import random
text = ['next weekend', 'the week after next', 'before too long', 'in two weeks time', 'the day after tomorrow', 'later today', 'four years from now', 'in the near future', 'venue', 'publicity', 'so do i', 'nor do i', 'neither do i', 'draw up a guest list', 'pay a deposit', 'organise the food', 'decorate the room', 'choose a theme', 'get permission', 'hire a DJ', 'send out invitations', 'be responsible for', 'put something up', 'sorry about', 'think about', 'about 10 o clock', 'what about you', 'forget about', 'about to', 'hologram', 'robot', 'transplant', 'technology', 'poverty']
woorden = text
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
    |  
____|____
 """ 
    ,
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
    if Answer_Galgje == "next weekend":
        print("The defenition of the word is: the next Saturday and Sunday")
    elif Answer_Galgje == "the week after next":
        print("The defenition of the word is: the week that is the first one after next week")
    elif Answer_Galgje == "before too long":
        print("The defenition of the word is: soon")
    elif Answer_Galgje == "in two weeks time":
        print("The defenition of the word is: about fourteen days from now")
    elif Answer_Galgje == "the day after tomorrow":
        print("The defenition of the word is: not the next day but the day after that")
    elif Answer_Galgje == "later today":
        print("The defenition of the word is: at a later time on this day")
    elif Answer_Galgje == "four years from now":
        print("The defenition of the word is: four years after the present time")
    elif Answer_Galgje == "in the near future":
        print("The defenition of the word is: at a time that is not far away")
    elif Answer_Galgje == "venue":
        print("The defenition of the word is: a place where a sports game, musical performance, or special event happens")
    elif Answer_Galgje == "publicity":
        print("The defenition of the word is: advertising or information about someone or something in the newspaper, on television, etc.")
    elif Answer_Galgje == "so do I":
        print("The defenition of the word is: used for agreeing with a statement")
    elif Answer_Galgje == "nor do I":
        print("The defenition of the word is: used for agreeing with a negative statement")
    elif Answer_Galgje == "neither do I":
        print("The defenition of the word is: used for agreeing with a negative statement")
    elif Answer_Galgje == "draw up a guest list":
        print("The defenition of the word is: to decide who you want to invite to a party")
    elif Answer_Galgje == "pay a deposit":
        print("The defenition of the word is: to pay part of the cost of something before you pay the rest")
    elif Answer_Galgje == "organise the food":
        print("The defenition of the word is: to make arrangements to buy the things you will eat")
    elif Answer_Galgje == "decorate the room":
        print("The defenition of the word is: to add things to the room to make it look more attractive")
    elif Answer_Galgje == "choose a theme":
        print("The defenition of the word is: to choose a particular subject for a party and ask people to dress in a particular type of clothes")
    elif Answer_Galgje == "get permission":
        print("The defenition of the word is: someone says that they will allow you to do something")
    elif Answer_Galgje == "hire a DJ":
        print("The defenition of the word is: to arrange for someone to come and put on music at an event")
    elif Answer_Galgje == "send out invitations":
        print("The defenition of the word is: to post cards that invite people to an event such as a party")
    elif Answer_Galgje == "be responsible for":
        print("The defenition of the word is: to be the person whose duty is to deal with something")
    elif Answer_Galgje == "put something up":
        print("The defenition of the word is: to fasten something to a wall or ceiling")
    elif Answer_Galgje == "sorry about":
        print("The defenition of the word is: used to apologise for something")
    elif Answer_Galgje == "think about":
        print("The defenition of the word is: to consider something")
    elif Answer_Galgje == "about 10 o clock":
        print("The defenition of the word is: approximately ten o'clock")
    elif Answer_Galgje == "what about you":
        print("The defenition of the word is: used to ask for someone's opinion")
    elif Answer_Galgje == "forget about":
        print("The defenition of the word is: to not remember something")
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
                    if letter == " ":
                        Display = Display + "   "
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