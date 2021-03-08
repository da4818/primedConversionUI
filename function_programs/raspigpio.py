def raspi_connection(var):

    from gpiozero import DigitalOutputDevice
    from time import sleep


    # initializing output pins and setting them LOW to ensure transistor gates are all closed on startup
    UV405 = DigitalOutputDevice(17,initial_value=0)
    blue494 = DigitalOutputDevice(27,initial_value=0)
    red630 = DigitalOutputDevice(22,initial_value=0)
    lime540 = DigitalOutputDevice(23,initial_value=0)

    if(var == 'UV'):
        # turning UV LED on or pin output at HIGH (~3.3V)
        UV405.on()
        # program stops for 2 seconds then turns the led off
        sleep(2)
        led.off()

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

if __name__ == "__main__":
    raspi_connection('red_connection')