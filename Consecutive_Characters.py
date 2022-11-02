s=input()
c=1
l=[]
for i in range(len(s)-1):
    if s[i]==s[i+1]:c+=1
    else:
        l.append(c)
        c=1
l.append(c)
print(max(l))