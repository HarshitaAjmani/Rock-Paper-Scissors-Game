import random

def comp(num):
    if(num == 1):
        print("Rock")
    elif(num == 2):
        print("Paper")
    elif(num == 3):
        print("Scissor")

def compare ( a, b):
    if( a == 1):
        if( b == 1): print(" \n\t It's a Tie :( ")
        elif( b == 2 ): print("\n\t YOU LOSE ")
        elif( b == 3): print(" \n\t YOU WON")
    elif( a == 2):
        if( b == 2): print(" \n\t It's a Tie :( ")
        elif( b == 3 ): print("\n\t YOU LOSE ")
        elif( b == 1): print(" \n\t YOU WON")
    elif( a == 3):
        if( b == 3): print(" \n\t It's a Tie :( ")
        elif( b == 1 ): print("\n\t YOU LOSE ")
        elif( b == 2): print(" \n\t YOU WON")



print("\n\n*** Lets Play Rock, Paper, Scissor Game ***")
n = 'y'
while( n == "y"):
    print("\n1.Rock\n2.Paper\n3.Scissor")
    sel = int(input("Enter a selection: "))
    temp = random.randint(1,3)
    if( sel == 1):
        print("\nYour Selection: \nRock")
        print("Computer's Selection: ")
        comp(temp)
        compare(sel,temp)
    elif( sel == 2):
        print("\nYour Selection: \nPaper")
        print("Computer's Selection: ")
        comp(temp)
        compare(sel,temp)
    elif( sel == 3):
        print("\nYour Selection: \nScissor")
        print("Computer's Selection: ")
        comp(temp)
        compare(sel,temp)
    else:
        print("\n\tX Invalid Input X")
    n = input("\nWant to play more? \nEnter  y ==> YES\nEnter x ==> EXIT")
