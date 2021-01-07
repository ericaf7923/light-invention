while (true) {
    // if light level is greater than 3, then set neopixels off
    console.log("light level: " + input.lightLevel())
    if (input.lightLevel() > 3) {
        light.clear()
    } else if (input.lightLevel() >= 5) {
        // if light level is equal to or greater than 5, then set neo pixels pink 
        light.setAll(color.rgb(255, 56, 152))
    } else {
        light.setAll(color.rgb(255, 56, 152))
    }
    
}
