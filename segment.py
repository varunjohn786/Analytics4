from feature_map import get_img_np
import glob
import os
from tensorflow import keras
import numpy as np
import cv2

file = glob.glob(os.getcwd()+ '/uploaded*')

def predict():
    cv2.imread(file[0])

    boxes_array = get_img_np(file)
    model = keras.models.load_model('/content/drive/MyDrive/dataset/embedded_dataset_2/unet_model')
    
    chargrid_input = []
    chargrid_input.append(boxes_array)
    chargrid_input_np = np.array(chargrid_input)
    
    predict = model.predict(x=chargrid_input_np)

    for x in range(512):
        for y in range(512):
            if np.argmax(predict[0][x][y]) in [1,2]:
                img = cv2.circle(img, (x,y),1,(0,0,255))

    cv2.imwrite("predicted_image.jpg", img)
