# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 11:45:09 2018

@author: Paulo Augusto
"""

import pyaudio
import wave


#record
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
WAVE_OUTPUT_FILENAME = "teste.wav"
RATE = 44100
RECORD_SECONDS = 5

p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                output=True,
                frames_per_buffer=CHUNK,
                input_device_index=1)


frames = []

for i in range(0, int(RATE/CHUNK*RECORD_SECONDS)):
    data  = stream.read(CHUNK)
    frames.append(data)
    stream.write(data)
#    yield data 



wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(b''.join(frames))
wf.close()


stream.stop_stream()
stream.close()
p.terminate()



