

import serial
#Import serial is used to conenct the python file with hardware
#Pyserial is the library to upload

import time

arduino=serial.Serial('/dev/cu.usbmodem14201(Arduino Uno)', 9600)
#Between the '' you need to write the port that is used for the arduino
#It might be different for everyones computer, I am not sure, but that's what i wrote for mine
# you can find the exact name of the port on the arduino software


#I know this is a separate file, I tried to run it by creating another project, but it did not work
#I guess the problem comes from the port as the program could not find it
#I can try to do it again once I get the cable back

time.sleep(2)
print("Enter 1 to turn on LED and 0 to turn off LED")


while 1:
    datafromUser= input()
    if datafromUser =='1':
        arduino.write('1')
        print("LED is turned on")

    elif datafromUser =='O':
        arduino.write('0')
        print("LED is turned off")


