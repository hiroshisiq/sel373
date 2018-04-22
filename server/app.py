#!/usr/bin/env python
from importlib import import_module
from flask import Flask, render_template, Response
#from camera_opencv import Camera
import pyaudio
import wave

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

def genarateVideo(camera):
    """Video streaming generator function."""
    while True:
        frame = [] #camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpg\r\n\r\n' + frame + b'\r\n')

@app.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(genarateVideo(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

def generateAudio():
	CHUNK = 2048 #1024
	FORMAT = pyaudio.paInt16
	CHANNELS = 1
	WAVE_OUTPUT_FILENAME = "teste.wav"
	RATE = 48000
	RECORD_SECONDS = 10
	p1 = pyaudio.PyAudio()
#	p2 = pyaudio.PyAudio()
	streamIn = p1.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

#	streamOut = p2.open(format=FORMAT,
#                channels=CHANNELS,
#                rate=RATE,
#                output=True,
#                frames_per_buffer=CHUNK)


#	for i in range(0, int(RATE/CHUNK*RECORD_SECONDS)):
#	data = streamIn.read(CHUNK,exception_on_overflow = False)
# 	data = wav.read(2048)

 	#frames.append(data)
	#streamOut.write(data)
	filepath = '/home/pi/sel373/server/teste.wav'
	filepathtest = '/home/pi/sel373/server/teste2.wav'
#	with open(filepath,'rb')as wav:

#		data = wav.read(CHUNK)
	w=open(filepathtest,'rb')
	data=w.read(CHUNK)
	while data:
		yield data
		w.seek(0,0)
		data = w.read(CHUNK)
	w.close()

 	while data:
		print('stringmuitogrande')

#			data = wf.read(CHUNK)
#			wf.close()
		yield data
		data = streamIn.read(CHUNK)

               	wf = wave.open(filepath, 'wb')
               	wf.setnchannels(CHANNELS)
                wf.setsampwidth(p1.get_sample_size(FORMAT))
       	        wf.setframerate(RATE)
		wf.writeframes(data)
		wf.close()

		w = open(filepath,'rb')
		#wav.seek(0,0)
		data = w.read(CHUNK)
		w.close()


@app.route("/audio_feed")
def audio_feed():
    return Response(generateAudio(), mimetype="audio/x-wav;codec=pcm")

if __name__ == '__main__':
#	app.run(host='143.107.235.0', threaded=True)
	app.run(host='10.235.10.44', threaded=True,port=8082)

