# LEDs turned on by setting output pin to transistor gate voltage value to 0.9 = 3V, as 1 = 3.3V
def excitation_on(colour, excitation_leds):
    led = excitation_leds[colour]
    led.value = 0.9

def raspi_turnoff(gpio_class):
    for led in gpio_class.leds:
        led.off()

def set_filter(servo, filter_colour):
    if filter_colour == "green_excitation":
        servo.min()
        print("Set to green filter")
    elif filter_colour == "red_excitation":
        servo.max()
        print("Set to red filter")
"""
# function currently unused, will be replaced by pc/primed conversion led function(s)
def raspi_turnon(colour, gpio_class):
    for led in gpio_class.leds:
        # will need to make sure red_priming is referenced when priming so loop can turn both priming leds on
        if colour == led:
            # if statement turns 494nm LED and 630nm LED on for primed conversion
            if colour == "red_priming":
                gpio_class.leds[1].value = 0.9   # leds[1] is the 494nm LED.
            # turning UV LED on or pin output at HIGH (~3.3V)
            led[1].value = 0.9
            # program stops for 2 seconds then turns the led off
"""
if __name__ == "__main__":
    pass
