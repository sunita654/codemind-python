n=input()
c=0
p=1
for i in n:
    c+=int(i)
    p*=int(i)
print(p-c)