# TODO:
# we got alot to do global and thingy

from tkinter import *
import tkinter.font as tkFont
from matplotlib import pyplot as plt
import pandas as pd
import time as t
import array
import math


class gui():
    def __init__(self):
        global gravity
        global time
        global sensitivity

        sensitivity = 200
        gravity = array.array('f')
        time = array.array('f')

        self.prefill()  # use this if this is a test run

        self.root = Tk()
        self.root.geometry("800x440")
        self.root.title('Arz Cazibesi')

        #tkFont.Font(family="Lucida Grande", size=20)

        self.label = Label(self.root, text="Arz Cazibesi")
        self.labelcurrentPressure = Label(self.root, text="Current Pressure is:0.00 atm|0 Hgcm")
        self.labelcurrentPressurePersentage = Label(self.root, text="Current Pressure Percentage is: 0%")
        self.labelexp = Label(self.root, text="    |Current Experiment Values|")
        self.labelgravity = Label(self.root, text="Gravity: 0.00")
        self.labeltime = Label(self.root, text="Time: 0.00")
        self.labelpressure = Label(self.root, text="Pressure: 0.00")

        self.button0 = Button(self.root, text="     Start Experiment      ", command=self.startexp)
        self.button1 = Button(self.root, text="  Position - Time Graphic  ", command=self.ptG)
        self.button2 = Button(self.root, text="   Speed - Time Graphic    ", command=self.stG)
        self.button3 = Button(self.root, text="Acceleration - Time Graphic", command=self.atG)
        self.button4 = Button(self.root, text="      Print on Console     ", command=self.printVal)
        self.button5 = Button(self.root, text=" Adjust Pressure ", command=self.adjustPressure)
        self.button6 = Button(self.root, text="         Save Data         ", command=self.writeFile)

        self.pressureSlider = Scale(self.root, from_=0, to=760, length=180, tickinterval=190, orient=HORIZONTAL)
        self.pressureSlider.set(0)  # change this if necessary

        self.button0.config(font=("Courier 14"))
        self.button1.config(font=("Courier 14"))
        self.button2.config(font=("Courier 14"))
        self.button3.config(font=("Courier 14"))
        self.button4.config(font=("Courier 14"))
        self.button5.config(font=("Courier 14"))
        self.button6.config(font=("Courier 14"))
        self.labelcurrentPressure.config(font=("Courier 14"))
        self.labelcurrentPressurePersentage.config(font=("Courier 14"))
        self.labelexp.config(font=("Courier 14 italic bold"))
        self.labelgravity.config(font=("Courier 14"))
        self.labeltime.config(font=("Courier 14"))
        self.labelpressure.config(font=("Courier 14"))
        self.label.config(font=("Courier 30 bold"))

        self.label.place(x=250, y=20)
        self.labelcurrentPressure.place(x=365, y=105)
        self.labelcurrentPressurePersentage.place(x=365, y=145)
        self.labelexp.place(x=365, y=250)
        self.labelgravity.place(x=365, y=295)
        self.labeltime.place(x=365, y=335)
        self.labelpressure.place(x=365, y=375)
        self.button0.place(x=20, y=95)
        self.button1.place(x=20, y=150)
        self.button2.place(x=20, y=205)
        self.button3.place(x=20, y=260)
        self.button4.place(x=20, y=370)
        self.button5.place(x=375, y=190)
        self.button6.place(x=20, y=315)
        self.pressureSlider.place(x=585, y=180)

        self.root.mainloop()

    # main code goes in here
    def startexp(self):
        return

    def adjustPressure(self):
        currentPressure = self.pressureSlider.get()
        currentPressureAtm = currentPressure / 760
        persentage = currentPressure * 100 / 760
        self.labelcurrentPressure.config(
            text="Current Pressure is:{0:0.2f} atm|{1:d} Hgcm".format(currentPressureAtm, currentPressure))
        self.labelcurrentPressurePersentage.config(text="Current Pressure Percentage is: {0:0.2f}%".format(persentage))

    # position-time graphic
    def ptG(self):
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
    def stG(self):
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
    def atG(self):
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

    # writes datas on txt file
    def writeFile(self, expnum=4):
        file = open("gravity.txt", "a")
        for i in range(50):
            file.write('-')
        file.write("\nExperiment Number{0:4s}Gravity{0:4s}Pressure{0:4s}Time\n".format(' '))
        for i in range(expnum):
            file.write('{4:4s}Exp {0:d}:{1:18.6f}{2:10.2f}{3:10.4f}\n'.format(i, gravity[i], pressure[i], time[i], ' '))

    # prints values in console
    def printVal(self):
        exnum = ['Exp 1:', 'Exp 2:', 'Exp 3:', 'Exp 4:']
        g = pd.Series(gravity)
        t = pd.Series(time)
        Data = {'Experiment Number': exnum, 'Gravity': g, 'Pressure': pressure, 'Time': t}
        df = pd.DataFrame(Data)
        print(df)

    # fills values manualy
    def prefill(self):
        global time
        global gravity
        global exnum
        global pressure

        height = 2.0  # meters
        time = [0.61, 0.622, 0.6423, 0.6323]
        pressure = [1, 0.9, 0.81, 0.3]
        exnum = ['Exp 1:', 'Exp 2:', 'Exp 3:', 'Exp 4:']
        for i in range(0, 4):
            gravity.insert(i, 2 * height / time[i] ** 2)


if __name__ == '__main__':
    screen = gui()
