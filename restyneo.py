from flask import Flask, jsonify
from gpio import GPIO

app = Flask(__name__)

@app.route("/")
def index():
    return "restyneo to the rescue!"

# export routing
@app.route("/export/<int:pin>")
def export(pin):
    return GPIO.export(pin)

# change direction
@app.route("/direction/<int:pin>/<direction>")
def direction(pin, direction):
    return GPIO.changeDirection(pin, direction)

# set value
@app.route("/value/<int:pin>/<int:value>")
def value(pin, value):
    return GPIO.setValue(pin, value)

if __name__ == "__main__":
    app.debug = True
    app.run(host = "0.0.0.0")
