def raspi_connection(var):

    from gpiozero import PWMOutputDevice
    from time import sleep
    # assigning integers representing GPIO pins (in broadcam representation)
    UV405 = 17
    blue494 = 27
    red630 = 22
    lime540 = 23

    if(var == 'UV'):
        # initializing Pin connected to transistor controlling current to UV LED circuit
        # initial value is 1 or on at full. Duty cycle is then 1->0->1 at X frequency
        # can choose different duty cycle start e.g., initial_value=0.9: 0.9->0.1->0.9 at X frequency
        # chose to have pin on HIGH at initialisation and turn it off after 2sec for faster/shorter code
        led = PWMOutputDevice(UV405,initial_value=1,frequency=1000) # need to check frequency capabilities of 2N7000 transistor
        # program stops for 2 seconds then turns the led off
        sleep(2)
        led.off()

    elif(var =='PC'):
        # same process as above but for primed conversion LEDs
        blue_priming = PWMOutputDevice(blue494,initial_value=1,frequency=1000)
        red_converting = PWMOutputDevice(red630,initial_value=1,frequency=1000)
        sleep(2)
        blue_priming.off()
        red_converting.off()
    elif(var =='green_excitation'):
        led = PWMOutputDevice(blue494,initial_value=1,frequency=1000)
        sleep(2)
        led.off()
    elif(var =='red_excitation'):
        led = PWMOutputDevice(lime540,initial_value=1,frequency=1000)
        sleep(2)
        led.off()

if __name__ == "__main__":
    raspi_connection('red_connection')