import tkinter as tk
from tkinter import *
from tkinter import ttk
import queries as que
import drawww as dr
import buttons as bt

def send0(event):
    if argumentEntry.get() == "deal":
        print("Оьработано")
    elif argumentEntry.get() =="city":
        print("ddd")
        send()
    
def send():
    dr.pie(que.pie(lima= argumentEntry.get(),
                        pokaz=WhatEntry.get(), 
                       date_year=yearEntry.get(),
                       start_date_mon=startMonEntry.get(),
                       finish_date_mon=stopMonEntry.get()))
    



def new_func():
    arguments = ["city", "deal", "tenant", "shop", "zone", "category", "bis"]
    nums = ["lf1", "lf2", "sales", "revenue"]
    cities = que.cities()
    global argumentEntry
    global WhatEntry
    global yearEntry
    global startMonEntry
    global stopMonEntry

    window = tk.Tk()

    params = tk.Frame(relief=tk.RAISED, master = window)
    params.pack()

    what = tk.Label(text="Что считаем? ", master=params,width=15)
    WhatEntry = ttk.Combobox(values= nums, master = params, width=50)
    what.grid(row=0,column=0, sticky="e")
    WhatEntry.grid(row=0, column=1)

    argument = tk.Label(master=params, text = "Агрегация", width = 15)
    argumentEntry = ttk.Combobox(values=arguments, master = params, width=50)
    argument.grid(row=1, column = 0)
    argumentEntry.grid(row=1, column=1)

    year = tk.Label(master = params, text="Укажите отчетный год", width=15)
    yearEntry = tk.Entry(master = params, width = 50)
    year.grid(row=2, column=0)
    yearEntry.grid(row=2, column=1)

    startMon = tk.Label(master = params, text = "Начальный месяц", width = 15)
    startMonEntry = tk.Entry(master = params, width=50)
    startMon.grid(row=3, column=0)
    startMonEntry.grid(row=3,column=1)

    stopMon = tk.Label(master = params, text = "Последний месяц", width = 15)
    stopMonEntry = tk.Entry(master = params, width=50)
    stopMon.grid(row=4, column=0)
    stopMonEntry.grid(row=4,column=1)
#Кнопки

    buttonFrame = tk.Frame(relief=tk.SUNKEN, master=window)
    buttonFrame.pack()

    btn_submit = tk.Button(master=buttonFrame, text="Отправить")
    btn_submit.grid(row=0,column=0)
    
    bt_clear = tk.Button(master = buttonFrame, text = "Стереть ")
    bt_clear.grid(row=0,column=1)

    btn_submit.bind("<Button-1>", send0)
    window.mainloop()

