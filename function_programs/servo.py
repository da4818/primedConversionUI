from gpiozero import Servo
from time import sleep
class Motor:
    def __init__(self):
        self.servo = Servo(17) #GPIO17 = BOARD11
        print("Motor connected")
        self.servo.value = 0
        #self.servo.value = None #Will need to ensure the wheel is set properly when putting it into the housing

    def set_filter(self, filter_colour):
        if filter_colour == "green_excitation":
            self.servo.value = 0
            sleep(1)
            self.servo.value = None
            print("Set to green filter")
        elif filter_colour == "red_excitation":
            self.servo.value = 0.545454 #value to rotate 30 degrees (from 0 to 1 is 55 degrees rotation)
            sleep(1)
            self.servo.value = None
            print("Set to red filter")
        self.servo.detach()