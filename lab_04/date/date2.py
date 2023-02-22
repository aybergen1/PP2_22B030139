import datetime
td = datetime.datetime.now()
yd = td.day-1
ttd = td.day+1
d = datetime.date(td.year, td.month, yd)
d2 = datetime.date(td.year, td.month, ttd)
d1 = datetime.date(td.year, td.month, td.day)
print(d,d1,d2)
