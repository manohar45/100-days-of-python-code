import random
from hangman_art import logo,stages
from hangman_words import word_list

chosen_word=random.choice(word_list)
word_len=len(chosen_word)

print(f"The random word is : {chosen_word}")
lives=6
end_of_game=False
display=[]
for i in range(word_len):
    display.append('_')

while not end_of_game:
    guess=input("Guess a letter : ")
    for p in range(word_len):
        letter=chosen_word[p]
        if(letter == guess):
            display[p]=letter
    
    print(display)
    if guess not in chosen_word:
        lives=lives-1
        if(lives==0):
            print("You loose")
            end_of_game=True


    if '_' not in display:
        print("You win")
        end_of_game=True
    
    print(stages[lives])
