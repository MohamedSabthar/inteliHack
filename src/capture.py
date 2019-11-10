import cv2
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # get directory root
image_dir = os.path.join(BASE_DIR, "images")  # get image directory path
# print(image_dir)
person_id = input("Enter the Id: ")  # receive the id input
image_dir_id = os.path.join(image_dir, person_id)  # create a path specific to the id

try:
    os.mkdir(image_dir_id)  # create a directory in the name of id
except FileExistsError:
    print('Directory already exist')

# print(image_dir_id)

cam = cv2.VideoCapture(0)  # using standard web-cam as input object
detector = cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_alt2.xml')  # set haarcascade frontalface model

sampleNum = 0
while (True):
    ret, img = cam.read()       # read image
    # print(ret)                # checking for camera read the image properly
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = detector.detectMultiScale(gray, 1.5, 5)
    for (x, y, w, h) in faces:
        sampleNum = sampleNum + 1   # incrementing sample number
        # print(os.path.join(image_dir_id,str(sampleNum))+ ".jpg")
        cv2.imwrite(os.path.join(image_dir_id, str(sampleNum)) + ".jpg", img=img)   # saving images to indexed directory
        cv2.imshow('frame', img)      # display the frame
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)    # setting the rectangle for ROI

    if cv2.waitKey(25) & 0xFF == ord('q'):  # delay 25 millisecond break if key 'q' pressed
        break
    elif sampleNum > 200:   # finish execution after 100 sample pictures
        break

cam.release()       # release the camera resource
cv2.destroyAllWindows()
