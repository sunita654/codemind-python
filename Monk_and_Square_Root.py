import math
t=int(input())
for _ in range(t):
    m,n=map(int,input().split())
    count=0
    for i in range(int(math.floor(math.sqrt(m))),n//2+1):
        if(i*i)%n==m:
            print(i)
            count=1
            break
    if count==0:
        print(-1)
            