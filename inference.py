import tensorflow as tf
import numpy as np
from PIL import Image
import json


MODEL_DIR = 'models/' + '4_class_20_ep.h5'
LABElS_DICT = 'models/' + 'labels_dict.json'

"""Load Model and labels dict"""
loaded_model = tf.keras.models.load_model(MODEL_DIR)
with open(LABElS_DICT) as f :
    labels_dict = json.load(f)

"""Inference functions"""
# predict from image array
def predict_from_image_array(img_array: np.array) -> str: # Image must be of shape : (150, 150, 1)
    img_array = np.array([img_array]) / 255.
    out = loaded_model.predict(img_array, verbose=0)
    prediction, proba = np.argmax(out), round(np.max(out), 2)
    prediction = labels_dict[str(prediction)]
    return prediction, proba

# predict from file path, directly leverage keras utils
def predict_from_image_path(img_path: str) -> str:
    img = tf.keras.utils.load_img(
        img_path,
        color_mode="grayscale",
        target_size=(150, 150),)
    img_array = tf.keras.utils.img_to_array(img)
    prediction, proba = predict_from_image_array(img_array)
    return prediction, proba

# predict from bytes/ explicit but faster (avoids writing/reading from file first)
def predict_from_image_bytes(img_bytes: str) -> str: #TODO : DO NOT USE : GIVE DIFFERENT RESULTS
    from io import BytesIO
    img = Image.open(BytesIO(img_bytes)).convert('L')
    img = img.resize((150, 150))
    
    img_array = np.array(img)
    img_array = np.expand_dims(img_array, axis=-1)
    img_array = np.array(img_array) / 255.
    prediction, proba = predict_from_image_array(img_array)
    return prediction, proba