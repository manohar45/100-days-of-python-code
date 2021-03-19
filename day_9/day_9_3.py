import os
print("Welcome to the secret auction program.")
dict={}
name=input("What is your name ? ")
bid=int(input("What's your bid ? "))
val=input("Are there any other bidders? Type 'yes' or 'no'.")
dict[name]=bid
flag=True
while flag:
    if(val=='yes'):
        os.system('clear')
        name=input("What is your name ? ")
        bid=int(input("What's your bid ? "))
        dict[name]=bid
        val=input("Are there any other bidders? Type 'yes' or 'no'.")
    elif(val=='no'):
        os.system('clear')
        flag=False
        maxi=0;
        for i in dict:
            prices=dict[i]
            if(prices>maxi):
                maxi=prices
                name=i;
        print(f"The winner of the bid is {name} with a bid of {maxi}")

