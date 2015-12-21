class GPIO: 
    GPIOLIST = [4, 5, 6, 7, 116, 127, 124, 119,
                174, 175, 176, 177, 202, 203,
                21, 20, 19, 18, 17, 16, 15, 14, 22, 25,
                124, 182, 173, 172, 181, 180, 107, 106]

    DIRECTION = ["in", "out"]

    VALUE = [0, 1]

    @staticmethod
    def export(pin):
        return "Exporting pin " + str(pin)

    @staticmethod
    def changeDirection(pin, direction):
        valid = True
        if pin not in GPIO.GPIOLIST:     
            return "Pin " + str(pin) + " is not a valid pin"
        if direction not in GPIO.DIRECTION:
            return "Specified direction: " + direction + ", is not a valid direction"
        if valid:
            return "Changing direction of " + str(pin) + " to " + direction



    @staticmethod
    def setValue(pin, value):
        if pin not in GPIO.GPIOLIST:
            return "Pin " + str(pin) + " is not a valid pin"
        if value not in GPIO.VALUE:
            return "Invalid value"
        return "Setting pin " + str(pin) + " to " + str(value)
