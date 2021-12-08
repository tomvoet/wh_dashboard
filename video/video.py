import cv2 as cv
from flask import Flask, render_template, Response
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

cors = CORS(app, resource={
    r"/*":{
        "origins":"*"
    }
})

app = Flask(__name__)

cam = cv.VideoCapture(0)

def gen_frames():  
    while True:
        success, frame = cam.read()  
        if not success:
            break
        else:
            ret, buffer = cv.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')



@app.route('/')
def index():
    return Response(response=render_template('index.html'))

@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


app.run(port=8081)