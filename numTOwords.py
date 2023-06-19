#!/usr/bin/env python3
# Number to words 0 to 999
oneTOnine=["zero","one","two","three","four","five","six","seven","eight","nine"]
elTOnine=["eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
tenTOninty=["ten","twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]
hundred="hundred"
hundreden="hundreden"
num=int(input("Enter the number :"))

# 0 to 19

if (0<=num<=19):
    if 10<=num<=19:
       if num==10:
          print(tenTOninty[0])  # handle only 10
       else:
          print(elTOnine[num%10-1])
    else:
       print(oneTOnine[num])



# below equalent (num == 20 or num==30 or num==40 or num==50 or num==60 or num==70 or num==80 or num==90):
elif (10<=num<=90 and  num%10==0):
    print(tenTOninty[num//10-1])

elif (21<=num<=99):
    print(tenTOninty[num//10-1],oneTOnine[num%10])
elif (100<=num<=999):
    if (num%100==0):
        print(oneTOnine[num//100],hundred)
    twodigit=num%100

    temp=tenTOninty[0]
    if ( twodigit == 10 ):
        print(oneTOnine[num//100],hundred,tenTOninty[0])
    elif (11<=twodigit<=19):
        print(oneTOnine[num//100],hundred,elTOnine[twodigit%10-1])
    elif (twodigit%10==0):
        print(oneTOnine[num//100],hundred,tenTOninty[twodigit//10-1])
    elif (21<=twodigit<=99):
        print(oneTOnine[num//100],hundred,tenTOninty[twodigit//10-1],oneTOnine[twodigit%10])
# end #
