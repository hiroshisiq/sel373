#!/usr/bin/env python
from importlib import import_module
from flask import Flask, render_template, Response
#from camera_opencv import Camera
import pyaudio

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/camera')
def camera_page():
	return render_template('camera.html')

@app.route('/getapp')
def getapp_page():
	return render_template('getapp.html')

@app.route('/about')
def about_page():
	return render_template('about.html')

#def genarateVideo(camera):
#    """Video streaming generator function."""
#    while True:
#        frame = camera.get_frame()
#        yield (b'--frame\r\n'
#               b'Content-Type: image/jpg\r\n\r\n' + frame + b'\r\n')

#@app.route('/video_feed')
#def video_feed():
#    """Video streaming route. Put this in the src attribute of an img tag."""
#    return Response(genarateVideo(Camera()),
#                    mimetype='multipart/x-mixed-replace; boundary=frame')

def generateAudio():
	CHUNK = 1024
	FORMAT = pyaudio.paInt16
	CHANNELS = 1
	WAVE_OUTPUT_FILENAME = "teste.wav"
	RATE = 44100
	RECORD_SECONDS = 3600
	p = pyaudio.PyAudio()
	stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                output=True,
                frames_per_buffer=CHUNK)

	for i in range(0, int(RATE/CHUNK*RECORD_SECONDS)):
   		data  = stream.read(CHUNK)
    		stream.write(data)

@app.route("/audio_feed")
def audio_feed():
    return Response(generateAudio(), mimetype="audio/x-wav")

if __name__ == '__main__':
#	app.run(host='143.107.235.0', threaded=True)
	app.run(host='10.235.10.44', threaded=True)
