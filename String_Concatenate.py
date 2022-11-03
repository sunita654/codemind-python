s=input()
p=input()
l=[]
for i in s:
    l.append(i)
for i in p:
    l.append(i)
l.sort()
print("".join(l))