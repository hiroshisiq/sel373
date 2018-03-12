from flask import Flask, render_template, Response

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/webcam')
def webcam_page():
	return render_template('webcam.html')

if __name__ == '__main__':
	app.run(debug=True, host='10.42.14.232', port=int("8080"))
