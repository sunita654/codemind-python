n=int(input())
for i in range(n):
    p=int(input())
    k=1
    for j in range(1,p+1):
        k*=j
    print(k)