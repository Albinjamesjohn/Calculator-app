#calculator program Albin

from tkinter import*
import math
import sys
import os

def resource_path(relative_path):
    try:
        # When bundled with PyInstaller, it stores data in a temporary folder accessible via sys._MEIPASS
        base_path=sys._MEIPASS
    except Exception:
        # If running normally using pycharm (not bundled), use current folder
        base_path=os.path.abspath(".")
    return os.path.join(base_path,relative_path)


def button_press(num):
    global equation_text
    equation_text=equation_text + str(num)
    equation_label.set(equation_text)


def equals():
    global equation_text
    try:
        total=str(eval(equation_text))    #eval will parse the expression or calculate the expression
        equation_label.set(total)
        equation_text=total
    except SyntaxError:     #typing only symbols error correction if we press =,the text remains same
        equation_text=""
    except ZeroDivisionError:    #zero division error alert
        equation_label.set("Not defined")

def equals_key(event):
    global equation_text
    try:
        total = str(eval(equation_text))  # eval will evaluate the expression
        equation_label.set(total)
        equation_text = total
    except SyntaxError:  # typing only symbols error correction if we press =,the text remains same
        equation_text = ""
    except ZeroDivisionError:  # zero division error alert
        equation_label.set("Not defined")



def clear():
    global equation_text
    equation_label.set("")
    equation_text=""

def backspace():
    global equation_text
    equation_text=equation_text[:-1]  #removes the last charactor
    equation_label.set(equation_text)

def Percent():
    global equation_text
    try:
        percentage=float(equation_text)/100
        equation_label.set(str(percentage))
        equation_text=str(percentage)
    except ValueError:
        equation_text=equation_text


def sqrt_fun():
    global equation_text
    try:
        roots = math.sqrt(float(equation_text))
        equation_label.set(str(roots))
        equation_text = str(roots)
    except ValueError:
        equation_text = equation_text


window=Tk()
window.title("ALBIN'S CALCULATOR")
icon_path=r"C:\Users\Albin\OneDrive\Documents\VS Code Python\CALCULATOR APP\static\equal.png"   # copy the icon image path here
icon_img=PhotoImage(file=icon_path)
window.iconphoto(False,icon_img)
window.geometry("470x638+100+100")  # +100+100 are the coordinates of fixed position on opening the window
window.resizable(False, False)


equation_text=""
equation_label=StringVar()
label=Label(window,textvariable=equation_label,font=("times new roman",20),bg="black",fg="white",width=31,height=2)
label.pack()

frame=Frame(window)
frame.config(bg="#121212")
frame.pack()
button1=Button(frame,text=1,height=4,width=9,font=35,
               bg="#808080",fg="yellow",command=lambda: button_press(1))
button1.grid(row=0,column=0)

window.bind('1',lambda event:button_press(1))

button2=Button(frame,text=2,height=4,width=9,font=35, bg="#808080",fg="yellow",
               command=lambda: button_press(2))
button2.grid(row=0,column=1)
window.bind('2',lambda event:button_press(2))


button3=Button(frame,text=3,height=4,width=9,font=35, bg="#808080",fg="yellow",
               command=lambda: button_press(3))
button3.grid(row=0,column=2)
window.bind('3',lambda event:button_press(3))

button4=Button(frame,text=4,height=4,width=9,font=35, bg="#808080",fg="yellow",
               command=lambda: button_press(4))
button4.grid(row=1,column=0)
window.bind('4',lambda event:button_press(4))

button5=Button(frame,text=5,height=4,width=9,font=35, bg="#808080",fg="yellow",
               command=lambda: button_press(5))
button5.grid(row=1,column=1)
window.bind('5',lambda event:button_press(5))


button6=Button(frame,text=6,height=4,width=9,font=35, bg="#808080",fg="yellow",command=lambda: button_press(6))
button6.grid(row=1,column=2)
window.bind('6',lambda event:button_press(6))

button7=Button(frame,text=7,height=4,width=9,font=35,bg="#808080",fg="yellow",
               command=lambda: button_press(7))
button7.grid(row=2,column=0)
window.bind('7',lambda event:button_press(7))

button8=Button(frame,text=8,height=4,width=9,font=35,bg="#808080",fg="yellow",
               command=lambda: button_press(8))
button8.grid(row=2,column=1)
window.bind('8',lambda event:button_press(8))

button9=Button(frame,text=9,height=4,width=9,font=35,bg="#808080",fg="yellow",
               command=lambda: button_press(9))
button9.grid(row=2,column=2)
window.bind('9',lambda event:button_press(9))

button0=Button(frame,text=0,height=4,width=9,font=35,bg="#808080",fg="yellow",
               command=lambda: button_press(0))
button0.grid(row=3,column=0)
window.bind('0',lambda event:button_press(0))

plus=Button(frame,text="+",height=4,width=9,font=35,bg="#808080",fg="black",
               command=lambda: button_press('+'))
plus.grid(row=0,column=3)
window.bind('+',lambda event:button_press('+'))

minus=Button(frame,text="-",height=4,width=9,font=35,bg="#808080",fg="black",
               command=lambda: button_press('-'))
minus.grid(row=1,column=3)
window.bind('-',lambda event:button_press('-'))


mult=Button(frame,text="*",height=4,width=9,font=35,bg="#808080",fg="black",
               command=lambda: button_press('*'))
mult.grid(row=2,column=3)
window.bind('*',lambda event:button_press('*'))


div=Button(frame,text="/",height=4,width=9,font=35,bg="#808080",fg="black",
               command=lambda: button_press('/'))
div.grid(row=3,column=3)
window.bind('/',lambda event:button_press('/'))


#equal sign button
equal=Button(frame,text="=",height=4,width=9,font=35,bg="#808080",fg="black",
               command=equals)
equal.grid(row=3,column=2)
window.bind('<=>',equals_key)
window.bind('<Return>',equals_key)

#decimal point button
decimal=Button(frame,text=".",height=4,width=9,font=35,bg="#808080",fg="black",
               command=lambda: button_press('.'))
decimal.grid(row=3,column=1)
window.bind('.',lambda event:button_press('.'))

#clear all button
clear=Button(frame,text="Clear",height=4,width=9,font=35,bg="#808080",fg="black",
               command=clear)
clear.grid(row=4,column=2)

#backspace
back=Button(frame,text="\u2190",height=4,width=9,font=35,bg="#808080",fg="black",
               command=backspace)
back.grid(row=4,column=3)
window.bind('<BackSpace>',lambda event:backspace())

#pecentage button
percent=Button(frame,text="%",height=4,width=9,font=35,bg="#808080",fg="black",
               command=Percent)
percent.grid(row=4,column=1)
window.bind('<%>',lambda event:Percent())

#squareroot calculation button
root=Button(frame,text="\u221A",height=4,width=9,font=35,bg="#808080",fg="black",
               command=sqrt_fun)
root.grid(row=4,column=0)


window.mainloop()