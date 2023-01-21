from os import system as sys
from platform import system
from time import sleep as slp
if system()=="Linux":
    clear="clear"
else:
    clear="cls"
dic={}
for x in range(1,51):
    dic[x]="*"
class preetyplayer:
    def home(self):
        try:
            sys(clear)
            what=int(input("\t\t1.Start Game\n\t\t2.Help\n\t\t3.MainManu\n\t\t4.Exit\n\t\tEnter what you want :"))
            if what==1:
                obj.game()
            elif what==2:
                obj.help()
            elif what==3:
                obj.mainmanu()
            elif what==4:
                obj.exi()
            else:
                print("This is not valid...")
                slp(2)
                obj.home()
        except(ValueError):
            print("Press Only Numbers 1,2")
            slp(1)
            obj.home()
    def help(self):
        helpp='''********** WELCOME HELP PAGE **********
                This is number based object moving game we only
                insert the box number after we can move our object
                on the particular place and put our thing
                
                
                 ****************************************
                |        BOARD NUMBER SYSTEM             |
                 ****************************************        
            
                -----------------------------------------
                |01 |02 |03 |04 |05 |06 |07 |08 |09 |10 |
                |___|___|___|___|___|___|___|___|___|___|
                |11 |12 |13 |14 |15 |16 |17 |18 |19 |20 |
                |___|___|___|___|___|___|___|___|___|___|
                |21 |22 |23 |24 |25 |26 |27 |28 |29 |30 |
                |___|___|___|___|___|___|___|___|___|___|
                |31 |32 |33 |34 |35 |36 |37 |38 |39 |40 |
                |___|___|___|___|___|___|___|___|___|___|
                |41 |42 |43 |44 |45 |46 |47 |48 |49 |50 |
                |___|___|___|___|___|___|___|___|___|___| '''
        print(helpp)
        slp(10)
        obj.mainmanu()
    def initial(self):
        for x in range(0,51):
            dic[x]="*"
        obj.game()
    def game(self):
        sys(clear)
        #for x in range(0,51):
        #    dic[x]="*"
        print("-------------------------------")
        print("|"+dic[1]+" |"+dic[2]+" |"+dic[3]+" |"+dic[4]+" |"+dic[5]+" |"+dic[6]+" |"+dic[7]+" |"+dic[8]+" |"+dic[9]+" |"+dic[10]+" |")
        print("|__|__|__|__|__|__|__|__|__|__|")
        print("|"+dic[11]+" |"+dic[12]+" |"+dic[13]+" |"+dic[14]+" |"+dic[15]+" |"+dic[16]+" |"+dic[17]+" |"+dic[18]+" |"+dic[19]+" |"+dic[20]+" |")
        print("|__|__|__|__|__|__|__|__|__|__|")
        print("|"+dic[21]+" |"+dic[22]+" |"+dic[23]+" |"+dic[24]+" |"+dic[25]+" |"+dic[26]+" |"+dic[27]+" |"+dic[28]+" |"+dic[29]+" |"+dic[30]+" |")
        print("|__|__|__|__|__|__|__|__|__|__|")
        print("|"+dic[31]+" |"+dic[32]+" |"+dic[33]+" |"+dic[34]+" |"+dic[35]+" |"+dic[36]+" |"+dic[37]+" |"+dic[38]+" |"+dic[39]+" |"+dic[40]+" |")
        print("|__|__|__|__|__|__|__|__|__|__|")
        print("|"+dic[41]+" |"+dic[42]+" |"+dic[43]+" |"+dic[44]+" |"+dic[45]+" |"+dic[46]+" |"+dic[47]+" |"+dic[48]+" |"+dic[49]+" |"+dic[50]+" |")
        print("|__|__|__|__|__|__|__|__|__|__|")
        try:
            box=int(input("Enter Box Number :"))
            if dic[box]=="*":
                dic[box]="o"
                obj.game()
            elif dic[box]=="o":
                i=1
                print("This is box already filled...")
                slp(2)
                for x in range(1,51):
                    if dic[x]!="*":
                        i+=1
                    else:
                        obj.game()
                if 50<=i:
                    print("You completely filled all box")
                    slp(2)
                    if (input("You want restart (y,n) :")=="y" | "Y"):
                        obj.initial()
                    else:
                        obj.mainmanu()
                else:
                    obj.game()
                slp(2)
                obj.game()
            else:
                dic[box]="o"
        except(ValueError):
            print("Sorry dear only box number's allowled...")
            slp(1)
            obj.game()
        except(KeyError):
            if box==111:
                obj.mainmanu()
            else:
                print("Only have 50 box...")
            slp(2)
            obj.game()
    def mainmanu(self):
        obj.home()
    def exi(self):
        exit()
if __name__=="__main__":
    obj=preetyplayer()
    obj.home()
