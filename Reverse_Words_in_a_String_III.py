l=list(map(str,input().split(" ")))
k=[]
for i in l:
    k.append(i[::-1])
print(" ".join(k))