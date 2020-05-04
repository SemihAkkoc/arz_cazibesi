"""
TODO:
import bmp280
setup the sensors
write general algorithm
due to values make a graph
"""

import RPi.GPIO as GPIO
import time
import board
import digitalio
import busio
import adafruit_bmp280
from tkinter import*

i2c = busio.I2C(board.SCL, board.SDA)
bmp280 = adafruit_bmp280.Adafruit_BMP280_I2C(i2c)

bmp280.seaLevelhPa = 1013.25

print('temp: {0.1f}'.format(bmp280.temperature))

vacum_pump = 19
infra_sens = 13

GPIO.setwarnings(False)
GPIO.cleanup()
GPIO.setmode(GPIO.BCM)
GPIO.setup(vacum_pump, GPIO.OUT)
GPIO.setup(infra_sens, GPIO.IN)

class screen():
    def __init__(self): #create a root and make it dynamic
        self.root = Tk()
        self.root.title('Arz Cazibesi')
        self.root.geometry('400x300')
        self.root.resizable(False,False) #disables resizing

        self.pressureValue = StringVar()
        self.pressureValue.set("Pressure: ")
        self.labelPressure = Label(root, textvariable=self.pressureValue)
        self.labelPressure.config(font=("Courier 20 bold"))
        self.labelPressure.place(x=160,y=10)

    def buttonPressed(self): #check if pressed or not
        

def main():
