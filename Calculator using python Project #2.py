from tkinter import *

def add(a,b):
    return a + b

def sub(a,b):
    return a - b

def mul(a,b):
    return a * b

def div(a,b):
    return a / b

def mod(a,b):
    return a % b

def sqr(a, b):
    return a ** b

def lcm(a, b):
    l = a if a > b else b  # a = 2 and b = 3
    while l <= a * b:   # 2 * 3 = 6
        if l % a == 0 and l % b == 0: 
            return l
        l = l + 1
def hcd(a,b):
    h = a if a < b else b # a = 6 and b = 9
    while h >= 1: 
        if a % h == 0 and b % h == 0:
            return h
        h = h - 1
def extract_numbers(text):
    L = []
    for t in text.split(' '):
        try:
            float(t)
            L.append(float(t))
        except ValueError:
            pass
    return L

def calculate():
    text = textin.get()
    for word in text.split(' '):
        if word.upper() in operations.keys():
            try:
                splitted = extract_numbers(text)
                response = operations[word.upper()](splitted[0], splitted[1])
                list.delete(0, END)
                list.insert(END, response)
            except:
                list.delete(0, END)
                list.insert(END, "Something went wrong")
            finally:
                break
        else:
            list.delete(0, END)
            list.insert(END, "Please! Try Again!!!")

operations = {
    '+':add, 'ADD':add, 'ADDITION':add,'SUM':add,'SUMMATION':add, 'PLUS':add, 
    'SUBSTRACT':sub,'MINUS':sub,'-':sub,'DIFFERENCE':sub,'SUB':sub,
    'MULTIPLY':mul,'*':mul,'MULTIPLICATION':mul,'TIMES':mul,'PRODUCT':mul,
    'MOD':mod,'MODULUS':mod,'%':mod, 'LCM':lcm,'HCD':hcd,'DIV':div,'/':div,
    'DIVIDE':div,'DIVISION':div, 'square':sqr,'sqr':sqr,'**':sqr
}

root = Tk()
root.title("AI_Mirror_Calculator")
root.geometry("500x300")
root.resizable(False, False)
root.config(background="black")

L1 = Label(root, text="Simple and easy calculator", font="cambria 12 bold", width="30", padx="3")
L1.place(x=115, y=35)

L1 = Label(root, text="Suported Operators (+,-,*,/,%,**,Lcm,Hcd)", font="cambria 12 bold", width="33", padx="3")
L1.place(x=105, y=75)

L1 = Label(root, text="Eg. Multiply 20 and 100", font="cambria 12 bold", width="25", padx="3")
L1.place(x=136, y=130)

textin = StringVar()
Enter = Entry(root, width="30", textvariable=textin)
Enter.place(x=156, y=166)


Btn = Button(root, text="Get Result", font="cambria 12 bold", command= calculate)
Btn.place(x=210, y=200)

list = Listbox(root, width="35", height="2")
list.place(x=135, y=248)

root.mainloop()
