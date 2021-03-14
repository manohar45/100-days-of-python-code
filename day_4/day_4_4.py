import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

val=[rock,paper,scissors]
length=len(val)
my_val=int(input("What do you choose? Type 0 for Rock,1 for Paper or 2 for Scissor?\n"))
comp_val=random.randint(0,length-1)

#logic

if(my_val==comp_val):
  print("No one wins")
elif(my_val==0 and comp_val==1):
  print("Computer wins")
elif(my_val==1 and comp_val==0):
  print("I won")
elif(my_val==0 and comp_val==2):
  print("i won")
elif(my_val==2 and comp_val==0):
  print("Compuetr wins")
elif(my_val==1 and comp_val==2):
  print("Computer wins")
elif(my_val==2 and comp_val==1):
  print("I won")
else:
  print("choose correct value")

