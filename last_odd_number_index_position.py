n=int(input())
l=list(map(int,input().split(" ")))
l.reverse()
for i in l:
    p=1
    if(i%2!=0):
        print(len(l)-p)
        break
    p+=1