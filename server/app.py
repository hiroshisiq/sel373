from flask import Flask, render_template, Response
from camera import VideoCamera

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/webcam')
def webcam_page():
	return render_template('webcam.html')

def genarateImage(camera):
	while True:
		frame = camera.get_frame()
		yield(b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n'))

@app.route('/test')
def test_page():
	return Response(genarateImage(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
	app.run(debug=True, host='10.42.14.232', port=int("8080"))
