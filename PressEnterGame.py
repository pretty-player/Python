from random import randint as rt
from time import sleep as s
from os import system as sy
from platform import system
if system()=="Linux":
    clear="clear"
else:
    clear="cls"
#Python dice game
tap="\t\t\t"
def one(a):
    print(tap+" _____")
    print(tap+"|     |")
    print(tap+"|  %d  |"%a)
    print(tap+"|_____|")
    s(1.9) 
uname=input("Enter Your Name Here:")
count=1
while True: 
    try:
        sy(clear)
        print("Player 1:System... \t\t\t%d round"%count)
        s(1.3)
        sys=int(rt(1,6))
        one(sys)
        cho=input("Player 2:%s:\t\t\tSimply press enter"%uname) #Simple Press Enter For Player 2 OtherWise Leave the Game...
        glo=int(rt(1,3))
        if cho=="" or cho=="":
            if sys==glo:
                print(tap+" _____")
                print(tap+"|     |")
                print(tap+"|  %d  |"%sys)
                print(tap+"|_____|")
                print("\n\t\t\tWOW!!! DEAR:%s YOU WON THE MATCH"%uname)
                if count==1:
                    print("Your Are Lucky Guy")
                elif count>=3:
                    print("Nice To Meet You")
                else:
                    print("Good Lucky Dears")
                break
            else:
                count+=1
                one(glo)
        else:
            exit()
    except(Exception):
        print("Error",Exception)
        break
