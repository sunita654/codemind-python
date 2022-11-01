n=input()
d=1
s=0
for i in n:
    s+=int(i)**d
    d+=1
if(int(n)==s):
    print("True")
else:
    print("False")
