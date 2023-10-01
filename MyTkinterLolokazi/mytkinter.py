import sqlite3
from tkinter import *

db = sqlite3.connect('BigFail.db')
cur = db.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS lessons
            (name TEXT,
            max_count INT,
            min_age INT,
            max_age INT)
            """)


def create_master():
    with sqlite3.connect('BigFail.db') as con:
        cur = con.cursor()
        date = ent_1.get(), ent_2.get(), ent_3.get(), ent_4.get()
        cur.execute("""INSERT INTO lessons (name, max_count, min_age, max_age)
         VALUES (?,?,?,?)""", date)
        ent_1.delete(0, 'end')
        ent_2.delete(0, 'end')
        ent_3.delete(0, 'end')
        ent_4.delete(0, 'end')

root = Tk()

root.title('Tkinter')
root.geometry('500x400')
label = Label(text='Добро пожаловать,заристрируйтесь',)
label.place(x=150, y=5)

ent_1  = Entry(width=30)
ent_1.place(x=5, y=30)
ent_1.insert(0, 'Введите название мастер класса')

ent_2  = Entry(width=30)
ent_2.place(x=5, y=55)
ent_2.insert(0, 'Введите макс. кол-во человек')

ent_3  = Entry(width=30)
ent_3.place(x=5, y=80)
ent_3.insert(0, 'Введите минимальный возраст')

ent_4  = Entry(width=30)
ent_4.place(x=5, y=110)
ent_4.insert(0, 'Введите максимальный возраст')

button_create = Button(text='Создать', command=create_master)
button_create.place(x=200,y=130)




root.mainloop()