def isprime(num):
    if num > 1:
        for i in range(2, int(num/2)+1):
             if (num % i) == 0:
                  return False
                  break
        else:
              return True
  
    else:
         return False
n=int(input())
k=int(input())
for i in range(1,n+k):
    if(isprime(n+k+i)):
        print(i)
        break