num=input()
l=[]
for i in num:
    l.append(i)
for i in range(len(l)):
    if(l[i]=="6"):
        l[i] = "9"
        break
print("".join(l))