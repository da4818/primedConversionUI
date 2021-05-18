def raspi_turnon(colour, gpio_class):
    from gpiozero import DigitalOutputDevice
    for led in gpio_class.leds:
        # will need to make sure red_priming is referenced when priming so loop can turn both priming leds on
        if colour == led[0]:
            # if statement turns 494nm LED and 630nm LED on for primed conversion
            if colour == "red_priming":
                gpio_class.leds[1][1].on()    # leds[1] is the 494nm LED.
            # turning UV LED on or pin output at HIGH (~3.3V)
            led[1].on()
            # program stops for 2 seconds then turns the led off


def raspi_turnoff(gpio_class):
    for led in gpio_class.leds:
        # will need to make sure red_priming is referenced when priming so loop can turn both priming leds on
        led[1].off()


'''
old function
def raspi_connection(var,gpio_class):

    from gpiozero import DigitalOutputDevice
    from time import sleep
    # initializing output pins and setting them LOW to ensure transistor gates are all closed on startup
    if(var == 'UV'):
        # turning UV LED on or pin output at HIGH (~3.3V)
        UV405.on()
        # program stops for 2 seconds then turns the led off
        sleep(2)
        UV405.off()

    elif(var =='PC'):
        # same process as above but for primed conversion LEDs
        blue494.on()
        red630.on()
        sleep(2)
        blue494.off()
        red630.off()
    elif(var =='green_excitation'):
        blue494.on()
        sleep(2)
        blue494.off()
    elif(var =='red_excitation'):
        lime540.on()
        sleep(2)
        lime540.off()
'''
'''if __name__ == "__main__":
    raspi_connection('red_connection')'''