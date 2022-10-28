def isPrime(num):
    flag = False
    if num > 1:
        for i in range(2, num):
              if (num % i) == 0:
                     flag = True
                     break
    return flag
n=int(input())
k=str(n)
if isPrime(n):
     print("not prime")
else:
    if(isPrime(int(k[::-1]))):print("prime but not a circular prime")
    else:print("circular prime")