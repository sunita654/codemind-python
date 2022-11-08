n=int(input())
l=list(map(int,input().split(" ")))
o=0
for i in range(1,n,2):o+=l[i]
print(o)