#Arz Cazibesi
#Semih Akkoc

# TODO:
# we got alot to do global and thingy

from tkinter import *
from matplotlib import pyplot as plt
from gpiozero import LED as relay
from gpiozero import MotionSensor
import pandas as pd
import time as t
import array
import math
import smbus2
import bme280

infra = MotionSensor(27) #use queue_len if it detects twitchy
vaccum = relay(17)
magnet = relay(18)

#turn off vaccum turn on magnet
vaccum.on()
magnet.off()

port = 1
address = 0x76
bus = smbus2.SMBus(port)

cp = bme280.load_calibration_params(bus, address) #calibration_params
pressureData = bme280.sample(bus, address, cp)

print(pressureData)
print(pressureData.temperature)

curExNum=0 #current experiment number

class gui():
    def __init__(self):
        self.height = 2.0
        self.sensitivity = 200
        self.gravity = array.array('f')
        self.time = array.array('f')
        self.pressure = array.array('f')
        self.exnum = ['0']
        self.exnum.remove('0')

        #self.prefill()  # use this if this is a test run

        self.root = Tk()
        self.root.geometry("800x440")
        self.root.title('Arz Cazibesi')

        # tkFont.Font(family="Lucida Grande", size=20)

        self.label = Label(self.root, text="Arz Cazibesi")
        self.labelcurrentPressure = Label(self.root, text="Current Pressure is:0.00 atm|0 Hgcm")
        self.labelcurrentPressurePersentage = Label(self.root, text="Current Pressure Percentage is: 0.00%")
        self.labelexp = Label(self.root, text="    |Current Experiment Values|")
        self.labelgravity = Label(self.root, text="Gravity: 0.00")
        self.labeltime = Label(self.root, text="Time: 0.00")
        self.labelpressure = Label(self.root, text="Pressure: 0.00")

        self.button0 = Button(self.root, text="     Start Experiment      ", command=self.startexp)
        self.button1 = Button(self.root, text="  Position - Time Graphic  ", command=self.ptG)
        self.button2 = Button(self.root, text="   Speed - Time Graphic    ", command=self.stG)
        self.button3 = Button(self.root, text="Acceleration - Time Graphic", command=self.atG)
        self.button4 = Button(self.root, text="      Print on Console     ", command=self.printVal)
        self.button5 = Button(self.root, text="Adjust Pressure", command=self.adjustPressure)
        self.button6 = Button(self.root, text="         Save Data         ", command=self.toWriteFile)

        self.pressureSlider = Scale(self.root, from_=0, to=760, length=180, tickinterval=190, orient=HORIZONTAL)
        self.pressureSlider.set(760)  # change this if necessary

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

        self.label.place(x=250, y=15)
        self.labelcurrentPressure.place(x=365, y=95)
        self.labelcurrentPressurePersentage.place(x=365, y=135)
        self.labelexp.place(x=365, y=240)
        self.labelgravity.place(x=365, y=285)
        self.labeltime.place(x=365, y=325)
        self.labelpressure.place(x=365, y=365)
        self.button0.place(x=20, y=85)
        self.button1.place(x=20, y=140)
        self.button2.place(x=20, y=195)
        self.button3.place(x=20, y=250)
        self.button4.place(x=20, y=360)
        self.button5.place(x=370, y=180)
        self.button6.place(x=20, y=305)
        self.pressureSlider.place(x=585, y=170)

        self.adjustPressure(onLoop=False) #to show pressure on label

        self.root.mainloop()

    # main code goes in here
    def startexp(self):  # just for showing purposes manual inputs
        global curExNum #current experiment number

        print('Experiment is starting...')
        magnet.off()
        print('Magnet on.')
        t.sleep(0.5)
        print('Magnet off. Ball is releasing.')
        magnet.on()

        start = t.time()
        while(infra.motion_detected):
            end = t.time()

        self.time.insert(curExNum, end-start)
        self.gravity.insert(curExNum, (self.height/self.time[curExNum]**2)*2) #calculating gravity
        self.pressure.insert(curExNum, self.adjustPressure(onLoop=True))
        self.exnum.insert(curExNum, 'Exp {0:d}'.format(curExNum+1))

        self.labelgravity.config(text="Gravity: {0:0.2f}".format(self.gravity[curExNum]))
        self.labeltime.config(text="Time: {0:0.2f}".format(self.time[curExNum]))
        self.labelpressure.config(text="Pressure: {0:0.2f}".format(self.pressure[curExNum]))

        magnet.off()
        curExNum=curExNum+1



    #returns bme280 datas (pressure, temperature, humidty, time)
    def getPressure(self):
        port = 1
        address = 0x76
        bus = smbus2.SMBus(port)
        cp = bme280.load_calibration_params(bus, address) #calibration_params
        pressureData = bme280.sample(bus, address, cp)
        return pressureData


    def adjustPressure(self, onLoop=True):
        currentData = self.getPressure()
        currentPressureAtm = currentData.pressure * 0.000987
        currentPressure = currentPressureAtm * 760
        persentage = currentPressureAtm * 100
        self.labelcurrentPressure.config(text="Current Pressure is:{0:0.2f} atm|{1:d} Hgcm".format(currentPressureAtm, int(currentPressure)))
        self.labelcurrentPressurePersentage.config(text="Current Pressure Percentage is: {0:0.2f}%".format(persentage))

        pressureWanted = self.pressureSlider.get()
        if (onLoop):
            while (pressureWanted < int(currentPressure)):
                vaccum.off()
                t.sleep(0.01)

                currentData = self.getPressure()
                currentPressureAtm = currentData.pressure * 0.000987
                currentPressure = currentPressureAtm * 760
                persentage = currentPressureAtm * 100
                self.labelcurrentPressure.config(text="Current Pressure is:{0:0.2f} atm|{1:d} Hgcm".format(currentPressureAtm, int(currentPressure)))
                self.labelcurrentPressurePersentage.config(text="Current Pressure Percentage is: {0:0.2f}%".format(persentage))

                # delete this line when you add vaccum
                t.sleep(2)
                break

        vaccum.on()

        #this might not work be carefull
        if (onLoop):
            return currentPressureAtm


    # position-time graphic
    def ptG(self):
        global curExNum

        currentHeight = array.array('f')
        currentTime = array.array('f')
        for i in range(0, int(self.time[curExNum-1] * self.sensitivity)):  # this is not correct
            currentTime.insert(i, math.sqrt(i * self.time[curExNum-1] / self.sensitivity))
            currentHeight.insert(i, (0.5 * self.gravity[curExNum-1] * currentTime[i] ** 2))
            print(currentHeight[i])
        plt.figure('Arz Cazibesi')
        plt.plot(currentTime, currentHeight)
        plt.ylabel('Position')
        plt.xlabel('Time')
        plt.title('Position-Time Graphic')
        plt.show()

    # speed-time graphic
    def stG(self):
        global curExNum

        currentTime = array.array('f')
        currentSpeed = array.array('f')
        for i in range(0, int(self.time[curExNum-1] * self.sensitivity)):
            currentTime.insert(i, math.sqrt(i * self.time[curExNum-1] / self.sensitivity))
            currentSpeed.insert(i, self.gravity[curExNum-1] * currentTime[i])
            print(currentSpeed[i])
        plt.figure('Arz Cazibesi')
        plt.plot(currentTime, currentSpeed)
        plt.ylabel('Speed')
        plt.xlabel('Time')
        plt.title('Speed-Time Graphic')
        plt.show()

    # acceleration-time graphic
    def atG(self):
        global curExNum

        currentTime = array.array('f')
        currentGravity = array.array('f')
        for i in range(0, int(self.time[curExNum-1] * self.sensitivity)):
            currentTime.insert(i, math.sqrt(i * self.time[curExNum-1] / self.sensitivity))
            currentGravity.insert(i, self.gravity[curExNum-1])
        plt.figure('Arz Cazibesi')
        plt.plot(currentTime, currentGravity)
        plt.ylabel('Acceleration')
        plt.xlabel('Time')
        plt.title('Acceleration-Time Graphic')
        plt.show()

    def toWriteFile(self):
        global curExNum
        self.writeFile(expnum=curExNum)

    # writes datas on txt file
    def writeFile(self, expnum=0):
        file = open("gravity.txt", "a")
        for i in range(50):
            file.write('-')
        file.write("\nExperiment Number{0:4s}Gravity{0:4s}Pressure{0:4s}Time\n".format(' '))
        for i in range(expnum):
            file.write('{4:4s}Exp {0:d}:{1:18.6f}{2:10.2f}{3:10.4f}\n'.format(i, self.gravity[i], self.pressure[i], self.time[i], ' '))

    # prints values in console
    def printVal(self):
        global exnum

        g = pd.Series(self.gravity)
        t = pd.Series(self.time)
        Data = {'Experiment Number': self.exnum, 'Gravity': g, 'Pressure': self.pressure, 'Time': t}
        df = pd.DataFrame(Data)
        print(df)

    # fills values manualy 
    # currently offline
    def prefill(self):
        global time
        global gravity
        global exnum
        global pressure
        global height

        height = 2.0  # meters
        time = [0.61, 0.622, 0.6423, 0.6323]
        pressure = [1, 0.9, 0.81, 0.3]
        exnum = ['Exp 1:', 'Exp 2:', 'Exp 3:', 'Exp 4:']
        for i in range(0, 4):
            gravity.insert(i, 2 * height / time[i] ** 2)


if __name__ == '__main__':
    screen = gui()
