light.set_brightness(300)
while True: 

    #if light level is greater than 5, then set neopixels off
    print("light level: " + input.light_level())
    if input.light_level() > 5 :
        light.clear()

    #if light level is equal to or greater than 2, then set neopixels pink
    elif input.light_level() >= 2 :
        light.set_all(color.rgb(255,56,152))

    else:
        light.set_all(color.rgb(255,56,152))
    