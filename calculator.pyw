from tkinter import *

'''
Author -  Swastik
Date Created - 13/05/2021
'''
def press(num):
    # print(num)
    global expression
    expression+=str(num)
    input_text.set(expression)
    # print(type(input_text.get()))
def equal():
    input_text.set(eval(input_text.get()))
def clear():
    input_text.set('')
    global expression
    expression=''
def delete():
    global input_text
    input_text.set(input_text.get()[0:len(input_text.get()) -1])


if __name__ == '__main__':    
    root=Tk()
    root.geometry('225x310')
    root.resizable(0, 0)  # this is to prevent from resizing the window
    root.wm_iconbitmap('calculator.ico')
    root.title('Calculator')
    input_text=StringVar()
    input_text.set('')
    expression = ''
    screen = Entry(root, textvariable=input_text,state=DISABLED, font=('Courier New', 16))
    screen.pack(padx=10, pady=10, ipadx=5, ipady=5)
    buttons=Frame()
    buttons.pack()
    number1 = Button(buttons, text='1', command=lambda: press(1), font=('Courier New', 16), relief=GROOVE)
    number1.grid(row=0, column=0, ipadx=5, padx=5, pady=5)
    number2 = Button(buttons, text='2', command=lambda: press(2), font=('Courier New', 16), relief=GROOVE)
    number2.grid(row=0, column=1, ipadx=5, padx=5, pady=5)
    number3 = Button(buttons, text='3', command=lambda: press(3), font=('Courier New', 16), relief=GROOVE)
    number3.grid(row=0, column=2, ipadx=5, padx=5, pady=5)
    number4 = Button(buttons, text='4', command=lambda: press(4), font=('Courier New', 16), relief=GROOVE)
    number4.grid(row=1, column=0, ipadx=5, padx=5, pady=5)
    number5 = Button(buttons, text='5', command=lambda: press(5), font=('Courier New', 16), relief=GROOVE)
    number5.grid(row=1, column=1, ipadx=5, padx=5, pady=5)
    number6 = Button(buttons, text='6', command=lambda: press(6), font=('Courier New', 16), relief=GROOVE)
    number6.grid(row=1, column=2, ipadx=5, padx=5, pady=5)
    number7 = Button(buttons, text='7', command=lambda: press(7), font=('Courier New', 16), relief=GROOVE)
    number7.grid(row=2, column=0, ipadx=5, padx=5, pady=5)
    number8 = Button(buttons, text='8', command=lambda: press(8), font=('Courier New', 16), relief=GROOVE)
    number8.grid(row=2, column=1, ipadx=5, padx=5, pady=5)
    number9 = Button(buttons, text='9', command=lambda: press(9), font=('Courier New', 16), relief=GROOVE)
    number9.grid(row=2, column=2, ipadx=5, padx=5, pady=5)
    number0 = Button(buttons, text='0', command=lambda: press(0), font=('Courier New', 16), relief=GROOVE)
    number0.grid(row=3, column=1, ipadx=5, padx=5, pady=5)
    point = Button(buttons, text='.', command=lambda: press('.'), font=('Courier New', 16), relief=GROOVE)
    point.grid(row=3, column=0, ipadx=5, padx=5, pady=5)
    equal = Button(buttons, text='=', command=equal, font=('Courier New', 16), relief=GROOVE)
    equal.grid(row=3, column=2, ipadx=5, padx=5, pady=5)
    clear= Button(buttons, text='C', command=clear, font=('Courier New', 16), relief=GROOVE)
    clear.grid(row=4, column=0, ipadx=5, padx=5, pady=5)
    delete =  Button(buttons, text='⌫', command=delete, font=('Courier New', 12), relief=GROOVE)
    delete.grid(row=4, column=1, ipadx=5,ipady=5, padx=5, pady=5)
    plus = Button(buttons, text='+', command=lambda: press('+'), font=('Courier New', 16), relief=GROOVE)
    plus.grid(row=0, column=3, ipadx=5, padx=5, pady=5)
    minus = Button(buttons, text='-', command=lambda: press('-'), font=('Courier New', 16), relief=GROOVE)
    minus.grid(row=1, column=3, ipadx=5, padx=5, pady=5)
    multiply = Button(buttons, text='*', command=lambda: press('*'), font=('Courier New', 16), relief=GROOVE)
    multiply.grid(row=2, column=3, ipadx=5, padx=5, pady=5)
    divide = Button(buttons, text='/', command=lambda: press('/'), font=('Courier New', 16), relief=GROOVE)
    divide.grid(row=3, column=3, ipadx=5, padx=5, pady=5)
    root.mainloop()
