import requests
import re
import tkinter as tk
import os
import datetime
import sqlite3
sea = r'<div class="col-md-2 col-xs-9 _right mono-num">\d+.\d\d'
name = requests.get('https://cbr.ru')
if name.status_code == 200:
    matcher = re.findall(sea, name.text)
    usd = matcher[0][47:52]
    used = 'USD: ' + ' ' + usd + ' ' + 'RUB'
    eur = matcher[2][47:52]
    used1 = 'EUR:' + ' ' + eur + ' ' + 'RUB'



win = tk.Tk()

win.title('Курс доллара и евро')
win.geometry('300x200+600+300')
win.resizable(False, False)
label_1 = tk.Label(win, text=used, font=('' , 24, 'bold'), pady=30)
label_1.pack()
label_2 = tk.Label(win, text=used1, font=('' , 24, 'bold'), pady=30)
label_2.pack()
win.mainloop()

con = sqlite3.connect('course.db')
cur = con.cursor()
cur.execute(""" CREATE TABLE IF NOT EXISTS curs(
    data TEXT,
    Dollar REAL,
    Euro REAL
    )
""")
con.commit()

day = datetime.date.today()
abc = (str(day), used, used1)
cur.execute("""SELECT data FROM curs""")
spis = cur.fetchall()
new_spis = []
for j in spis:
    new_spis += [j[0]]
if spis != None:
    if str(day) not in new_spis:
        print(day, spis)
        cur.execute("INSERT INTO curs VALUES(?, ?, ?)", abc)
        con.commit()
    else:
        print(new_spis)
else:
    print(type(spis))
    cur.execute("""INSERT INTO curs VALUES(?, ?, ?)""", abc)
    con.commit()

for i in cur.execute("SELECT * FROM curs"):
    print(i)
con.close()