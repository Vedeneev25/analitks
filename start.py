import tkinter as tk
from tkinter import *
import buttons as btns
from tkinter.ttk import *
from PIL import ImageTk, Image
import pie as pie

def goto(event):
    start.destroy()
    pie.new_func()

start = tk.Tk()

buttonsFrame = tk.Frame(master = start, relief=tk.SUNKEN)
buttonsFrame.pack()
btn1 = ImageTk.PhotoImage(Image.open("/Users/a1234/Desktop/SuperAnalitik/images/budka1.jpeg"))
btn2 = ImageTk.PhotoImage(Image.open("/Users/a1234/Desktop/SuperAnalitik/images/budka2.jpeg"))



btn_pie = tk.Button(master=buttonsFrame, image=btn1, padx=10, pady = 10)
btn_pie.grid(row=0,column=0)

bt_plot = tk.Button(master=buttonsFrame, image=btn2, padx=10, pady = 10)
bt_plot.grid(row=0,column=1)

btn_pie.bind("<Button-1>", goto)
start.mainloop()

