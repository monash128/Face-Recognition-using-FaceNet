# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 14:30:17 2019

@author: Monashree.Sanil
@description: detect faces from frame using haar cascade and return face pixel array and face dimensions
"""

import cv2

def facechop(image=None, img_array=None):  
    if image:
        img = cv2.imread(image)
    else:
        img = img_array
    img1 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    face_dims = cascade.detectMultiScale(img1)
    sub_faces = []
    for f in face_dims:
        x, y, w, h = [ v for v in f ]
        sub_face = img[y:y+h, x:x+w]
        # cv2.imshow(image, sub_face)
        sub_faces.append(cv2.resize(sub_face, (96, 96)))
    return  (sub_faces, face_dims)

facedata = "haarcascade_frontalface_alt2.xml"
cascade = cv2.CascadeClassifier(facedata)