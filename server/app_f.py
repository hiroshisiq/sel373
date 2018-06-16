from importlib import import_module
from flask import Flask, render_template, Response, request
from camera_opencv import Camera
import pyaudio
import wave
import subprocess
import time
import numpy as np
from gpio_control import GPIOControl
import json
import subscription_manager as subManager
import functions

app = Flask(__name__)

@app.route('/')
def index():
        return render_template('index.html')

@app.route('/recorder')
def recorder_page():
        return render_template('RecorderDemo.html')

@app.route('/camera')
def camera_page():
        return render_template('camera.html')

@app.route('/handler', methods = ['GET', 'POST'])
def handler_page():
        if request.method == 'POST':
                print('Handling post')
                control = GPIOControl()
                control.openDoor()
                return 'Handle Post'
        if request.method == 'GET':
                print('Handling post')
                return 'Handle Get'

@app.route('/subscription', methods=['POST'])
def subscription():
    request.get_data()
    userSubscription = request.json
    subManager.appendSubscription(userSubscription)
    return 'ok'

@app.route('/saveaudio', methods=['POST'])
def saveaudio():
    audio = request
    audio.get_data()
    record = audio.data
    wf = wave.open('/home/pi/sel373/server/out.wav', 'wb')
    wf.setnchannels(1)
    wf.setsampwidth(4) #p1.get_sample_size(FORMAT))
    wf.setframerate(44100)
    wf.writeframes(record)
    wf.close()
    #time.sleep(0.1)
    subprocess.run(["play","out.wav"])

    return 'ok'

@app.route('/duplicate')
def duplicate():
    subManager.removeDuplicate()
    return 'ok'

@app.route('/getapp')
def getapp_page():
        return render_template('getapp.html')

@app.route('/microfone')
def microfone_page():
        return render_template('microfone.html')

@app.route('/about')
def about_page():
        return render_template('about.html')

@app.route('/micro')
def micro_page():
        return render_template('micro.html')


@app.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(functions.genarateVideo(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route("/audio_feed")
def audio_feed():
    print('audiofeed')
    return Response(functions.generate_Audio(), mimetype="audio/wav")

@app.route('/service-worker.js')
def sw():
    return app.send_static_file('js/service-worker.js')

if __name__ == '__main__':
# app.run(host='localhost', threaded=True, port=8080, ssl_context='adhoc')
    app.run(host='10.235.10.44', threaded=True,  port=8080, ssl_context=('ssl/certificate.crt', 'ssl/private.key'))
# app.run(host='10.235.10.44', threaded=True,  port=8080, ssl_context='adhoc')

