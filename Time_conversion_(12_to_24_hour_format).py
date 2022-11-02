from datetime import datetime
m2 = input()
i= datetime.strptime(m2, "%I:%M %p")
o = datetime.strftime(i, "%H:%M")
print(o)