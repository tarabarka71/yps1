from flask import Flask, request, jsonify
import random
import time

app = Flask(__name__)

@app.route("/temperature/<location>")
def get_temperature(location):
    import random
    value = round(random.uniform(15.0, 30.0), 2)
    return {"Value": value}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8081, debug=True)
