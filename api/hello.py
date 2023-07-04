from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)

@app.route("/nmap")
def nmap():
    print("nmap")
    return "<p>nmap!</p>"


@app.route("/wireshark")
def wireshark():
    print("nmap")
    return "<p>wireshark!</p>"