from tkinter import *
import tkinter

root = Tk()

root.title("CALCULATOR")
root.geometry('450x520')

operator = ''

root.resizable(0, 0)


def btnClick(number):
    global operator
    operator = operator + str(number)
    input_text.set(operator)


def btnClear(opr):
    global operator
    operator = ''
    input_text.set(operator)


def btnEquals(oper):
    global operator
    sump = str(eval(operator))
    input_text.set(sump)
    operator = ''


input_text = StringVar()

# black1 = Label(root, width='47', height='13')
# black1.place(x=10, y=11)

calculator = Label(root, text='CALCULATOR', fg='red', width='15', height='1', font=('times', 25, 'bold'))
calculator.place(x=70, y=10)

text = Entry(root, fg='red', width='28', font=('times', 22, 'bold'),
             justify='right', textvariable=input_text)
text.place(x=22, y=80)

# black2 = Label(root, width='47', height='18')
# black2.place(x=10, y=220)

# numlab = Label(root, bg='black', height='17', width='30')
# numlab.place(x=30, y=140)

# oppanel = Label(root, bg='black', height='17', width='8')
# oppanel.place(x=315, y=140)

# line first /
button0 = Button(root, text='0', fg='red', bg='black', width='4', height='1', font=('times', 25, 'bold'),
                 command=lambda: btnClick(0), activebackground='orange')
button0.place(x=132, y=330)

button1 = Button(root, text='1', width='4', fg='red', bg='black', height='1', font=('times', 25, 'bold'),
                 command=lambda: btnClick(1), activebackground='orange')
button1.place(x=225, y=260)

button2 = Button(root, text='2', fg='red', bg='black', width='4', height='1', font=('times', 25, 'bold'),
                 command=lambda: btnClick(2),activebackground = 'orange')
button2.place(x=132, y=260)
button3 = Button(root, text='3', width='4', fg='red', bg='black', height='1', font=('times', 25, 'bold'),
                 command=lambda: btnClick(3), activebackground='orange')
button3.place(x=38, y=260)

button4 = Button(root, text='4', width='4', fg='red', bg='black', height='1', font=('times', 25, 'bold'),
                 command=lambda: btnClick(4), activebackground='orange')
button4.place(x=225, y=210)
button5 = Button(root, text='5', fg='red', bg='black', width='4', height='1', font=('times', 25, 'bold'),
                 command=lambda: btnClick(5), activebackground='orange')
button5.place(x=132, y=210)

button6 = Button(root, text='6', fg='red', bg='black', width='4', height='1', font=('times', 25, 'bold'),
                 command=lambda: btnClick(6), activebackground='orange')
button6.place(x=38, y=210)

button7 = Button(root, text='7', width='4', fg='red', bg='black', height='1', font=('times', 25, 'bold'),
                 command=lambda: btnClick(7), activebackground='orange')
button7.place(x=38, y=160)

button8 = Button(root, text='8', width='4', fg='red', bg='black', height='1', font=('times', 25, 'bold'),
                 command=lambda: btnClick(8), activebackground='orange')
button8.place(x=132, y=160)

button9 = Button(root, text='9', width='4', fg='red', bg='black', height='1', font=('times', 25, 'bold'),
                 command=lambda: btnClick(9), activebackground='orange')
button9.place(x=225, y=160)

buttonDV = Button(root, text='/', width='4', fg='red', bg='black', height='1', font=('times', 25, 'bold'),
                  command=lambda: btnClick('/'), activebackground='orange')
buttonDV.place(x=320, y=160)

buttonMP = Button(root, text='*', fg='red', bg='black', width='4', height='1', font=('times', 25, 'bold'),
                  command=lambda: btnClick('*'), activebackground='orange')
buttonMP.place(x=320, y=210)

buttonPlus = Button(root, text='+', width='4', fg='red', bg='black', height='1', font=('times', 25, 'bold'),
                    command=lambda: btnClick('+'), activebackground='orange')
buttonPlus.place(x=320, y=260)

buttonc = Button(root, text='C', width='4', fg='red', bg='black', height='1', font=('times', 25, 'bold'),
                 command=lambda: btnClear('c'))
buttonc.place(x=38, y=330)

buttonEqu = Button(root, text='=', fg='red', bg='black', width='4', height='1', font=('times', 25, 'bold'),
                   command=lambda: btnEquals('='), activebackground='orange')
buttonEqu.place(x=225, y=330)

buttonMinus = Button(root, text='-', fg='red', bg='black', width='4', height='1', font=('times', 25, 'bold'),
                     command=lambda: btnClick('-'), activebackground='orange')
buttonMinus.place(x=320, y=330)

root.mainloop()
