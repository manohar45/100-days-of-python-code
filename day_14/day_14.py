import random
from art import logo,vs
from game_data import data
import os


def compute(choice_a,choice_b,choice):
    mychoice=choice.lower()
    if(choice_a['follower_count']>choice_b['follower_count']):
        return mychoice=='a'
    else:
        return mychoice=='b'
        

score=0
print(logo)
size=len(data)
val_b=random.randint(0,size-1)
play=True
while play:    
    #print(f"Your score is {score}")
    val_a=val_b
    choice_a=data[val_a]
    print(f"Compare A: {choice_a['name']}, a {choice_a['description']}, from {choice_a['country']}")

    print(vs)

    
    val_b=random.randint(0,size-1)
    if(val_a==val_b):
        val_b=random.randint(0,size-1)
    
    choice_b=data[val_b]
    print(f"Compare B: {choice_b['name']}, a {choice_b['description']}, from {choice_b['country']}")
    choice=input("Who has more followers ? Type 'A' or 'B':")
    guess=compute(choice_a,choice_b,choice)
    os.system('clear')
    if(guess):
        score=score+1
        print(f"You are right! Score is :{score}")
        
    else:
        print(f"Sorry thats wrong :Final score is {score}")
        play=False
        





