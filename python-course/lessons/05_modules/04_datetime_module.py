
# Birinci bölüm <---

# from datetime import date

# todaydate = date.today()

# print(todaydate)
# print(todaydate.day)
# print(todaydate.month)
# print(todaydate.year)
# print(todaydate.weekday())
# print(todaydate.isoweekday())

# historydate = date(2014,5,4)
# print("Eski tarih: ", historydate.weekday())

# --->


# İkinci bölüm <---

# from datetime import datetime # burada kullanılmamalı farkındayım fakat karışmasın diye yaptım

# nowdate = datetime.now()
# print("Şuan Tarih: ", nowdate)

# --->


# Üçüncü bölüm <---

from datetime import date
from datetime import datetime
from datetime import timedelta

nowdate2 = datetime.now()
tdelta = timedelta(days = 90, hours= 30, seconds = 90)
print(nowdate2 + tdelta)
print(nowdate2 - tdelta)

# --->