from importlib import import_module
from flask import Flask, render_template, Response, request
from camera_opencv import Camera
import pyaudio
import wave
import time
import numpy as np
from gpio_control import GPIOControl
import json
import subscription_manager as subManager

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
    userSubscription = request.json
    subManager.appendSubscription(userSubscription)
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

def genarateVideo(camera):
    """Video streaming generator function."""
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpg\r\n\r\n' + frame + b'\r\n')

@app.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(genarateVideo(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')
def callback(in_data,frame_count,time_info,status):

        frames.append(in_data)
        time.sleep(0.01)
        return(None,pyaudio.paContinue)

def generateAudio():
        global CHUNK,FORMAT,RATE,CHANNELS
        CHUNK = 1024*4
        FORMAT = pyaudio.paInt16
        CHANNELS = 1
        WAVE_OUTPUT_FILENAME = "teste.wav"
        RATE = 44100
        RECORD_SECONDS = 10

        p1 = pyaudio.PyAudio()
        streamIn = p1.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK,
                input_device_index=2,
                stream_callback=callback)

        filepath = '/home/pi/sel373/server/teste.wav'
        filepathtest = '/home/pi/sel373/server/teste.wav'
        global frames;

        while True:
            frames=[]
            while len(frames)<15:
                time.sleep(0.01)
            wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
            wf.setnchannels(CHANNELS)
            wf.setsampwidth(p1.get_sample_size(FORMAT))
            wf.setframerate(RATE)
            wf.writeframes(b''.join(frames))
            wf.close()

            with open(filepath, 'rb') as wav:
                    data = wav.read(CHUNK)
                    while data:
                            yield data
                            data = wav.read(CHUNK)
                    wav.close()

        stream.stop_stream()
        stream.close()


@app.route("/audio_feed")
def audio_feed():
    return Response(generateAudio(), mimetype="audio/x-wav;codec=pcm")

@app.route('/service-worker.js')
def sw():
    return app.send_static_file('js/service-worker.js')

if __name__ == '__main__':
    # app.run(host='localhost', threaded=True, port=8080, ssl_context='adhoc')
    app.run(host='10.235.10.44', threaded=True,  port=8080, ssl_context=('ssl/certificate.crt', 'ssl/private.key'))
    # app.run(host='10.235.10.44', threaded=True,  port=8080, ssl_context='adhoc')
