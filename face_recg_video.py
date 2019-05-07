# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 15:55:14 2019

@author: Monashree.Sanil
"""
import cv2
import pickle
#from mtcnn_face_chop import facechop
from haar_cascade_face_chop import facechop
from bounding_box import draw_box
from face2vec import pred_feature,dist

# Loads dictionary containing the tags and corresponding facevectors of training images.
baseline_dict = pickle.load(open('baseline_dict_e_r_16', 'rb'))

# calculate euclidean distance with every target image and return the one having minimum distance
def pred_face(target_faces):
    # target_faces = facechop(img_array=target_frame)
    for target_face in target_faces:
        target_pred_vect = pred_feature(target_face)
        minn = 999 
        for im in baseline_dict.keys(): 
            im_dist = dist(target_pred_vect, baseline_dict[im]) 
            if im_dist < minn: 
                minn = im_dist
                path = im 
        print(path)


cap = cv2.VideoCapture('ellen.mp4')
try:
    while(True):
        # Capture frame-by-frame
        ret, frame = cap.read()
        frame = cv2.resize(frame, (400, 150))
        # pred_face(frame)
        # get faces and their dimensions 
        sub_faces,face_dims = facechop(img_array=frame)
        #render bounding box
        frame_with_boxes=draw_box(frame,face_dims)
        # predict face
        pred_face(sub_faces)
        cv2.imshow('frame',frame_with_boxes)
        if cv2.waitKey(50) & 0xFF == ord('q'):
            break
except KeyboardInterrupt:
    pass
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()