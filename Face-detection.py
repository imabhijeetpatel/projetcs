# This is the face detection system which use open cv pretarined model for face detection

# requirement for this
# > pip install opencv-python

import cv2

# Load Haar casecade Classifier
face_casecade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontaface_default.xml')

def detect_face_image(image_path):
    image =cv2.imread(image_path)
    gray =cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces =face_casecade.detectMultiScale(gray, scaleFactor =1.1, minNeighbors =5, minSize=(30,30))
    for (a,b,c,d) in faces:
     cv2.rectangle(image, (a,b), (a+b, b+d ), (0,255, 0), 2)
    cv2.imshow("Face Detection", image)
    cv2.waitKey(0)
    cv2.destroyAllwindows()
    
def detect_faces_from_webcam():
    cap =cv2.VideoCapture(0)

    while True:
        ret,frame = cap.read()
        gray =cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces= face_casecade.detectMultiScale(gray, scaleFactor =1.1, minNeighbor =5, minSize(30,30))

        for (a,b,c,d) in faces:
         cv2.rectangle(image, (a,b), (a+b, b+d ), (0,255, 0), 2)

        cv2.imshow("Face Detection", frame)
        if cv2.waitKey(6) & 0xFF == ord("q"):
            break
    cap.release()
    cv2.destroyAllwindows()

# RUN THE FACE DETECTION APP
print("choice an option:\n1 Detect face from image\n2 Detect face from webcam\n3")

choice = input("enter >> 'image' or >> 'webcam'")
if choice == "image":
   image_path = input("Enter the image path")
   detect_face_image(image_path)
elif choice =="webcam":
   detect_faces_from_webcam()
else:
   print("Invalid Choice try right")


    ########### here the single implementation of each ###############



# image =cv2.imread("face.jpg")
# gray =cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# # HERE DETECTS FACE 
# faces =face_casecade.detectMultiScale(gray, scaleFactor =1.1, minNeighbors =5, minSize=(30,30))

# # here we drow the rectangles around the image
# for (a,b,c,d) in faces:
#     cv2.rectangle(image, (a,b), (a+b, b+d ), (0,255, 0), 2)

# #here shoe the image
# cv2.imshow("Face Detection", image)
# cv2.waitKey(0)
# cv2.destroyAllwindows()

# # In this initialize the web camera of the system

# cap =cv2.VideoCapture(0)

# while True:
#     ret, frame = cap.read()
#     gray =cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

#     # detects the faces
#     faces= face_casecade.detectMultiScale(gray, scaleFactor =1.1, minNeighbor =5, minSize|(30,30))
    
#     # here we drow the rectangles around the image
#     for (a,b,c,d) in faces:
#         cv2.rectangle(image, (a,b), (a+b, b+d ), (0,255, 0), 2)

#     #here shoe the image
#     cv2.imshow("Face Detection", frame)

#     # press 'q'  to quit
#     if cv2.waitKey(6) & 0xFF == ord("q"):
#         break

# # here we release resources
# cap.release()
# cv2.destroyAllwindows()
