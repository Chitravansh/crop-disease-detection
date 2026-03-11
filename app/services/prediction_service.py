import numpy as np
from keras.models import load_model
from keras.preprocessing import image

from app.data.disease_labels import disease_labels
from config import Config


print(" ** Model Loading **")
model = load_model(Config.MODEL_PATH)
print(" ** Model Loaded **")


def model_predict(img_path):

    img = image.load_img(img_path, target_size=(224, 224))

    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = x / 255

    preds = model.predict(x)
    d = preds.flatten()
    index = np.argmax(d)
    class_name = disease_labels[index].split("___")
    confidence = float(d[index]) * 100

    return class_name, confidence
