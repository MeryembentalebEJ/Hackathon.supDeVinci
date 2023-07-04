from flask import Flask
from flask_cors import CORS
from nmap import nmap_call

app = Flask(__name__)
cors = CORS(app)

@app.route("/nmap")
def nmap():
    print("nmap")
    nmap_call()
    return "<p>nmap!</p>"


@app.route("/wireshark")
def wireshark():
    print("nmap")
    return "<p>wireshark!</p>"