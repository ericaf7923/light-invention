while True: 

    #if light level is greater than 4, then set neopixels off
    print("light level: " + input.light_level())
    if input.light_level() > 4:
        light.clear()

    #if light level is equal to or greater than 2, then set neopixels pink 
    elif input.light_level() >= 2 :
        light.set_all(color.rgb(255,56,152))

    else: 
        light.set_all(color.rgb(255,56,152))