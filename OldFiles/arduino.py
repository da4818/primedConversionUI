def arduino_connection(var):
    #from pip._vendor.distlib.compat import raw_input
    import serial
    import time
    port = "/dev/cu.usbmodem143201" #This port name is found on arduino>tools>port
    ard = serial.Serial(port, 9600, timeout=0.1) #9600 is the baudrate - should be the same for all devices
    t = 0
    ard_data = []
    while 1:
        if(var == 'UV'):
            ard.write(b'1') #Writing 1 to the arduino effectively sets val to 1 (see arduino code)
            data = len(ard.readline()) #When an LED is turned on, the arduino will write "ON\n", this data can be read through python
            if (data==3): # "ON\n" is 3 characters long--> \n counts as the 3rd character
                break #This stops the LED from blinking in a loop
        elif(var =='PC'):
            ard.write(b'2')
            data = len(ard.readline()) #Similar to above
            if (data==3):
                break
        elif(var =='green_excitation'):
            ard.write(b'3')
            data = len(ard.readline()) #Similar to above
            if (data==3):
                break
        elif(var =='red_excitation'):
            ard.write(b'4')
            data = len(ard.readline()) #Similar to above
            if (data==3):
                break








    '''while 1 and t<2:
        if (var == '1'): #If the value is 1
            print("Green LED turned ON")
            ard.write(b'1') #Sends 1 to arduino - equivalent of writing HIGH to the pin
            time.sleep(2)
            #if (t == 0):
            #    print("Green LED turned ON")
            ard.write(b'0')
            t = t+1
        if (var == '0'): #if the value is 0
            ard.write(b'0') #Sends 1 to arduino - equivalent of writing LOW to the pin
            print("Green LED turned OFF")
        if (var == '2'): #if the value is 0
            ard.write(b'2') #Sends 1 to arduino - equivalent of writing LOW to the pin
            print("Red LED turned OFF")
        if (var == '3'): #if the value is 0
            print("Red LED turned ON")
            ard.write(b'3') #Sends 1 to arduino - equivalent of writing LOW to the pin
            time.sleep(2)
            ard.write(b'2')
            t = t+1'''
    ard.close()

if __name__ == "__main__":
    arduino_connection('red')


'''
print ("Enter 1 to get LED ON & 0 to get OFF")
while 1:      #Do this in loop

    var = raw_input() #get input from user
    if (var == '1'): #if the value is 1
        ard.write(b'1') #send 1
        #led.value = True
        print ("LED turned ON")
        print(ard.readline())
        #time.sleep(1)
    if (var == '0'): #if the value is 0
        ard.write(b'0') #send 0
        #led.value = False
        print ("LED turned OFF")
        print(ard.readline())
        #time.sleep(1) '''