n=int(input())
l=list(map(int,input().split(" ")))
l=set(l)
if(n<3):print(max(l))
else:
    l.remove(max(l))
    l.remove(max(l))
    print(max(l))