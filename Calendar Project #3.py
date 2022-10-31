# Programmer - ARTIFICIAL INTELLIGENCE (C.E.O Ezechiel KIREGHA)

# PYTHON GUI TO DISPLAY CURRENT YEAR'S CALENDAR AND USER-INPUT YEAR'S CALENDAR USING THE calendar PACKAGE

'''
The calendar module allows output calendars like the program and provides addition useful functions
related to the calendar. Functions and classes defined in the calendar module use an idealized calendar.
The current Gregorian calendar extend indefinitely in both directions. By default, these calendars have Monday as the first day of the week, and Sunday as the last (the European convetion).
'''

# The calendar package is an inbuilt in Python

# Importing necessary packages
import calendar
import tkinter as tk
from datetime import date
from tkinter import *
from logging import root

# Defining CreateWidgets() function to create necessary tkinter widgets
def widget():
    root.calllabel = Label(root, bg="white",fg="black", font=("cambria", 20), width=30)
    root.calllabel.grid(row=1, column=1, padx= 10, pady= 10, columnspan= 2)

    root.calendarText = Text(root, bg="white", borderwidth=2, relief="raised", width=75, height=35)
    root.calendarText.grid(row=2, column=1, padx=10, columnspan=2)

    root.calendarEntry = Entry(root, width=35, textvariable= year, justify="center")
    root.calendarEntry.grid(row=3, column= 1, padx= 40, pady= 10)

    root.getcalendarBtn = Button(root, text="DISPLAY CALENDAR", width=20, command=getCalendar)
    root.getcalendarBtn.grid(row=3, column= 2, padx= 10, pady= 1)

    onStartUp()

# Defining onStartUp() to display current year's calendar when the application starts
def onStartUp():
    # Fetching the current day, mounth, and year using day,month, year property of today() method of date class of datetime
    current_month = date.today().month
    current_day = date.today().day
    current_year = date.today().year
    # Fetching the calendar of the user-input year and sorting it in calendar_text variable
    calendar_Text = calendar.calendar(current_year)
    # Configuring label to display the year of the calendar
    root.calllabel.config(text=str(current_month)+"-"+str(current_day)+"-"+str(current_year)+"| CALENDAR")
    # Displaying the calendar in the calendar Text Widget using the insert() method
    root.calendarText.insert(0.0, calendar_Text)

# Defining getCalendar() to fetch user-input year and display the calendar of user-input year
def getCalendar():
    # Retrieving the user-input year and sorting it in calendar_text as integer
    current_year = int(year.get())
    # Fetching the calendar of the user-input and sorting it in the calendar variable
    calendar_Text = calendar.calendar(current_year)
    # Configuring label to display the year of the calendar
    root.calllabel.config(text="YEAR "+str(current_year)+"| CALENDAR")
    # Displaying the calendar in the calendar Text Widget using the insert() method
    root.calendarText.insert(0.0, calendar_Text)

# Creating the object of the tk class
root = tk.Tk()
# setting the title, window size, background color and disabling th resizing property
root.title("AI_Mirror_Calendar")
# Creating tkinter variables
root.geometry("625x660")
root.resizable(False,False)
root.config(bg="black")
# Creating tkinter variables
year = StringVar()
#calling the CreateWidgets() function
widget()
# Defining infinite loop to run application
root.mainloop()