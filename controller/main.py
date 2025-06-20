from flask import Flask, render_template, request
import os
from datetime import datetime

app = Flask(__name__, template_folder="templates")

bots = [
    {"id": "001", "os": "Windows 10", "status": "Online", "last_seen": "5s ago"},
    {"id": "002", "os": "Windows 11", "status": "Idle", "last_seen": "2 min ago"},
]

logs = [
    {"time": "12:01", "msg": "Bot 001 connected."},
    {"time": "12:02", "msg": "Bot 002 idle."}
]

@app.route("/")
def index():
    return render_template("index.html", bots=bots, logs=logs)

@app.route("/cmd", methods=["POST"])
def command():
    cmd = request.form.get("cmd")
    logs.append({"time": datetime.now().strftime("%H:%M"), "msg": f"Command sent: {cmd}"})
    return render_template("index.html", bots=bots, logs=logs)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host="0.0.0.0", port=port)
