print("Welcome to Python Pizza Deliveries!")
size=input("What size pizza do you want? S,M or L")
pepp=input("Do you want pepperoni?Y or N")
cheese=input("Do you want extra cheese?Y or N")
bill=0

if(size=='S'):
    bill=bill+15
elif(size=='M'):
    bill=bill+20
elif(size=='L'):
    bill=bill+25

if(pepp=='Y'):
    if(size=='S'):
        bill=bill+2
    elif(size=='M' or size=='L'):
        bill=bill+3

if(cheese=='Y'):
   bill=bill+1

print(f"The bill is {bill}") 

