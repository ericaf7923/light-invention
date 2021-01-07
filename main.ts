while (true) {
    // if light level is greater than 4, then set neopixels off
    console.log("light level: " + input.lightLevel())
    if (input.lightLevel() > 4) {
        light.clear()
    } else if (input.lightLevel() >= 2) {
        // if light level is equal to or greater than 2, then set neopixels pink 
        light.setAll(color.rgb(255, 56, 152))
    } else {
        light.setAll(color.rgb(255, 56, 152))
    }
    
}
