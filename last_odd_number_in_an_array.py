n=int(input())
l=list(map(int,input().split(" ")))
l.reverse()
for i in l:
    if(i%2!=0):
        print(i)
        break