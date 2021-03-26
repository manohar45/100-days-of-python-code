from art import logo
import random

EASY=10
HARD=5

def setdificulty(diff):
    if (diff=='easy'):
        return EASY
    elif (diff=='hard'):
        return HARD

def check_answer(guess,answer,turns):
    if(guess>answer):
        print("Too high !")
        return turns-1
    elif(guess<answer):
        print("Too low !")
        return turns-1
        




def game():
    print(logo)
    print("Welcome to the number guessing game!")
    print("I'm thinking of a number between 1 and 100 ")
    diff=input("Choose a dificulty level between 'easy' and 'hard':")
    turns=setdificulty(diff)
    answer=random.randint(1,101)
    print(f"The number is {answer}")
    guess=0
    while(guess!=answer):
        print(f"You have {turns} attempts remaining to guess the number ")
        guess=int(input("Make a guess : "))
        turns=check_answer(guess,answer,turns)
        if(turns==0):
            print("You run out of guess!")
            return
        elif(guess==answer):
            print("you win!")
        else:
            print("Guess again !")


game()