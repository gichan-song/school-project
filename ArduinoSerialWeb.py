from flask import Flask
from flask import request
from flask import render_template
from flask import Response
#from threading import Thread
import serial


web_gui=Flask(__name__)

def serial_start():
    ser=serial.Serial('COM8',115200)
    stop_flag=False
    while not stop_flag:
        if ser.readable():
            res=ser.readline()
            res_decode=res.decode()
            print(res_decode)

@web_gui.route('/')
def hello_fnc():
    Response(serial_start())
    return 'Hello'

@web_gui.route('/page',methods=['GET','POST'])
def page_fnc():
    if request.method=='POST':
        return 'POST received'
    else:
        return render_template('page.html')

web_gui.run(debug=True,port=9999)