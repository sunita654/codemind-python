e=0
o=0
m=0
s=input()
for i in s:
    if(int(i)%2==0):e+=1
    elif(int(i)%2!=0):o+=1
    else:m+=1
if(e==len(s)):print("Even")
elif(o==len(s)):print("Odd")
else:print("Mixed")