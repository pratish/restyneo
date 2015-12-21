from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return "restyneo to the rescue!"

# export routing
@app.route("/export/<int:gpio>")
def export(gpio):
    return "exporting pin " + str(gpio)

if __name__ == "__main__":
    app.debug = True
    app.run(host = "0.0.0.0")
