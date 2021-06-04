#import RPi.GPIO as GPIO
#from gpipzero import DigitalOutputDevice -> gpiozero.LED extends DigitalOutputDevice

from gpiozero import LED
import time
class LEDs:
    def __init__(self):
        self.lime = LED(17) #GPIO17 = BOARD11
        self.red = LED(18) #GPIO18 = BOARD12˚
        self.blue = LED(22) #GPIO22 = BOARD15
        #self.uv = LED(23) #GPIO23 = BOARD16
        self.lime.off()
        self.red.off()
        #self.blue.off()
        #self.uv.off()
    def illuminate(self,led):
        if led == "pr": #Primed conversion - priming and converting beams simultaneously
            print("Starting Primed Conversion")
            self.red.on()
            self.blue.on()
            time.sleep(5) #set time for primed conversion
            self.red.off()
            self.blue.off()
            print("Finished Primed Conversion")
        elif led == "pc":
            print("Starting Photo Conversion")
            #self.uv.on()
            time.sleep(5)
            #self.uv.off()
            print("Finished Photo Conversion")
        elif led == "green_excitation":
            print("Starting Green Excitation")
            self.lime.on()
            time.sleep(5)
            self.lime.off()
            print("Finished Green Excitation")
        elif led == "red_excitation":
            print("Starting Red Excitation")
            self.red.on()
            time.sleep(5)
            self.red.off()
            print("Finished Red Excitation")
