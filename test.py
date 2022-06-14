from flask import Flask, render_template, request, redirect, url_for
from pyduino import *
import time
app = Flask(__name__)
ser = serial.Serial(
    port='COM8',\
    baudrate=9600,\
    parity=serial.PARITY_NONE,\
    stopbits=serial.STOPBITS_ONE,\
    bytesize=serial.EIGHTBITS,\
        timeout=0)

@app.route('/')
def home():
    return render_template('radarprocessing.html')

# @app.route('/data',methods=['GET'])
# def serialdata():
#     return ser.read()
while True:
    for line in ser.read():
        print(chr(line))
# print("connected to: " + ser.portstr)
# count=1

        # count = count+1

# ser.close()

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)