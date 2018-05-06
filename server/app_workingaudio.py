from importlib import import_module
from flask import Flask, render_template, Response
from camera_opencv import Camera
import pyaudio
import wave
import time
import numpy as np
import array
import alsaaudio

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
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpg\r\n\r\n' + frame + b'\r\n')

@app.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(genarateVideo(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

def generateAudio():
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
                input_device_index=2)

        filepath = '/home/pi/sel373/server/teste.wav'
        filepathtest = '/home/pi/sel373/server/teste.wav'
        frames=[]
        streamIn.start_stream()
        while streamIn.is_active:
                frames=[]
                error=0
                for i in range(0, int(RATE/CHUNK*1)): #RECORD_SECONDS)):
                        data  = streamIn.read(CHUNK)
                        frames.append(data)

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


@app.route("/audio_feed")
def audio_feed():
    return Response(generateAudio(), mimetype="audio/x-wav;codec=pcm")

if __name__ == '__main__':
        app.run(host='10.235.10.44', threaded=True,port=8082)
