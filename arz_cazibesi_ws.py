"""
this code is just to run system on console

also using zeropy to test
"""

from gpiozero import LED, MotionSensor
from time import sleep, time
import board
import digitalio
import busio
import adafruit_bmp280
import pandas as pd

i2c = busio.I2C(board.SCL, board.SDA)
bmp280 = adafruit_bmp280.Adafruit_BMP280_I2c(i2c)
bmp280.seaLevelhPa = 1013.25

print('(debug sesh)temp: {0:0.1f}'.format(bmp280.temperature))

vacum = LED(19)
magnet = LED(17) #config magnet pin
infra = MotionSensor(13) #use queue_len if it detects twitchy

def main():
    print('Experiment is starting...')
    magnet.on()
    print('Magnet on.')
    inp = input('Please enter s to start.')
    if(inp == 's'):
        print('Magnet off. Ball is releasing.')
        magnet.off()
        start = time()
        while(not infra.motion_detected()):
            end = time()
        time = end - start
        height = 100 #adjust height probably not correct
        print('Time is: {0:0.3f} \n Time^2 is: {1:0.3f} \n'.format(time,time**2))
        gravity = (height/time**2)*0.5 #calculating gravity
        print('\ngravity: {0:0.3f}\n\n'.format(gravity))
        print('Pressure: {0:0.2f}'.format(bmp280.pressure))
        print('Mapped pressure: %{0:s}'.format(returnPressure()))



def returnPressure():
    oldRange = (1013.25-0)
    newRange = (100-0)
    newValue = (((bmp280.pressure-0) * newRange) / oldRange) + 0)
    mappedPressure = str(newValue)
    return mappedPressure
