from commander import commander
from utility import utility
from flask import jsonify

class BrickConnector:

    ERRORCODE = -1
    SUCCESSCODE = 0

    @staticmethod
    def readSensor(sensor):
        raw, error = commander.execute("cat /sys/class/i2c-dev/i2c-1/device/1-0060/iio:device0/in_" + sensor + "_raw")
        scale, error = commander.execute("cat /sys/class/i2c-dev/i2c-1/device/1-0060/iio:device0/in_" + sensor + "_scale")
        if error:
            return utility.jsonifyme(BrickConnector.ERRORCODE, error)
        else:
            value = float(raw) * float(scale)
            return jsonify(ResultCode=BrickConnector.SUCCESSCODE, 
                           Sensor=str(value))
