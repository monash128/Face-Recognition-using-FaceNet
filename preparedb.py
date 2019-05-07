import glob
from face2vec import facechop
from face2vec import pred_feature
import pickle

baseline_dict_e_r_16={}

r_list=glob.glob("images/r/*")
e_list=glob.glob("images/e/*")
 
for img_path in r_list+e_list:
    sub_faces,face_dimensions=facechop(image=img_path)
    pred_vector=pred_feature(sub_faces[0])
    baseline_dict_e_r_16[img_path]=pred_vector
        
pickle.dump(baseline_dict_e_r_16,open('baseline_dict_e_r_16','wb'))   