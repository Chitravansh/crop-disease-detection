import os
from flask import Blueprint, request, jsonify
from werkzeug.utils import secure_filename

from config import Config
from app.services.prediction_service import model_predict


prediction = Blueprint("prediction", __name__)


@prediction.route("/predict", methods=["POST"])
def predict():

    f = request.files["file"]
    basepath = os.path.dirname(__file__)
    project_root = os.path.abspath(os.path.join(basepath, "../../"))
    file_path = os.path.join(
        project_root,
        Config.UPLOAD_FOLDER,
        secure_filename(f.filename),
    )
    f.save(file_path)

    class_name, confidence = model_predict(file_path)

    result = {
        "crop": class_name[0],
        "disease": class_name[1].title().replace("_", " "),
        "confidence": round(confidence, 2),
    }

    return jsonify(result)
