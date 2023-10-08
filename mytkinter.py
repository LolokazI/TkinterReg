import sqlite3
from tkinter import Entry, Tk, Label, Button
from tkinter.messagebox import showinfo


db = sqlite3.connect('Tkinter_users.db')
cur = db.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS lessons(
            name TEXT,
            max_count INT,
            min_age INT,
            max_age INT
            )""")


root = Tk()

root.title('Tkinter')
root.geometry('650x400')
label = Label(text='Здравстуйте! Чтобы зарегистироваться на мастер класс'
              + ' введите его название, свое имя и возраст',)
root.resizable(False, False)
label.place(x=40, y=5)


def entry_registration_name_master_class_focus(event):
    name: str = 'Введите назнание желаемого мастер класса'
    if entry_registration_name_master_class.get() == name:
        entry_registration_name_master_class.delete(0, "end")


def entry_registration_name_master_class_not_focus(event):
    if entry_registration_name_master_class.get() == '':
        entry_registration_name_master_class.insert(
            0, "Введите назнание желаемого мастер класса")


entry_registration_name_master_class = Entry(root, width=41)
entry_registration_name_master_class.place(x=40, y=40)

entry_registration_name_master_class.insert(
    0, 'Введите назнание желаемого мастер класса')

entry_registration_name_master_class.bind(
    "<FocusIn>", entry_registration_name_master_class_focus)

entry_registration_name_master_class.bind(
    "<FocusOut>", entry_registration_name_master_class_not_focus)


def entry_registration_name_focus(event):
    if entry_registration_name.get() == 'Введите свое имя':
        entry_registration_name.delete(0, "end")


def entry_registration_name_not_focus(event):
    if entry_registration_name.get() == '':
        entry_registration_name.insert(0, 'Введите свое имя')


entry_registration_name = Entry(width=41)
entry_registration_name.place(x=40, y=65)
entry_registration_name.insert(0, 'Введите свое имя')
entry_registration_name.bind("<FocusIn>", entry_registration_name_focus)
entry_registration_name.bind("<FocusOut>", entry_registration_name_not_focus)


def entry_registration_age_focus(event):
    if entry_registration_age.get() == 'Введите свой возраст':
        entry_registration_age.delete(0, "end")


def entry_registration_age_not_focus(event):
    if entry_registration_age.get() == "":
        entry_registration_age.insert(0, 'Введите свой возраст')


entry_registration_age = Entry(width=41)
entry_registration_age.place(x=40, y=90)
entry_registration_age.insert(0, 'Введите свой возраст')
entry_registration_age.bind("<FocusIn>", entry_registration_age_focus)
entry_registration_age.bind("<FocusOut>", entry_registration_age_not_focus)


def create_window():
    def create_master():
        with sqlite3.connect('Tkinter_users.db') as con:
            cur = con.cursor()
            date = [ent_name_master_class.get(), ent_max_people.get(),
                    ent_min_age.get(), ent_max_age.get()]
            if date[0] and date[1] and date[2] and date[3] != "":
                cur.execute("""INSERT INTO lessons (
                name, max_count,
                min_age, max_age)
                VALUES (?,?,?,?)""", date)

                ent_name_master_class.delete(0, 'end')
                ent_max_people.delete(0, 'end')
                ent_min_age.delete(0, 'end')
                ent_max_age.delete(0, 'end')
                db.commit()
                showinfo(
                    title='Информация!',
                    message='Вы успешно зарегистрировались!'
                    )

    new_window = Tk()
    new_window.geometry('500x300')
    new_window.title('Регистрация нового мастер класса')
    new_window.resizable(False, False)

    def on_entry_focus_name(event):
        if ent_name_master_class.get() == 'Введите название мастер класса':
            ent_name_master_class.delete(0, "end")

    def on_entry_focus_max_people(event):
        if ent_max_people.get() == 'Введите макс. кол-во человек':
            ent_max_people.delete(0, "end")

    def on_entry_focus_min_age(event):
        if ent_min_age.get() == 'Введите минимальный возраст':
            ent_min_age.delete(0, "end")

    def on_entry_focus_max_age(event):
        if ent_max_age.get() == 'Введите максимальный возраст':
            ent_max_age.delete(0, "end")

    def on_entry_leave_master_class(event):
        if ent_name_master_class.get() == "":
            ent_name_master_class.insert(0, 'Введите название мастер класса')

    def on_entry_leave_max_people(event):
        if ent_max_people.get() == "":
            ent_max_people.insert(0, 'Введите макс. кол-во человек')

    def on_entry_leave_min_age(event):
        if ent_min_age.get() == "":
            ent_min_age.insert(0, 'Введите минимальный возраст')

    def on_entry_leave_max_age(event):
        if ent_max_age.get() == "":
            ent_max_age.insert(0, 'Введите максимальный возраст')

    ent_name_master_class = Entry(new_window, width=30)
    ent_name_master_class.place(x=150, y=30)
    ent_name_master_class.insert(0, 'Введите название мастер класса')

    ent_max_people = Entry(new_window, width=30)
    ent_max_people.place(x=150, y=55)
    ent_max_people.insert(0, 'Введите макс. кол-во человек')

    ent_min_age = Entry(new_window, width=30)
    ent_min_age.place(x=150, y=80)
    ent_min_age.insert(0, 'Введите минимальный возраст')

    ent_max_age = Entry(new_window, width=30)
    ent_max_age.place(x=150, y=110)
    ent_max_age.insert(0, 'Введите максимальный возраст')

    ent_name_master_class.bind("<FocusIn>", on_entry_focus_name)
    ent_name_master_class.bind("<FocusOut>", on_entry_leave_master_class)

    ent_max_people.bind("<FocusIn>", on_entry_focus_max_people)
    ent_max_people.bind("<FocusOut>", on_entry_leave_max_people)

    ent_min_age.bind("<FocusIn>", on_entry_focus_min_age)
    ent_min_age.bind("<FocusOut>", on_entry_leave_min_age)

    ent_max_age.bind("<FocusIn>", on_entry_focus_max_age)
    ent_max_age.bind("<FocusOut>", on_entry_leave_max_age)

    button_create = Button(new_window, text='Создать', command=create_master)
    button_create.place(x=200, y=140)


button_for_create = Button(text='Зарегистрировать новый мастер класс',
                                command=create_window).place(x=410, y=360)

for i in cur.execute("SELECT * FROM lessons"):
    print([*i])

root.mainloop()
