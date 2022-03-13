from tkinter import *
from tkinter.ttk import *
from time import strftime

clock = Tk()
clock.title("DIGITAL CLOCK")

def time():
    charac= strftime("%H:%M:%S:%p")
    label.config(text = charac)
    label.after(1000, time)

label = Label(clock, font=("AR DARLING",160), background='black', foreground='white')
label.pack(anchor="center", fill="both", expand="yes")

time()
clock.mainloop()