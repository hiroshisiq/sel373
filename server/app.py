#!/usr/bin/env python
from importlib import import_module
from flask import Flask, render_template, Response
from camera_opencv import Camera

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

def gen(camera):
    """Video streaming generator function."""
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpg\r\n\r\n' + frame + b'\r\n')

@app.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
	app.run(host='0.0.0.0', threaded=True)
#	app.run(debug=True, host='10.42.14.232', port=8080)
