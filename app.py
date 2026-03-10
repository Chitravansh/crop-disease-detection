from __future__ import division, print_function
import sys
import os
import glob
import re
import numpy as np
from flask import jsonify

# Keras
from keras.models import load_model
from keras.preprocessing import image

# Flask utils
from flask import Flask, redirect, url_for, request, render_template
from werkzeug.utils import secure_filename
from gevent.pywsgi import WSGIServer

# Define a flask app
app = Flask(__name__)

MODEL_PATH = "Model.hdf5"

# Load your trained model
print(" ** Model Loading **")
model = load_model(MODEL_PATH)
print(" ** Model Loaded **")
# model._make_predict_function()


def model_predict(img_path, model):
    img = image.load_img(img_path, target_size=(224, 224))

    # Preprocessing the image
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)

    x = x / 255

    preds = model.predict(x)
    d = preds.flatten()
    j = d.max()
    li = [
        "Apple___Apple_scab",
        "Apple___Black_rot",
        "Apple___Cedar_apple_rust",
        "Apple___healthy",
        "Blueberry___healthy",
        "Cherry_(including_sour)___Powdery_mildew",
        "Cherry_(including_sour)___healthy",
        "Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot",
        "Corn_(maize)___Common_rust_",
        "Corn_(maize)___Northern_Leaf_Blight",
        "Corn_(maize)___healthy",
        "Grape___Black_rot",
        "Grape___Esca_(Black_Measles)",
        "Grape___Leaf_blight_(Isariopsis_Leaf_Spot)",
        "Grape___healthy",
        "Orange___Haunglongbing_(Citrus_greening)",
        "Peach___Bacterial_spot",
        "Peach___healthy",
        "Pepper,_bell___Bacterial_spot",
        "Pepper,_bell___healthy",
        "Potato___Early_blight",
        "Potato___Late_blight",
        "Potato___healthy",
        "Raspberry___healthy",
        "Soybean___healthy",
        "Squash___Powdery_mildew",
        "Strawberry___Leaf_scorch",
        "Strawberry___healthy",
        "Tomato___Bacterial_spot",
        "Tomato___Early_blight",
        "Tomato___Late_blight",
        "Tomato___Leaf_Mold",
        "Tomato___Septoria_leaf_spot",
        "Tomato___Spider_mites Two-spotted_spider_mite",
        "Tomato___Target_Spot",
        "Tomato___Tomato_Yellow_Leaf_Curl_Virus",
        "Tomato___Tomato_mosaic_virus",
        "Tomato___healthy",
    ]

    index = np.argmax(d)
    class_name = li[index].split("___")
    confidence = float(d[index]) * 100

    return class_name, confidence
    # for index, item in enumerate(d):
    #     if item == j:
    #         class_name = li[index].split("___")
    # return class_name


# ----------- PAGE ROUTES -----------


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/detect")
def detect():
    return render_template("detect.html")


@app.route("/diseases")
def diseases():
    return render_template("diseases.html")


@app.route("/about")
def about():
    return render_template("about.html")


# ----------- PREDICTION ROUTE -----------


@app.route("/predict", methods=["GET", "POST"])
def upload():
    if request.method == "POST":
        # Get the file from post request
        f = request.files["file"]

        # Save the file to ./uploads
        basepath = os.path.dirname(__file__)
        file_path = os.path.join(basepath, "uploads", secure_filename(f.filename))
        f.save(file_path)

        # Make prediction
        class_name, confidence = model_predict(file_path, model)

        # result = str(
        #     f"Predicted Crop:{class_name[0]}  Predicted Disease:{class_name[1].title().replace('_',' ')}"
        # )
        result = {
            "crop": class_name[0],
            "disease": class_name[1].title().replace("_", " "),
            "confidence": round(confidence, 2)
        }
        return jsonify(result)
    return None


if __name__ == "__main__":
    app.run(debug=True)
