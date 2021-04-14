#LEGACY VERSION

import cv2
import numpy as np
import pytesseract
import matplotlib.pyplot as plt
from PIL import Image
import re



from PIL import ImageGrab
import time


pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'

tessdata_dir_config = '--tessdata-dir "C:/Program Files/Tesseract-OCR/tessdata"'
#pytesseract.image_to_string(image, config=tessdata_dir_config)


## (1) Read
img = cv2.imread("D:/KTP-OCR-master/ktpocr/dataset/pancard0.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)




x, y, w, h = 0,0,100,100
cv2.rectangle(gray, (36,103), (186,163), (0, 0, 255),2)  #added by me

cropped = gray[103:163,36:186]
cv2.imshow('img',cropped)
cv2.waitKey(0)

## (2) Threshold
th, threshed = cv2.threshold(cropped, 127, 255, cv2.THRESH_TRUNC)

hImg, wImg,_ = img.shape

## (3) Detect
result = pytesseract.image_to_string((threshed), config = r'-l eng+hin --psm 6')
from langdetect import detect_langs
detect_langs(result)

#print(result)

## (5) Normalize
for word in result.split("\n"):

    if "”—" in word:
      word = word.replace("”—", ":")
  
    #normalize NIK
    if "NIK" in word:
      nik_char = word.split()
    if "D" in word:
      word = word.replace("D", "0")
    if "?" in word:
      word = word.replace("?", "7") 
  

print(result.split())
print(result[1])

date_pattern = r'([0-9]{2}\/[0-9]{2}\/[0-9]{4})'
# re.findall() method:
search_result = re.findall(date_pattern, result)
print(search_result) # Returns found object

#pattern = "[a-zA-Z0-9]+@[a-zA-Z]+\.(com,net,edu)"
#date_pattern = r'([0-9]{2}\/[0-9]{2}\/[0-9]{4}'
#for i in range:
#  date = re.search(date_pattern, date.iat[i, index_description])
#  data.iat[i,index_date] = date    drvyatautas yt regex

#cv2.imshow('img', gray)
#cv2.waitKey(500)












#print(word)

#import spacy

#nlp = spacy.load('en_core_web_sm')
#doc = nlp(result)
#from spacy import displacy

#displacy.render(nlp(doc.text),style='ent')
#print(doc)


  #C:\Program Files\Tesseract-OCR
  #C:\Program Files\Tesseract-OCR\tessdata
