# import tensorflow as tf
# from tensorflow import keras
# import numpy as np
# import cv2
# from keras.models import load_model
# import numpy as np


# facedetect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# cap=cv2.VideoCapture(0)
# cap.set(3, 640)
# cap.set(4, 480)
# font=cv2.FONT_HERSHEY_COMPLEX


# model = load_model('keras_model.h5')


# def get_className(classNo):
# 	if classNo==0:
# 		return "Surya"
# 	elif classNo==1:
# 		return "Durga"

# while True:
# 	sucess, imgOrignal=cap.read()
# 	faces = facedetect.detectMultiScale(imgOrignal,1.3,5)
# 	for x,y,w,h in faces:
# 		crop_img=imgOrignal[y:y+h,x:x+h]
# 		img=cv2.resize(crop_img, (224,224))
# 		img=img.reshape(1, 224, 224, 3)
# 		prediction=model.predict(img)
# 		classIndex=model.predict_classes(img)
# 		probabilityValue=np.amax(prediction)
# 		if classIndex==0:
# 			cv2.rectangle(imgOrignal,(x,y),(x+w,y+h),(0,255,0),2)
# 			cv2.rectangle(imgOrignal, (x,y-40),(x+w, y), (0,255,0),-2)
# 			cv2.putText(imgOrignal, str(get_className(classIndex)),(x,y-10), font, 0.75, (255,255,255),1, cv2.LINE_AA)
# 		elif classIndex==1:
# 			cv2.rectangle(imgOrignal,(x,y),(x+w,y+h),(0,255,0),2)
# 			cv2.rectangle(imgOrignal, (x,y-40),(x+w, y), (0,255,0),-2)
# 			cv2.putText(imgOrignal, str(get_className(classIndex)),(x,y-10), font, 0.75, (255,255,255),1, cv2.LINE_AA)

# 		cv2.putText(imgOrignal,str(round(probabilityValue*100, 2))+"%" ,(180, 75), font, 0.75, (255,0,0),2, cv2.LINE_AA)
# 	cv2.imshow("Result",imgOrignal)
# 	k=cv2.waitKey(1)
# 	if k==ord('q'):
# 		break


# cap.release()
# cv2.destroyAllWindows()
#CHATGPT..
import tensorflow as tf
from tensorflow import keras
import numpy as np
import cv2
from keras.models import load_model
import numpy as np

facedetect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)
font = cv2.FONT_HERSHEY_COMPLEX

model = load_model('keras_model.h5')

def get_class_name(class_no):
    if class_no == 0:
        return "Surya"
    elif class_no == 1:
        return "Frd"

while True:
    success, img_original = cap.read()
    faces = facedetect.detectMultiScale(img_original, 1.3, 5)
    for x, y, w, h in faces:
        crop_img = img_original[y:y+h, x:x+h]
        img = cv2.resize(crop_img, (224, 224))
        img = img.reshape(1, 224, 224, 3)
        prediction = model.predict(img)
        class_index = np.argmax(prediction)
        probability_value = np.amax(prediction)
        
        cv2.rectangle(img_original, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.rectangle(img_original, (x, y-40), (x+w, y), (0, 255, 0), -2)
        cv2.putText(img_original, str(get_class_name(class_index)), (x, y-10), font, 0.75, (255, 255, 255), 1, cv2.LINE_AA)
        cv2.putText(img_original, str(round(probability_value * 100, 2)) + "%", (180, 75), font, 0.75, (255, 0, 0), 2, cv2.LINE_AA)
        
    cv2.imshow("Result", img_original)
    k = cv2.waitKey(1)
    if k == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()