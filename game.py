import dice
import random



validInput = "no"           # Is set to "no" until the user enters either 'y' or 'n'.                                        
play = "y"                  # Users response when they are prompt if they would like to continue to play.
games = int(0)              # Incremental counter to keep a count for the number of games the user has played.
die1 = 0                    # Stores the random value from 1 to 6 for die 1.
die2 = 0                    # Stores the random value from 1 to 6 for die 2
die3 = 0                    # Stores the random value from 1 to 6 for die 3
die4 = 0                    # Stores the random value from 1 to 6 for die 4
die5 = 0                    # Stores the random value from 1 to 6 for die 5
ThreeCorrect = 0            # Incremental counter to keep track of consecutive correct guesses 
ThreeIncorrect = 0          # Incremental counter to keep track of consecutive incorrect guesses 
index = 1                   # Incremental counter used to display the numbers from 1-6 in the game summary 
score = int(0)              # Correct answer for the roll
userGuess = int(0)          # Stores the user's guess for the roll 
correctGuesses = int(0)     # Incremental counter for the number of correct guesses
incorrectGuesses = int(0)   # Incremental counter for the number of incorrect guesses
die_count = [0,0,0,0,0,0,0] # List to store the number of times each number has been rolled



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


# The loop asks whether the user wants to play the game and continues to loop until the user enters 'y' or 'n'.
while validInput== "no": 
    
    play = input("Would you like to play Petals Around the Rose [y|n]? ")

    if play == "y":
           
        # validInput is set to yes once the user has entered a valid input in order to terminate the loop.
        validInput = "yes" 
 
    elif play == "n":
        print()
        print()
        print("No worries... another time perhaps... :)")
        validInput= "yes"

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

    # These if-else statements determine whether the userGuess is correct and display the message accordingly.
    if userGuess == score: 
        print()
        print("Well Done! You guessed it!")
        print()
        print()

        #correctGuesses and ThreeCorrect is incremented by 1 each time the user gueses correctly.
        correctGuesses = correctGuesses + 1
        ThreeCorrect = 1 + ThreeCorrect

        # Each time the user guesses a correct answer, the ThreeIncorrect is set to 0. 
        ThreeIncorrect = 0 

        # If the user gets 3 guesses correct in a row, it displays a special message
        if ThreeCorrect % 3 == 0:
            print("Congratulations! You have worked out the secret!")
            print("Make sure you don't tell anyone!")
            print()
            print()

    
    else:
        print()

        if userGuess % 2 == 0:
            print("No sorry, it's ",score," not ",userGuess,".",sep = "")
            
        else:
            print("No sorry, it's ",score," not ",userGuess,". The score is always even.", sep = "")

        # incorrectGuesses and ThreeIncorrect is incremented by 1 each time the user gueses correctly.
        incorrectGuesses= incorrectGuesses + 1
        ThreeIncorrect = 1 + ThreeIncorrect

        # Each time the user guesses an incorrect answer, the ThreeCorrect is set to 0.
        ThreeCorrect = 0 

        # If the user gets 3 guesses incorrect in a row, it displays a message giving them a hint
        if incorrectGuesses % 3 == 0:
            print()
            print()
            print("Hint: The name of the game is important... Petals Around the Rose.")
        
        print()
        print()


    validInput ="n"

    # The while loop asks if the user wants to roll dice again and continues to loop unitl the user enters 'y' or 'n'.
    while validInput == "n":
        play = input("Roll dice again [y|n]? ")

        if play == "y":
            validInput= "y"

        # If the user doesn't want to roll dice again, then the game summary is displayed.
        elif play == "n":
            
            print()
            print()
            print("Game Summary")
            print("============")
            print()
            print("You played",games,"games:")
            print()
            print("  |--> Number of correct guesses:   ", correctGuesses)
            print("  |--> Number of incorrect guesses: ",incorrectGuesses)
            print()
            print()
            print("Dice Roll Stats:")
            print()
            print("Face  Frequency")
            
            # The While loop displays the number from 1 to 6. 
            while index < len(die_count):
                
                print("  ",index, end = "  ") 

                # The for loop repeats and displays a '*' for the number of time each die has been rolled.
                for number in range(die_count[index]):

                    print("*", end = "")

                print()
                index = index + 1

 
            print()
            print("Thanks for playing!")
            # As the user entered a valid input, validInput = "y" to terminate the loop. 
            validInput = "y"

        else:
            print("Please enter either 'y' or 'n'.")
            print()
            # validInput ="n" as the user didn't enter 'y' or 'n' 
            validInput = "n"
            
