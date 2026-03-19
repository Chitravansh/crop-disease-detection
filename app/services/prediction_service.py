 
import numpy as np
from keras.models import load_model
from keras.preprocessing.image import load_img, img_to_array
# from keras.utils import load_img, img_to_array


from app.data.disease_labels import disease_labels
from config import Config


print(" ** Model Loading **")
model = load_model(Config.MODEL_PATH)
print(" ** Model Loaded **")


def model_predict(img_path):
    try:
        img = load_img(img_path, target_size=(224, 224))

        x = img_to_array(img)
        x = np.expand_dims(x, axis=0)
        x = x / 255

        preds = model.predict(x)
        d = preds.flatten()
        index = np.argmax(d)
        class_name = disease_labels[index].split("___")
        confidence = float(d[index]) * 100

        return class_name, confidence
    
    except Exception as e:
        print("Prediction Error: ", str(e))
        return ["Unknown", "Error"], 0.0
