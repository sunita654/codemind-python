n=int(input())
for k in range(n):
   s=input()
   c=0
   for i in s:
        if(i.isdigit()):c+=1
   if(c==len(s)):print("True")
   else:print("False")