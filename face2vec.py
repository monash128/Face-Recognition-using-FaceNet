# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 16:09:31 2019

@author: Monashree.Sanil
"""

import numpy as np
from keras.models import load_model

#calculate euclidean distance
def dist(pred1, pred2): 
    return np.sqrt(np.sum(np.square(pred1-pred2)))

# get vector for detected face
def pred_feature(img):  
    img = img/255. 
    img_reshaped = np.rollaxis(img, 2, 0) 
    # plt.imshow(img_reshaped[0,:,:])
    return model.predict([[img_reshaped]]) 

model = load_model('face-rec_Google.h5')