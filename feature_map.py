import cv2
import pytesseract
from pytesseract import Output
import numpy as np
import wikipedia2vec

with open("enwiki_20180420_win10_100d.pkl.bz2","rb+") as file:
  embedding = wikipedia2vec.Wikipedia2Vec.load(file)

def get_img_np(file):
    img = cv2.imread(file[0])
    height, width = img.shape[0], img.shape[1]
    boxes = pytesseract.image_to_data(img, output_type=Output.DATAFRAME)
    boxes = boxes[boxes['conf']>0]
    boxes['left'] = (boxes['left']/width)*512
    boxes['width'] = (boxes['width']/width)*512
    boxes['top'] = (boxes['top']/height)*512
    boxes['height'] = (boxes['height']/height)*512

    boxes['top'] = boxes['top'].astype('int')
    boxes['left'] = boxes['left'].astype('int')
    boxes['width'] = boxes['width'].astype('int')
    boxes['height'] = boxes['height'].astype('int')

    boxes_array = np.zeros([512,512,100])

    for index,row in boxes.iterrows():
              try:
                word = row.text.lower()
                word2 = ''.join(e for e in word if e.isalnum())
                boxes_array[row.left:(row.left+row.width),row.top:(row.top+row.height)] = embedding.get_word_vector(word2) 
              except:
                pass
    return boxes_array
