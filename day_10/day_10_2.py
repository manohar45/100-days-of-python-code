import os

def add(n1,n2):
    return n1+n2

def sub(n1,n2):
    return n1-n2

def mult(n1,n2):
    return n1*n2

def div(n1,n2):
    return n1/n2


def start():
    dict={'+':add,'-':sub,'*':mult,'/':div}
    first=int(input("What's the first number ? :"))
    for op in dict:
        print(op)
    perform=True
    while perform:
        chosen_operation=input("Pick an operation : ")
        second=int(input("What's the next number? "))
        function=dict[chosen_operation]
        result=function(first,second)
        print(f"{first} {chosen_operation} {second} = {result}")
        val=input(f"Type 'y' to continue calculating with {result} or type 'n' to start a new calculation :")
        if(val=='y'):
            first=result
        elif(val=='n'):
            os.system('clear')
            perform=False
            start()

        
start()




