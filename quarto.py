from datetime import datetime

d1 = datetime.strptime('20/04/1987 20:00:00', '%d/%m/%Y %H:%M:%S')
d2 = datetime.strptime('25/04/1987 22:33:00', '%d/%m/%Y %H:%M:%S')
dif = d2 - d1

print(d2.time())
print(dif)
print(dif.total_seconds())
print(dif.days)
