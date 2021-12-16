import cv2 as cv
from flask import Flask, render_template, Response, jsonify, make_response
from flask_cors import CORS
import json
import sqlite3
import os
import imutils
from imutils.video import VideoStream
import numpy as np
import time
timenow = {time: 0}
timenow["time"] = time.time()

face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')

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

vs = VideoStream(src=0).start() #use of imutils Threaded Videocapture
net = cv.dnn.readNetFromCaffe("deploy.prototxt.txt", "res10_300x300_ssd_iter_140000.caffemodel")
minConfidence = 0.5

def gen_frames():  
    while True:
        success = True
        frame = vs.read()
        (h, w) = frame.shape[:2]

        now_b = time.time()
        print(now_b - timenow["time"])
        timenow["time"] = time.time()
        if not success:
            break
        else:
            res = cv.flip(frame, 1)
            frame = imutils.resize(frame, width=400)
            frame_hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
            _, _, v_mean, _ = cv.mean(frame_hsv)

            (h, w) = res.shape[:2] #(480, 640)
            blob = cv.dnn.blobFromImage(cv.resize(frame, (300, 300)), 1.0,
		    (300, 300), (104.0, 177.0, 123.0))
            
            
            net.setInput(blob)
            detections = net.forward()
            faceInShot = False
            
            
            for i in range(0, detections.shape[2]):
                confidence = detections[0, 0, i, 2]
                
                if confidence < minConfidence:
                    continue
                
                faceInShot = True
                
                box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
                (startX, startY, endX, endY) = box.astype("int")
        
                startX = w - startX
                endX = w - endX
                
                text = "{:.2f}%".format(confidence * 100)
                
                y = startY - 10 if startY - 10 > 10 else startY + 10
                cv.rectangle(res, (startX, startY), (endX, endY),
                    (0, 255, 0), 2)
                cv.putText(res, text, (endX, y),
                cv.FONT_HERSHEY_SIMPLEX, 0.45, (0, 255, 0), 2)
                
            data["faceInShot"] = faceInShot
            data["brightness"] = v_mean

            ret, buffer = cv.imencode('.bmp', res)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/bmp\r\n\r\n' + frame + b'\r\n')

#cursor = None;

@app.route('/')
def index():
    return Response(response=render_template('index.html'))

@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/get_data')
def get_data():
    response = make_response(jsonify(data))
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response

app.run(port=8081)
