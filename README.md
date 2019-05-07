# Face-Recognition-using-FaceNet
## Facial Recognition  

This code helps in facial recognition using facenets (https://arxiv.org/pdf/1503.03832.pdf). The main concepts talked about triplet loss function to compare images of different person. I have used haar cascade for detecting face from videos. It is faster but MTCNN has better accuracy. MTCNN requires resources to run efficiently.

## Description
A facial recognition system is a technology capable of identifying or verifying a person from a digital image or a video frame from a video source. There are multiples methods in which facial recognition systems work, but in general, they work by comparing selected facial features from given image with faces within a database.

**Python Implementation**

**Network Used** - Inception Network

**Original Paper** - Facenet by Google

## Procedure
1. I have used a trained model face-rec_Google.h5 file which gets loaded at runtime.You need to have images in your database. The code check /images folder for that. You can either paste your pictures there or you can click it using web cam. 
2. Run preparedb.py for preparing database with tags and respective image vectors.
3. Run face_recg_video.py to run the application.

## References:
- Florian Schroff, Dmitry Kalenichenko, James Philbin (2015). FaceNet: A Unified Embedding for Face Recognition and Clustering
Yaniv Taigman, Ming Yang, Marc'Aurelio Ranzato, Lior Wolf (2014). DeepFace: Closing the gap to human-level performance in face verification
- The pretrained model used is inspired by Victor Sy Wang's implementation and was loaded using his code: https://github.com/iwantooxxoox/Keras-OpenFace.
- implementation also took a lot of inspiration from the official FaceNet github repository: https://github.com/davidsandberg/facenet
