s=input()
c=0
for i in s:
    if(i.isupper()):c+=1
if(s[0].isupper()):print(c)
else:print(c+1)