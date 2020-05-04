"""
TODO:
make choosable graphics NOT gravity[0], time[0]
"""

import matplotlib.pyplot as plt
import pandas as pd
import array, math
from tkinter import *

sensitivity = 200
height = 2.0  # meters
time = [0.61, 0.622, 0.6423, 0.6323]
pressure = [1, 0.9, 0.81, 0.3]
exnum = ['Exp 1:', 'Exp 2:', 'Exp 3:', 'Exp 4:']
gravity = array.array('f')

for i in range(0, 4):
    gravity.insert(i, 2 * height / time[i] ** 2)


# position-time graphic
def ptG():
    currentHeight = array.array('f')
    currentTime = array.array('f')
    for i in range(0, int(time[0] * sensitivity)):  # this is not correct
        currentTime.insert(i, math.sqrt(i * time[0] / sensitivity))
        currentHeight.insert(i, (0.5 * gravity[0] * currentTime[i] ** 2))
        print(currentHeight[i])
    plt.figure('Arz Cazibesi')
    plt.plot(currentTime, currentHeight)
    plt.ylabel('Position')
    plt.xlabel('Time')
    plt.title('Position-Time Graphic')
    plt.show()


# speed-time graphic
def stG():
    currentTime = array.array('f')
    currentSpeed = array.array('f')
    for i in range(0, int(time[0] * sensitivity)):
        currentTime.insert(i, math.sqrt(i * time[0] / sensitivity))
        currentSpeed.insert(i, gravity[0] * currentTime[i])
        print(currentSpeed[i])
    plt.figure('Arz Cazibesi')
    plt.plot(currentTime, currentSpeed)
    plt.ylabel('Speed')
    plt.xlabel('Time')
    plt.title('Speed-Time Graphic')
    plt.show()


# acceleration-time graphic
def atG():
    currentTime = array.array('f')
    currentGravity = array.array('f')
    for i in range(0, int(time[0] * sensitivity)):
        currentTime.insert(i, math.sqrt(i * time[0] / sensitivity))
        currentGravity.insert(i, gravity[0])
    plt.figure('Arz Cazibesi')
    plt.plot(currentTime, currentGravity)
    plt.ylabel('Acceleration')
    plt.xlabel('Time')
    plt.title('Acceleration-Time Graphic')
    plt.show()

def writeFile(expnum):
    file = open("gravity.txt", "a")
    for i in range(50):
        file.write('-')
    file.write("\nExperiment Number{0:4s}Gravity{0:4s}Pressure{0:4s}Time\n".format(' '))
    for i in range(expnum):
        file.write('{4:4s}Exp {0:d}:{1:18.6f}{2:10.2f}{3:10.4f}\n'.format(i, gravity[i], pressure[i], time[i], ' '))


def printVal():
    g = pd.Series(gravity)
    t = pd.Series(time)
    Data = {'Experiment Number': exnum, 'Gravity': g, 'Pressure': pressure, 'Time': t}
    df = pd.DataFrame(Data)
    print(df)
    writeFile(4)


root = Tk()
root.geometry("400x200")
root.title('Arz Cazibesi')

label= Label(root, text="Arz Cazibesi")

button1 = Button(root, text = "Position - Time", command = ptG)
button2 = Button(root, text = "Speed - Time", command = stG)
button3 = Button(root, text = "Acceleration - Time", command = atG)
button4 = Button(root, text = "Print on Console", command = printVal)

button1.config(font=("Courier 10 bold"))
button2.config(font=("Courier 10 bold"))
button3.config(font=("Courier 10 bold"))
button4.config(font=("Courier 10 bold"))
label.config(font=("Courier 22 bold"))

label.place(x=80, y=30)
button1.place(x=20,y=95)
button2.place(x=220,y=95)
button3.place(x=20,y=150)
button4.place(x=220,y=150)

root.mainloop()
