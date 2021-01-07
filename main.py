while True: 

    #if light level is greater than 3, then set neopixels off
    print("light level: " + input.light_level())
    if input.light_level() > 3:
        light.clear()

    #if light level is equal to or greater than 5, then set neo pixels pink 
    elif input.light_level() >= 5 :
        light.set_all(color.rgb(255,56,152))

    else: 
        light.set_all(color.rgb(255,56,152))