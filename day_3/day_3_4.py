# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
l1=name1.lower()
l2=name2.lower()
res=l1+l2
count_t=res.count('t')
count_r=res.count('r')
count_u=res.count('u')
count_e=res.count('e')
true=str(count_t+count_r+count_u+count_e)

count_l=res.count('l')
count_o=res.count('o')
count_v=res.count('v')
count_ee=res.count('e')
love=str(count_l+count_o+count_v+count_ee)

final_res=int(true+love)
if(final_res<10 or final_res>90):
  print(f"our score is {final_res}, you go together like coke and mentos.")

elif(final_res>=40 and final_res<=50):
  print(f"Your score is {final_res}, you are alright together.")

else:
  print(f"Your score is {final_res}")

