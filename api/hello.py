from flask import Flask
from flask_cors import CORS
from nmap import nmap_call
from elastic import persist_data
app = Flask(__name__)
cors = CORS(app)

@app.route("/nmap")
def nmap():
    print("nmap")
    data = nmap_call()
    persist_data(data)
    return "<p>nmap!</p>"


@app.route("/wireshark")
def wireshark():
    print("nmap")
    return "<p>wireshark!</p>"