def checkDigits(n):
    n=str(n)
    c=0
    for i in n:
        if(i=="2" or i=="3" or i=="5" or i=="7"):c+=1
    if(c==len(n)):return 1
    return 0
def prime(n):
    if (n == 1):
        return 0
    i = 2
    while i * i <= n :
        if (n % i == 0):
            return 0
        i = i + 1
    return 1
def isFullPrime(n) :
    return (checkDigits(n) and prime(n))
n = int(input())
if(isFullPrime(n)) :
    print("Mega Prime")
else :
    print("Not Mega Prime")
 