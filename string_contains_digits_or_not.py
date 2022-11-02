def mail(s):
    for i in s:
        if i.isdigit():return "Yes"
    return "No"
n=int(input())
for i in range(n):
    s=input()
    p=mail(s)
    print(p)