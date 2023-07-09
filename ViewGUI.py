import Schedualing as s
import tkinter as tk
from tkinter import StringVar
from tkinter import PhotoImage
from tkinter.constants import TOP, LEFT, CENTER

win = tk.Tk()
win.title("Schedualing")
height = 450
width = 450
# 視窗定正中間
xPos = int((win.winfo_screenwidth()-width)/2)
yPos = int((win.winfo_screenheight()-height)/2)
win.geometry(str(width)+"x"+str(height)+"+"+str(xPos)+"+"+str(yPos))
# 無法更改視窗大小
#win.resizable(0, 0)

win.config(bg="#323232")


taskLabel = tk.Label(win, text="Task: ", fg="#FFFFFF", bg="#323232")
taskLabel.config(font="Consolas 12")
taskLabel.pack()

taskFr = tk.Frame(win)
taskFr.pack()
taskStringShowed = StringVar()
taskStringShowed.set("")


def clear():
    global taskStringShowed
    taskStringShowed.set("")


clearBtn = tk.Button(taskFr, text="Clear", bg="#A3A3A3")
clearBtn.config(width=6, height=1, bd=2, command=clear)


taskEntry = tk.Entry(taskFr, font="Consolas 12", selectbackground="#FF8F2B")
taskEntry.config(width=40, textvariable=taskStringShowed)
taskEntry.pack(side=tk.LEFT)
clearBtn.pack(side=tk.LEFT)


def enter1():
    s = ""
    if len(taskEntry.get()) != 0:
        s += ","
    s += "1"
    taskEntry.insert(len(taskEntry.get()), s)


def enter2():
    s = ""
    if len(taskEntry.get()) != 0:
        s += ","
    s += "2"
    taskEntry.insert(len(taskEntry.get()), s)


def enter3():
    s = ""
    if len(taskEntry.get()) != 0:
        s += ","
    s += "3"
    taskEntry.insert(len(taskEntry.get()), s)


def enter4():
    s = ""
    if len(taskEntry.get()) != 0:
        s += ","
    s += "4"
    taskEntry.insert(len(taskEntry.get()), s)


def enter5():
    s = ""
    if len(taskEntry.get()) != 0:
        s += ","
    s += "5"
    taskEntry.insert(len(taskEntry.get()), s)


def enter6():
    s = ""
    if len(taskEntry.get()) != 0:
        s += ","
    s += "6"
    taskEntry.insert(len(taskEntry.get()), s)


def enter7():
    s = ""
    if len(taskEntry.get()) != 0:
        s += ","
    s += "7"
    taskEntry.insert(len(taskEntry.get()), s)


def enter8():
    s = ""
    if len(taskEntry.get()) != 0:
        s += ","
    s += "8"
    taskEntry.insert(len(taskEntry.get()), s)


def enter9():
    s = ""
    if len(taskEntry.get()) != 0:
        s += ","
    s += "9"
    taskEntry.insert(len(taskEntry.get()), s)


btnFr = tk.Frame(win)
btnFr.pack()
btn1 = tk.Button(btnFr, text="1", bg="#A3A3A3")
btn1.config(width=4, height=1, bd=2, command=enter1)
btn1.grid(row=0, column=0)
btn2 = tk.Button(btnFr, text="2", bg="#A3A3A3")
btn2.config(width=4, height=1, command=enter2)
btn2.grid(row=0, column=1)
btn3 = tk.Button(btnFr, text="3", bg="#A3A3A3")
btn3.config(width=4, height=1, bd=2, command=enter3)
btn3.grid(row=0, column=2)
btn4 = tk.Button(btnFr, text="4", bg="#A3A3A3")
btn4.config(width=4, height=1, bd=2, command=enter4)
btn4.grid(row=1, column=0)
btn5 = tk.Button(btnFr, text="5", bg="#A3A3A3")
btn5.config(width=4, height=1, bd=2, command=enter5)
btn5.grid(row=1, column=1)
btn6 = tk.Button(btnFr, text="6", bg="#A3A3A3")
btn6.config(width=4, height=1, bd=2, command=enter6)
btn6.grid(row=1, column=2)
btn7 = tk.Button(btnFr, text="7", bg="#A3A3A3")
btn7.config(width=4, height=1, bd=2, command=enter7)
btn7.grid(row=2, column=0)
btn8 = tk.Button(btnFr, text="8", bg="#A3A3A3")
btn8.config(width=4, height=1, bd=2, command=enter8)
btn8.grid(row=2, column=1)
btn9 = tk.Button(btnFr, text="9", bg="#A3A3A3")
btn9.config(width=4, height=1, bd=2, command=enter9)
btn9.grid(row=2, column=2)


machineLabel = tk.Label(
    win, text="Maximum Number of Machines: ", fg="#FFFFFF", bg="#323232")
machineLabel.config(font="Consolas 12")
machineLabel.pack()

machineFr = tk.Frame(win)
machineFr.pack()
machineStringShowed = StringVar()
machineStringShowed.set("")


def machineAdd():
    global machineStringShowed
    if machineStringShowed != "":
        machineStringShowed.set(str(int(machineStringShowed)+1))
    else:
        machineStringShowed.set("1")


addBtn = tk.Button(machineFr, text="<", bg="#A3A3A3")
addBtn.config(width=1, height=1, bd=2, command=machineAdd)
machineEntry = tk.Entry(machineFr, font="Consolas 12",
                        selectbackground="#FF8F2B")
machineEntry.config(width=5, justify=tk.CENTER, bd=2,
                    textvariable=machineStringShowed)
machineEntry.pack(side=tk.LEFT)
addBtn.pack(side=tk.LEFT)


timeLabel = tk.Label(win, text="Time Limit: ", fg="#FFFFFF", bg="#323232")
timeLabel.config(font="Consolas 12")
timeLabel.pack()

timeEntry = tk.Entry(win, font="Consolas 12", selectbackground="#FF8F2B")
timeEntry.config(width=5, justify=tk.CENTER, bd=2)
timeEntry.pack()

text = StringVar()
text.set("")

controlFr = tk.Frame(win)
controlFr.pack()


def start():
    global text
    try:
        schedualing = s.SchedualSystem()
        schedualing.assignTasks(taskEntry.get())
        schedualing.setMachineNumberLimit(int(machineEntry.get()))
        schedualing.setTimeLimit(int(timeEntry.get()))
        schedualing.minMachineRequired()
        text.set(schedualing.resultMessage())
    except Exception:
        text.set("Invalid Operation!")


starBtn = tk.Button(controlFr, text="Start", bg="#A3A3A3")
starBtn.config(width=6, height=1, bd=2, command=start)
starBtn.pack(side=tk.LEFT)


def renew():
    global text
    text.set("")


renewBtn = tk.Button(controlFr, text="Renew", bg="#A3A3A3")
renewBtn.config(width=6, height=1, bd=2, command=renew)
renewBtn.pack(side=tk.RIGHT)

resultLabel = tk.Label(win, textvariable=text, fg="#FFFFFF", bg="#323232")
resultLabel.config(font="Consolas 12", justify=tk.LEFT)
resultLabel.pack()


win.mainloop()
