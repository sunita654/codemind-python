n=int(input())
l=list(map(int,input().split(" ")))
if(len(set(l))!=1):print(len(l)-len(set(l))+1)
else:print(0)