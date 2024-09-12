# TODO : add play again

import random

def user_input():
    try:
        print("Make your choice to continue playing")
        user_choice = str(input("\n'S' : Stone\t'P' : Paper\t'X' : Scissor\n your input ==>\t"))
        print(user_choice)

    except:
        print("Invalid Input, exiting now . . .\n")
        exit()

    if user_choice.upper() == 'S':
        return 1
    
    elif user_choice.upper() == 'P':
        return 2
    
    elif user_choice.upper() == 'X':
        return 3
    
    elif (not user_choice.isalpha):
        print("Invalid Input, exiting now . . .\n")
        exit()

    else:
        return -999

def bot_choice():
    return random.randint(1,3)
    
def main():
    score = 0

    print("Win = +1 point\tLoss = -1 point")
    print("Starting Game Now...\n")
    while True:
        print(f">> Current score : {score}\n\n")
        u = user_input()
        bot = bot_choice()

        if u == -999:
            continue

        print(u)
        print(bot)
        if u == bot:
            print("\ndraw, no points\n")
        
        elif u == bot + 1 or bot - u == 2:
            score += 1
            print("\nVictory")
        
        else:
            score -= 1
            print("\nDefeat")


main()

