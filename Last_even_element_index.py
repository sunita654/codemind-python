n=int(input())
l=list(map(int,input().split(" ")))
l.reverse()
p=1
for i in l:
    if (i%2==0):
        print(len(l)-p)
        break;
    p+=1