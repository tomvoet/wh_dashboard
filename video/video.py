import cv2 as cv
from flask import Flask, render_template, Response, jsonify, make_response
from flask_cors import CORS
import json
import sqlite3
from sqlite3 import Error
import os

sql_create_table = """ CREATE TABLE IF NOT EXISTS daten(
        id integer PRIMARY KEY,
        brightness real DEFAULT 128,
        faceInShot integer DEFAULT 0
    );"""

sql_update_data_a = """
        INSERT OR IGNORE INTO daten VALUES (0, {0}, {1});
    """
sql_update_data_b = """
        UPDATE daten SET brightness = {0}, faceInShot = {1} WHERE id LIKE 0;
    """

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


def create_connection():
    connec = None;
    
    try:
        connec = sqlite3.connect("../db/data.db", check_same_thread=False)
        print(sqlite3.version)
    except Error as e:
        print(e)
    return connec
    
def create_table(create_table_sql):
    try:
        cursor.execute(create_table_sql)
    except Error as e:
        print(e)


def update_data(brightness, faceInShot):
    try:
        cursor.execute(sql_update_data_a.format(brightness, faceInShot))
        conn.commit()
        cursor.execute(sql_update_data_b.format(brightness, faceInShot))
        conn.commit()
    except Error as e:
        print(e)




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
            
            update_data(v_mean, 1 if len(faces) > 0 else 0)
            
            with open('data.json', 'w') as json_file:
                json.dump(data, json_file)

            for (x, y, w, h) in faces:
                cv.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)


            ret, buffer = cv.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

cursor = None;

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

conn = create_connection()

cursor = conn.cursor()

if conn is not None:
    create_table(sql_create_table)
else:
    print("Error! cannot create the database connection.")

 


app.run(port=8081)