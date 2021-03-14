# Split string method
import random
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
length=len(names)
val=random.randint(0,length-1)

print(f"{names[val]} is going to buy the meal today!")
