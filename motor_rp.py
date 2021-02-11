
#Brown wire to the ground
#red wire to 5V
#Brown wire to pin9


#I wanted to create an arduino file that would turn the servo motor by 180°
#However, I know that to connect the python file, we need to have the arduino code running,
#But as it needs to turn only once when we press the button, it does not really work as the motor would
#turn as soon as the code would run
#I need to figure out a way where clinking "red excitation" button and "green excitation button
#would make the arduino code start.


def arduino_rp ():
    #from pip._vendor.distlib.compat import raw_input
    import serial
    import time
    port = "/dev/cu.usbmodem14201" #This port name is found on arduino>tools>port
    ard = serial.Serial(port, 9600, timeout=0.1) #9600 is the baudrate - should be the same for all devices
    t = 0
    ard_data = []
    pos = 0;
    while 1:
        while pos<=180:
            myservo.write(pos);
        pos+=1


