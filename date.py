#print next ten consecutive days
from datetime import*
d=date.today()
print(d)
d=date(2003,2,3)
for x in range(1,10):
    nextdate=d+timedelta(days=x) 