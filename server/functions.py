from importlib import import_module
from flask import Flask, render_template, Response, request
from camera_opencv import Camera
import pyaudio
import wave
import time


def genarateVideo(camera):
    """Video streaming generator function."""
    print('Initiating video')
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpg\r\n\r\n' + frame + b'\r\n')

def callback(in_data,frame_count,time_info,status):

        frames.append(in_data)
        time.sleep(0.01)
        return(None,pyaudio.paContinue)

def generate_Audio():
    print('Initiating audio')
    global CHUNK,FORMAT,RATE,CHANNELS
    CHUNK = 1024*4
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    WAVE_OUTPUT_FILENAME = "teste.wav"
    RATE = 44100
    RECORD_SECONDS = 10
    print('Initiating audio')
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

