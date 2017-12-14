import matplotlib.pyplot as plt
import numpy as np
import cv2


# Load the classifier model
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

def capture():
    ''' Capturing a single frame from a webcam and return it'''
    cap = cv2.VideoCapture(0)
    time.sleep(0.5)

    ret, frame = cap.read()
    #cap.release()
    return frame

def display(frame):
    ''' function plots a single frame with detected face'''

    plt.imshow(cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)) #converting frame from RGB to BGR
    plt.title('Captured frame')
    plt.show()

def detect(frame, minsize):
    '''
    INPUT:
    frame ---- an array of an image to process for face detection.
    minsize -- a threshold value in pixels of minimum size of a detectable face.

    OUTPUT:
    returns position and size of a detected face.
    '''

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #converting into Gray-scale for faster processing.
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(minsize, minsize))
    return faces

def draw_rec(frame, detected_faces):
    for (x,y,w,h) in detected_faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
    return frame

img_source = 'background.jpg'
background = cv2.imread(img_source)

while(True):

    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    output = background
    faces = detect(frame, 250)
    if len(faces) > 0:
        output = draw_rec(frame, faces)

    cv2.namedWindow('frame', cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty('frame', cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
    cv2.imshow('frame', output)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    elif cv2.waitKey(1) & 0xFF == ord('p'):
        display(frame)
        print('frame is printed')

cv2.destroyAllWindows()
