c=0
p=1
s=input()
for i in s:
    c+=int(i)
    p*=int(i)
if(c==p):print("Spy Number")
else:print("Not Spy Number")