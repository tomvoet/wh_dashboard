import cv2 as cv
from flask import Flask, render_template, Response
from flask_cors import CORS
import json

face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
#https://www.pyimagesearch.com/2018/09/24/opencv-face-recognition/
app = Flask(__name__)
CORS(app)

cors = CORS(app, resource={
    r"/*":{
        "origins":"*"
    }
})

data = {
    "faceInShot": "false",
    "brightness": 128
}

app = Flask(__name__)

cam = cv.VideoCapture(0)

def gen_frames():  
    while True:
        success, frame = cam.read()  
        if not success:
            break
        else:
            frame_hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
            _, _, v_mean, _ = cv.mean(frame_hsv)
            print(v_mean)
            
            gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

            faces = face_cascade.detectMultiScale(gray, 1.1, 5)

            data["faceInShot"] = True if len(faces) > 0  else False
            data["brightness"] = v_mean
            
            with open('data.json', 'w') as json_file:
                json.dump(data, json_file)

            for (x, y, w, h) in faces:
                cv.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)


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