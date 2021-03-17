from gpiozero import servo
'''Motor angle calculated as percentage of the pulse cycle - called duty cycle (in %)
1ms signal corresponds to -90 deg, 1.5ms signal corresponds to 0deg, 2ms corresponds to 90
A servo uses a 50Hz control signal - period is 20ms per cycle
Therefore to obtain anticlockwise, the duty cycle must be 1/20= 5%, middle duty cycle = 7.5%, clockwise = 10%'''

#We will need to test these values, as it may vary between servos, generally 4% grants full left, 12.5% grants full right

# Class to connect and initiate rotation, then turn off - I may change this to be turned on and silently waiting for signal
class servo:
    def __init__(self, filter_colour, servo):
        self.filter_colour = filter_colour
        self.servo = servo
        self.set_filter(filter_colour)

    def set_filter(self, filter_colour):
        if filter_colour == "green":
            self.servo.min()
            print("Set to green filter")
        elif filter_colour == "red":
            self.servo.max()
            print("Set to red filter")
'''
def angle_to_percent (angle):
    if angle > 180 or angle < 0 :
        return False
    start = 4
    end = 12.5
    ratio = (end - start)/180 #Calculate ratio from angle to percent
    angle_as_percent = angle * ratio
    return start + angle_as_percent
'''



