n=int(input())
l=list(map(int,input().split(" ")))
o=0
for i in l:
    if(i%2==0):o+=i
print(o)