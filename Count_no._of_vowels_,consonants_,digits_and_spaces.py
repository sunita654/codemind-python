s=input()
v=0
c=0
d=0
ws=0
l=["a","e","i","o","u","A","E","I","O","U"]
for i in s:
    if(i.isdigit()):d+=1
    elif(i in l):v+=1
    elif(i==" "):ws+=1
    else:c+=1
print("Vowels:",v)
print("Consonants:",c)
print("Digits:",d)
print("White spaces:",ws)