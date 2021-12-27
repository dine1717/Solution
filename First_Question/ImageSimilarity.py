#!/usr/bin/env python
# coding: utf-8

# In[121]:


import pandas as pd
import numpy as np
import keras
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import h5py
import cv2

from keras.layers import Flatten, Dense, Input,concatenate
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Activation, Dropout
from keras.models import Model
from keras.models import Sequential
import tensorflow as tf
from keras.applications import imagenet_utils
from keras.preprocessing import image
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tensorflow.keras.applications.vgg19 import VGG19, preprocess_input, decode_predictions

import requests

# In[128]:


vgg16 = VGG19(weights='imagenet', include_top=True, 
                                          pooling='max', input_shape=(224, 224, 3))


# In[125]:


# from keras.models import load_model
# model = load_model('vgg19_weights_tf_dim_ordering_tf_kernels.h5')


# In[129]:


model =VGG19()
#model.summary()


# In[130]:


model.get_layer('fc2').output


# In[131]:


basemodel=model(model.input, model.get_layer('fc2').output)


# In[132]:


inputs = model.input
outputs = model.get_layer('fc2').output
model_1 = model(inputs,outputs)


# In[133]:


# def get_feature_vector(img):
#     #img1 = cv2.resize(img, (224, 224))
#     img1 = cv2.resize(img,(224,224),3)
#     #feature_vector = basemodel.predict(img1.reshape(1, 224, 224, 3))
#     #img = img_to_array(img)
#     img1 = img1.reshape(1,224,224,3)
#     feature_vector = model1.predict(img1)
#     return feature_vector


# In[113]:


import scipy
from scipy.spatial import distance
def calculate_similarity(vector1, vector2):
    return (1 - scipy.spatial.distance.cosine(vector1, vector2))

def feat_img(img_path):
    img = image.load_img(img_path, target_size=(224, 224))
    img_data = image.img_to_array(img)
    img_data = np.expand_dims(img_data, axis=0)
    img_data = preprocess_input(img_data)
    vgg_feature = model.predict(img_data)
    return vgg_feature




#f1 = feat_img("bike.jpg")
#f2 = feat_img("tiger.png")



#calculate_similarity(f1, f2)

def feat_img_download(url,name):
    response = requests.get(url)
    file = open(name+".png", "wb")
    file.write(response.content)
    file.close()
    return name+".png"


