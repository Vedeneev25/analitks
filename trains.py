import psycopg2
import matplotlib.pyplot as plt
import pandas as pd
import queries as que
import tkinter as tk
from tkinter import *
from tkinter import ttk
import drawww as dr

conn = psycopg2.connect(dbname='Rent', user='postgres', 
                        password='1234', host='localhost', port = "5432")
cursor = conn.cursor()

arguments = ["city", "deal", "tenant", "shop", "zone", "category", "bis"]
nums = ["lf1", "lf2", "sales", "revenue"]
cities = que.cities()
heads_rent = ["city", "date", "deal", "lf1", "sales", "lf2", "recipts", "revenue", "pax_id"]
heads_deal = ["deal", "cat_id", "square","start_date", "stop_date","zone", "tenant_id", "shop_id", "bis_id" ]


def send0(event):
    if argumentEntry.get() == "deal":
        send()
    elif argumentEntry.get() =="city":
        print("ddd")
    window.destroy()
    

def send():
    lima=argumentEntry.get()
    date_year = yearEntry.get()
    start_date_mon = startMonEntry.get() 
    finish_date_mon = stopMonEntry.get()
    cursor.execute( que.query1(lima, date_year, start_date_mon, finish_date_mon))
    record = cursor.fetchmany(size=5)
    cursor.close()
    conn.close()
    dr.draw(record)
    return record

def rounq():
    lima=argumentEntry.get()
    pokaz = WhatEntry.get()
    #filters
    date_year = yearEntry.get()
    start_date_mon = startMonEntry.get() 
    finish_date_mon = stopMonEntry.get()







window = tk.Tk()

params = tk.Frame(relief=tk.RAISED, master = window)
params.pack()

what = tk.Label(text="Что считаем? ", master=params,width=15)
WhatEntry = ttk.Combobox(values= nums, master = params, width=50)
what.grid(row=0,column=0, sticky="e")
WhatEntry.grid(row=0, column=1)

city = tk.Label(text="Выбери город", master = params, width=15)
cityEntry = ttk.Combobox(master=params, values = cities, width=50)
city.grid(row=1,column=0,sticky="e")
cityEntry.grid(row=1, column=1)

argument = tk.Label(master=params, text = "Агрегация", width = 15)
argumentEntry = ttk.Combobox(values=arguments, master = params, width=50)
argument.grid(row=2, column = 0)
argumentEntry.grid(row=2, column=1)

year = tk.Label(master = params, text="Укажите отчетный год", width=15)
yearEntry = tk.Entry(master = params, width = 50)
year.grid(row=3, column=0)
yearEntry.grid(row=3, column=1)

startMon = tk.Label(master = params, text = "Начальный месяц", width = 15)
startMonEntry = tk.Entry(master = params, width=50)
startMon.grid(row=4, column=0)
startMonEntry.grid(row=4,column=1)

stopMon = tk.Label(master = params, text = "Последний месяц", width = 15)
stopMonEntry = tk.Entry(master = params, width=50)
stopMon.grid(row=5, column=0)
stopMonEntry.grid(row=5,column=1)








buttonFrame = tk.Frame(relief=tk.SUNKEN, master=window)
buttonFrame.pack()

btn_submit = tk.Button(master=buttonFrame, text="Отправить")
btn_submit.grid(row=0,column=0)

bt_clear = tk.Button(master = buttonFrame, text = "Стереть ")
bt_clear.grid(row=0,column=1)

btn_submit.bind("<Button-1>", send0)




window.mainloop()

