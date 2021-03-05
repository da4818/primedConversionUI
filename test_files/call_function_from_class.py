import time
class servo:
    def __init__(self, input):
        self.colour = input
        #Use pin 12 for PWM signal
        servo_pin = 12 #pin number
        frequency = 50 #50Hz - 20ms pulse width/cycle
        print("Servo pin:",servo_pin,"Servo frequency:",frequency)
        self.set_filter(self.colour)
        time.sleep(1)
        print("servo stopped")

    def set_filter(self,colour):
        if colour == "red":
            alpha = 0
            duty_cycle = angle_to_percent(0)
            print("Set to red filter")
        elif colour == "green":
            alpha = 180
            duty_cycle = angle_to_percent(180)
            print("Set to green filter")
        print("Angle:",alpha,"Duty cycle:",duty_cycle)

def angle_to_percent (angle):
    if angle > 180 or angle < 0 :
        return False
    start = 4
    end = 12.5
    ratio = (end - start)/180 #Calculate ratio from angle to percent
    angle_as_percent = angle * ratio
    return start + angle_as_percent


if __name__ == "__main__":
    #s = servo("green")
    print (__file__)

