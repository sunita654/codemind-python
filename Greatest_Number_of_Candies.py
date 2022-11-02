n=int(input())
l=list(map(int,input().split(" ")))
p=int(input())
k=max(l)
for i in l:
    if(k<=i+p):print("True",end=" ")
    else:print("False",end=" ")
