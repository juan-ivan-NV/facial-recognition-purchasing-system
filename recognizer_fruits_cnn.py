import os
import cv2
import json
import numpy as np
from keras.models import model_from_json, load_model

with open('models_testings/model_architecture_15_fruits.json', 'r') as f:
    model = model_from_json(f.read())
model.load_weights('models_testings/model_weights_15_fruits.h5')

path = 'fruit'
fruits = []

for filename in os.listdir(path):
    if 'jpg' in filename:

        photo2 = cv2.imread(os.path.join(path,filename))
        img = cv2.resize(photo2,(100,100))
        image = np.expand_dims(img, axis=0)

        predict = model.predict(image)

        output = { 0:'apple',1:'avocado',2:'banana',3:'blueberry',4:'lemon',5:'onion red',6:'orange',7:'pepper green',8:'potato',9:'tomato',10:'strawberry',11:'raspberry',12:'pineapple',13:'pear',14:'coco'}
        #output = { 0:'apple',1:'avocado',2:'banana',3:'blueberry',4:'lemon',5:'onion red',6:'orange',7:'pepper green',8:'potato',9:'tomato'}

        print(predict)
        fruits.append(output[np.argmax(predict)])

print(fruits)