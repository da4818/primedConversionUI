
from gpiozero import Servo
class motor:
    def __init__(self, filter_colour):
        self.servo = Servo(17) #GPIO17 = BOARD11
        self.servo.value = 0
        self.servo.value = None #Will need to ensure the wheel is set properly when putting it into the housing
        self.set_filter(filter_colour)

    def set_filter(self, filter_colour):
        if filter_colour == "green":
            self.servo.value = 0
            print("Set to green filter")
        elif filter_colour == "red":
            self.servo.value = 0.5454545454 #value to rotate 30 degrees (from 0 to 1 is 55 degrees rotation)
            print("Set to red filter")
        self.servo.detach()
