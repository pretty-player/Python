# find neon number
def func(n):
    sqr=n*n
    sum=0
    while(sqr!=0):
        sum=sum+sqr%10
        sqr=sqr//10
    if(sum==n):
        return n
    else:
        return ""
for x in range(0,10000):
    print(func(x),end='')
    
# only 3 numbers are neon numbers 0,1,9
