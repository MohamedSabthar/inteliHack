import os
import cv2
import numpy as np
from PIL import Image
import pickle

BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # get directory root
image_dir = os.path.join(BASE_DIR, "images")  # get image directory path

face_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_alt2.xml')
recognizer = cv2.face.LBPHFaceRecognizer_create()  # loading face recognizer from cv2

current_id = 0
label_ids = {}  # dictionary to map id and student id
y_labels = []   # list to store student ids
x_train = []    # list to training data points

for root, dirs, files in os.walk(image_dir):    # traverse all directories
    for file in files:                          # traversing each file in directory
        if file.endswith("png") or file.endswith("jpg"):    # selecting file having .png or .jpg extention
            path = os.path.join(root, file)                 # get the path of the image
            label = os.path.basename(root).replace(" ", "-").lower()    # spaces to hyphen and change to lowercase
            # print(label, path)
            if not label in label_ids:
                label_ids[label] = current_id   # map id and student id
                current_id += 1
            id_ = label_ids[label]
            pil_image = Image.open(path).convert("L")  # get the image with gray scale
            size = (550, 550)
            final_image = pil_image.resize(size, Image.ANTIALIAS)
            image_array = np.array(final_image, "uint8")    # convert the image to array
            # print(image_array)
            faces = face_cascade.detectMultiScale(image_array, scaleFactor=1.5, minNeighbors=5) # find faces

            for (x, y, w, h) in faces:
                roi = image_array[y:y + h, x:x + w] # get the region of interest
                x_train.append(roi)     # append training data points
                y_labels.append(id_)    # append lables

# print(y_labels)
# print(x_train)

with open("pickles/face-labels.pickle", 'wb') as f:
    pickle.dump(label_ids, f)   # creating pickle dump of lable_ids dictionary

recognizer.train(x_train, np.array(y_labels))    # train dataset
recognizer.save("recognizers/face-trainner.yml")    # save trained dataset

