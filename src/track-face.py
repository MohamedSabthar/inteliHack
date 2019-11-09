import numpy as np
import cv2
import pickle
from datetime import datetime, date, timedelta
import os
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

attendance_buffer = []  # maintaining a time buffer to store the person_id
attendanceTimer = {'start': datetime.time(datetime.now()),
                   'end': datetime.time(datetime.now() + timedelta(hours=8))}  # attendance time constraint

credential_path = "./ServiceAccountKey.json"  # firebase credentials certificate path
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path  # setting the environment in os environment

cred = credentials.Certificate('./ServiceAccountKey.json')  # get credential
firebase_admin.initialize_app(cred)  # set credential to firebase
db = firestore.Client()

face_cascade = cv2.CascadeClassifier(
    'cascades/data/haarcascade_frontalface_alt2.xml')  # loading face recognizer from cv2
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("./recognizers/face-trainner.yml")

labels = {"person_name": 1} # dictionary to store student_id,id mapping
with open("pickles/face-labels.pickle", 'rb') as f:
    og_labels = pickle.load(f)
    labels = {v: k for k, v in og_labels.items()} # load and set the student_id id mapping from pickle file

cap = cv2.VideoCapture(0)   # using standard web-cam as input object

while (True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # convert to gray image
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)    # detect faces
    for (x, y, w, h) in faces:
        roi_gray = gray[y:y + h, x:x + w]  # region of interest y,x cordinates end point
        roi_color = frame[y:y + h, x:x + w]

        id_, conf = recognizer.predict(roi_gray)    # predict an id with confidence level
        if 100 > conf >= 70:  # if confidence level > 70 assume the person ged mached
            font = cv2.FONT_HERSHEY_SIMPLEX
            student_id = labels[id_]  # get the student/person_id
            doc_ref = db.collection(u'Register').document(date.today().strftime("%d-%m-%Y"))    # get the document reference
            # doc_ref.collection(name).document().get().to_dict() is None
            now = datetime.time(datetime.now())     # get the current date and time (@ what time person get detected)
            if attendanceTimer['start'] <= now and attendanceTimer['end'] > now:
                if student_id not in attendance_buffer:  # if person/student not all ready detected that day

                    # send the data to firebase
                    doc_ref.collection(student_id).document(u'details').set({
                        u'ID': student_id,
                        u'TIME': datetime.now()
                    })

                    attendance_buffer.append(student_id)    # add the student_id to time buffer
            else:
                attendance_buffer = []  # refresh the buffer after timeout

            color = (255, 255, 255)
            stroke = 2
            cv2.putText(frame, student_id, (x, y), font, 1, color, stroke, cv2.LINE_AA) # set student_id in the video frame

        img_item = "latest.png"
        cv2.imwrite(img_item, roi_color)    # capture and write the latest image took by the webcam

        color = (255, 0, 0)  # BGR 0-255
        stroke = 2
        end_cord_x = x + w
        end_cord_y = y + h
        cv2.rectangle(frame, (x, y), (end_cord_x, end_cord_y), color, stroke) # draw a rectangle around the face

    cv2.imshow('frame', frame)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

cap.release() # release the camera resource
cv2.destroyAllWindows()
