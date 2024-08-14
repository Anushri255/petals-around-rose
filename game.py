import dice
import random

validInput = "no"
play = "y"
games = int(0)
die1 = 0
die2 = 0
die3 = 0
die4 = 0
die5 = 0
ThreeCorrect = 0
ThreeIncorrect = 0
index = 1
score = int(0)
userGuess = int(0)
correctGuesses = int(0)
incorrectGuesses = int(0)
die_count = [0,0,0,0,0,0,0]

# Adapted the description from wikipedia
print("Petals Around the Rose")
print("----------------------")
print()
print("The name of the game is 'Petals Around the Rose'. The name of the")
print("game is important. The computer will roll five dice and ask you to")
print("guess the score for the roll. The score will always be zero or an")
print("even number. Your mission, should you choose to accept it, is to")
print("work out how the computer calculates the score. If you succeed in")
print("working out the secret and guess correctly three times in a row, you")
print("become a Potentate of the Rose.")
print()

while validInput == "no":
    play = input("Would you like to play Petals Around the Rose [y|n]? ")
    if play == "y":
        validInput = "yes"
    elif play == "n":
        print()
        print()
        print("No worries... another time perhaps... :)")
        validInput = "yes"
    else:
        print("Please enter either 'y' or 'n'.")
        print()


# The loop continues until the user enters 'n' (i.e wants to stop rolling the dice)
while (play == 'y'): 

    # The dice are assigned a randomly generated number.
    die1 = random.randint(1,6)
    die2 = random.randint(1,6)
    die3 = random.randint(1,6)
    die4 = random.randint(1,6)
    die5 = random.randint(1,6)

    # The die_count list is updated by adding 1 to the index of the corresponding number that has been rolled.
    die_count[die1] = die_count[die1] + 1 
    die_count[die2] = die_count[die2] + 1
    die_count[die3] = die_count[die3] + 1
    die_count[die4] = die_count[die4] + 1
    die_count[die5] = die_count[die5] + 1

    # The dice are displayed using the display_dice function.
    dice.display_dice(die1,die2,die3,die4,die5) 
    
    userGuess = int(input("Please enter your guess for the roll: "))

    # The variable score is set to zero for each new game.
    score = 0 
    games = games + 1

    # The following if-elif statements calculate the correct score for each game.
    # If 3 is rolled, 2 is added to the score and if a 5 is rolled, 4 is added to the score.
    if die1 == 3:
        score = score + 2
    elif die1 == 5:
        score = score + 4

    if die2 == 3:
        score = score + 2
    elif die2 == 5:
        score = score + 4

    if die3 == 3:
        score = score + 2
    elif die3 == 5:
        score = score + 4

    if die4 == 3:
        score = score + 2
    elif die4 == 5:
        score = score + 4

    if die5 == 3:
        score = score + 2
    elif die5 == 5:
        score = score + 4