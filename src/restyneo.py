from flask import Flask, jsonify
from gpio import GPIO
import logging

app = Flask(__name__)

serviceName = "restyneo"

# default service
@app.route("/" + serviceName + "/")
def index():
    return "restyneo to the rescue!"

# export routing
@app.route("/" + serviceName + "/export/<int:pin>")
def export(pin):
    return GPIO.export(pin, True)

# change direction
@app.route("/" + serviceName + "/setDirection/<int:pin>/<direction>")
def setDirection(pin, direction):
    return GPIO.changeDirection(pin, direction)

# set value
@app.route("/" + serviceName + "/setValue/<int:pin>/<int:value>")
def setValue(pin, value):
    return GPIO.setValue(pin, value)

# unexport 
@app.route("/" + serviceName + "/unexport/<int:pin>")
def unexport(pin):
    return GPIO.export(pin, False)

# getDirection
@app.route("/" + serviceName + "/getDirection/<int:pin>")
def getDirection(pin):
    return GPIO.getDirection(pin)

# get value
@app.route("/" + serviceName + "/getValue/<int:pin>")
def getValue(pin):
    return GPIO.getValue(pin)

if __name__ == "__main__":
#    logger = logging.getLogger('werkzeug')
#    handler = logging.FileHandler('access.log')
#    logger.addHandler(handler)
#    app.logger.addHandler(handler)
    app.debug = True
    app.run(host = "0.0.0.0")
