# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 11:45:09 2018

@author: Paulo Augusto
"""
import gc
import pyaudio
import wave


#record
CHUNK = 2048 #1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
WAVE_OUTPUT_FILENAME = "teste.wav"
RATE = 48000
RECORD_SECONDS = 5
print('oi')
p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK
		,input_device_index=2)


frames = []

for i in range(0, int(RATE/CHUNK*RECORD_SECONDS)):
    data  = stream.read(CHUNK)
#    frames.append(data)
    frames = data
    
    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))

    print(wf.tell())

    wf.close()
    gc.collect()
    
#    yield data 



#wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
#wf.setnchannels(CHANNELS)
#wf.setsampwidth(p.get_sample_size(FORMAT))
#wf.setframerate(RATE)
#wf.writeframes(b''.join(frames))
#wf.close()


stream.stop_stream()
stream.close()
p.terminate()



