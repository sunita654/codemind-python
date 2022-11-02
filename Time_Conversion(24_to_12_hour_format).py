from datetime import datetime
d = datetime.strptime(input(), "%H:%M")
print(d.strftime("%I:%M %p"))