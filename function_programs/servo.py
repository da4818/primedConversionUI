
import time
import RPi.GPIO as GPIO
'''Motor angle calculated as percentage of the pulse cycle - called duty cycle (in %)
1ms signal corresponds to -90 deg, 1.5ms signal corresponds to 0deg, 2ms corresponds to 90
A servo uses a 50Hz control signal - period is 20ms per cycle
Therefore to obtain anticlockwise, the duty cycle must be 1/20= 5%, middle duty cycle = 7.5%, clockwise = 10%'''

#We will need to test these values, as it may vary between servos, generally 4% grants full left, 12.5% grants full right

#servo_cycle = 20 #in ms
#duty_cycle180 = 2.5/servo_cycle

#1ms - fast anticlockwise, 1.5ms-stop, 2ms - fast clockwise
def angle_to_percent (angle):
    if angle > 180 or angle < 0 :
        return False

    start = 4
    end = 12.5
    ratio = (end - start)/180 #Calculate ratio from angle to percent

    angle_as_percent = angle * ratio

    return start + angle_as_percent

def set_filter(filter,pwm):
    if filter == "red":
        pwm.ChangeDutyCycle(angle_to_percent(0))
    elif filter == "green":
        pwm.ChangeDutyCycle(angle_to_percent(180))


# Function to set up the
def start_servo():
    GPIO.setmode(GPIO.BOARD) #Use Board numerotation mode
    GPIO.setwarnings(False) #Disable warnings
    #Use pin 12 for PWM signal
    servo_pin = 12 #pin number
    frequency = 50 #50Hz - 20ms pulse width/cycle
    GPIO.setup(servo_pin, GPIO.OUT)
    pwm = GPIO.PWM(servo_pin, frequency)
    pwm.start(angle_to_percent(0))



    #Close GPIO & cleanup
    def stop_servo():
        pwm.stop()
        GPIO.cleanup()




