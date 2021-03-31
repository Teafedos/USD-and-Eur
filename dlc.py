import sqlite3
import matplotlib.pyplot as plt
import datetime
import matplotlib.dates as mdates

x, y, z = [], [], []
con = sqlite3.connect("course.db")
cur = con.cursor()
for i in cur.execute("SELECT * FROM curs"):
    x += [datetime.date(int(i[0][0:4]), int(i[0][5:7]), int(i[0][8:10]))]

    y += [float(i[1][6:8] + "." + i[1][9:11])]
    z += [float(i[2][5:7] + "." + i[2][8:10])]

print(y, z)

month = mdates.MonthLocator()
day = mdates.DayLocator()
timeFmt = mdates.DateFormatter("%Y-%m")
fig, ax = plt.subplots()
plt.plot(x, y)
plt.plot(x, z)
ax.xaxis.set_major_locator(month)
ax.xaxis.set_major_formatter(timeFmt)
ax.xaxis.set_minor_locator(day)

plt.show()