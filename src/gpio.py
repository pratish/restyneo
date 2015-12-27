from commander import commander
from utility import utility

class GPIO: 
    GPIOLIST = [4, 5, 6, 7, 116, 127, 124, 119,
                174, 175, 176, 177, 202, 203,
                21, 20, 19, 18, 17, 16, 15, 14, 22, 25,
                124, 182, 173, 172, 181, 180, 107, 106]
    DIRECTION = ["in", "out"]
    VALUE = [0, 1]
    ERRORCODE = -1
    SUCCESSCODE = 0
    BASE_PATH = "/sys/class/gpio/"

    @staticmethod
    def export(pin, shouldExport):
        if pin not in GPIO.GPIOLIST:
            return utility.jsonifyme(GPIO.ERRORCODE, "Pin " + str(pin) + " is not a valid gpio pin")

        fullPath = GPIO.BASE_PATH + "gpio" + str(pin) + "/"

        if shouldExport:
            export = "export"
        else:
            export = "unexport"

        if not commander.checkFile(fullPath):
            executionResult, error = commander.execute("echo " + str(pin) + " > " + GPIO.BASE_PATH + export)
            if error:
                return utility.jsonifyme(GPIO.ERRORCODE, error)     
            else:
                return utility.jsonifyme(GPIO.SUCCESSCODE, "Pin " + str(pin) + " successfully exported")
        else:
            if not shouldExport:
                executionResult, error = commander.execute("echo " + str(pin) + " > " + GPIO.BASE_PATH + export)
                if error: 
                    return utility.jsonifyme(GPIO.ERRORCODE, error)
                else:
                    return utility.jsonifyme(GPIO.SUCCESSCODE, "Pin " + str(pin) + " successfully unexported")
            else:
                return utility.jsonifyme(GPIO.ERRORCODE, "Pin already exported") 

    @staticmethod
    def changeDirection(pin, direction):
        if pin not in GPIO.GPIOLIST:     
            return utility.jsonifyme(GPIO.ERRORCODE, "Pin " + str(pin) + " is not a valid pin")
        if direction not in GPIO.DIRECTION:
            return utility.jsonifyme(GPIO.ERRORCODE, "Specified direction: " + direction + ", is not a valid direction")
        
        fullPath = GPIO.BASE_PATH + "/gpio" + str(pin) + "/direction"
        if commander.checkFile(fullPath):
            executionResult, error = commander.execute("echo " + direction + " > " + fullPath)
            if error:
                return utility.jsonifyme(GPIO.ERRORCODE, error)
            else:
                return utility.jsonifyme(GPIO.SUCCESSCODE, "Direction of pin " + str(pin) + " is set to '" + direction + "'")
        else: 
            return utility.jsonifyme(GPIO.ERRORCODE, "Pin " + str(pin) + " probably hasn't been exported yet")
    
    @staticmethod
    def getDirection(pin):
        if pin not in GPIO.GPIOLIST:     
            return utility.jsonifyme(GPIO.ERRORCODE, "Pin " + str(pin) + " is not a valid pin")
        
        fullPath = GPIO.BASE_PATH + "/gpio" + str(pin) + "/direction"
        if commander.checkFile(fullPath):
            executionResult, error = commander.execute("cat " + fullPath)
            if error:
                return utility.jsonifyme(GPIO.ERRORCODE, error)
            else:
                return utility.jsonifyme(GPIO.SUCCESSCODE, "Pin " + str(pin) + ": " + executionResult)
        else: 
            return utility.jsonifyme(GPIO.ERRORCODE, "Pin " + str(pin) + " probably hasn't been exported yet")



    @staticmethod
    def setValue(pin, value):
        if pin not in GPIO.GPIOLIST:
            return utility.jsonifyme(GPIO.ERRORCODE, "Pin " + str(pin) + " is not a valid pin")
        if value not in GPIO.VALUE:
            return utility.jsonifyme(GPIO.ERRORCODE, "Invalid value")

        fullPath = GPIO.BASE_PATH + "/gpio" + str(pin) + "/value"

        if commander.checkFile(fullPath):
            executionResult, error = commander.execute("echo " + str(value) + " > " + fullPath)
            if error: 
                return utility.jsonifyme(GPIO.ERRORCODE, error)
            else:
                return utility.jsonifyme(GPIO.SUCCESSCODE, "Setting pin " + str(pin) + " to " + str(value))
        else:
            return utility.jsonifyme(GPIO.ERRORCODE, "Pin " + str(pin) + " probably hasn't been exported yet")


    @staticmethod
    def getValue(pin):
        if pin not in GPIO.GPIOLIST:
            return utility.jsonifyme(GPIO.ERRORCODE, "Pin " + str(pin) + " is not a valid pin")

        fullPath = GPIO.BASE_PATH + "/gpio" + str(pin) + "/value"

        if commander.checkFile(fullPath):
            executionResult, error = commander.execute("cat " + fullPath)
            if error: 
                return utility.jsonifyme(GPIO.ERRORCODE, error)
            else:
                return utility.jsonifyme(GPIO.SUCCESSCODE, "Pin " + str(pin) + ": " + executionResult)
        else:
            return utility.jsonifyme(GPIO.ERRORCODE, "Pin " + str(pin) + " probably hasn't been exported yet")


