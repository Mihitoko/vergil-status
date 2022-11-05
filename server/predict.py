"""
MIT License

Copyright (c) 2020 The nsfw_model Developers

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
documentation files (the "Software"), to deal in the Software without restriction, including without limitation the
rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software,
and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the
Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE
WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

This file is a slightly modified and
stripped down version of (https://github.com/GantMan/nsfw_model/blob/master/nsfw_detector/predict.py)
"""

from os.path import exists

import numpy as np
import tensorflow as tf
import tensorflow_hub as hub
from tensorflow import keras

IMAGE_DIM = 224  # required/default image dimensionality


def load_images(image_list, image_size):
    keras_images = []
    try:
        for image_binary in image_list:
            image = keras.preprocessing.image.load_img(image_binary, target_size=image_size)
            image = keras.preprocessing.image.img_to_array(image)
            image /= 255
            keras_images.append(image)
    except Exception:
        print("Image Load Failure")

    return np.asarray(keras_images)


def load_model(model_path):
    if model_path is None or not exists(model_path):
        raise ValueError("saved_model_path must be the valid directory of a saved model to load.")

    model = tf.keras.models.load_model(model_path, custom_objects={'KerasLayer': hub.KerasLayer}, compile=False)
    return model


def classify(model, input_paths, image_dim=IMAGE_DIM):
    """ Classify given a model, input paths (could be single string), and image dimensionality...."""
    images = load_images(input_paths, (image_dim, image_dim))
    probs = classify_nd(model, images)
    return probs


def classify_nd(model, nd_images):
    """ Classify given a model, image array (numpy)...."""

    model_preds = model.predict(nd_images)

    categories = ['drawings', 'hentai', 'neutral', 'porn', 'sexy']

    probs = []
    for i, single_preds in enumerate(model_preds):
        single_probs = {}
        for j, pred in enumerate(single_preds):
            single_probs[categories[j]] = float(pred)
        probs.append(single_probs)
    return probs
