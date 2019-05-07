# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 14:44:37 2019

@author: Monashree.Sanil
@description: renders bounding box on each frame
"""
import cv2

def draw_box(frame,box_dims):
    for box in box_dims:
        # get co-ordinates of bounding box of face
            x, y, w, h = box
        #render rectangle around detected face in frame    
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0,0,255), 2)
        
    return frame