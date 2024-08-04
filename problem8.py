# Problem 8
# Jay Chen

import random   

# create a function to print result
def game_strategy(human, computer):
    if (human == "paper"):
        if (computer == "rock"):
            print("The computer choose %s, you win!" %(computer))
        elif (computer == "scissors"):
            print("Computer choose %s, the computer wins :("%(computer))
        else:
            print("The computer choose %s. Let's settle this."%(computer))
    elif (human == "rock"):
        if (computer == "scissors"):
            print("The computer choose %s, you win!" %(computer))
        elif (computer == "paper"):
            print("Computer choose %s, the computer wins :("%(computer))
        else:
            print("The computer choose %s. Let's settle this."%(computer))
    elif (human == "scissors"):
        if (computer == "paper"):
            print("The computer choose %s, you win!" %(computer))
        elif (computer == "rock"):
            print("Computer choose %s, the computer wins :("%(computer))
        else:
            print("The computer choose %s. Let's settle this."%(computer))               
        

game_set = ["paper", "rock", "scissors"]
choose = "y"

# a while loop for asking if user wants to play again
while choose == "y":
    user_input = input("Choose: ")
    computer_object = random.choice(["paper", "rock", "scissors"])
    if user_input not in game_set:
        print("You must choose paper, rock or scissors.")
        choose = input("Would you like to play again? ")       
    else:
        game_strategy(user_input,computer_object)
        if user_input == computer_object:
            break
        else:
            choose = input("Would you like to play again? ")

    if choose != "y":
        break


