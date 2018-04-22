#!/usr/bin/env python
from importlib import import_module
from flask import Flask, render_template, Response, request
from camera_opencv import Camera
from gpio_control import GPIOControl

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

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

@app.route('/getapp')
def getapp_page():
	return render_template('getapp.html')

@app.route('/about')
def about_page():
	return render_template('about.html')

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

def generateAudio():
	with open("/home/hiroshi.siq/Documents/sel373/server/static/test.wav", "rb") as fwav:
		data = fwav.read(1024)
		while data:
			yield data
			data = fwav.read(1024)

@app.route("/audio_feed")
def audio_feed():
    return Response(generateAudio(), mimetype="audio/x-wav")

if __name__ == '__main__':
#	app.run(host='192.168.0.103', threaded=True)
	app.run(host='10.235.10.44', threaded=True,  port=8080)
