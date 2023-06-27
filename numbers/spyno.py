#spynumber
def spyno(n):
    org=n
    sum=0
    mul=1
    while (n!=0):
        digit=n%10
        sum+=digit
        mul*=digit
        n//=10
    if (sum==mul):
        return True  # org
    else:
        return False # ""

n=int(input("Enter the number :"))
print((spyno(n))
'''
for x in range(0,10000):
    print(spyno(x),end=".")
'''
