# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 13:43:12 2019

@author: Monashree.Sanil
@description: detect faces from frame using MTCNN and return face pixel array and face dimensions
"""

import cv2
from mtcnn.mtcnn import MTCNN

def facechop(image=None, img_array=None) :
    if image:
        img=cv2.imread(image)
    else:
        img=img_array
    detector=MTCNN()
    face_attrs=detector.detect_faces(img) 
    face_dims=[]
    sub_faces=[]
    for face in face_attrs:
        x,y,w,h=face['box']
        sub_face=img[y:y+h,x:x+w]
        face_dims.append([x,y,w,h])
        sub_faces.append(cv2.resize(sub_face, (96, 96)))

    return (sub_faces,face_dims)   
        
        
    