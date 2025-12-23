from flask import Flask, render_template, request
import os
import tensorflow as tf

from utils.preprocess import preprocess_image
from utils.inference import run_inference
from utils.suggestions import generate_suggestions

app = Flask(__name__)

UPLOAD_FOLDER = "static/uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Load model ONCE (important)
model = tf.keras.models.load_model("model/uiux_model.keras")

@app.route("/", methods=["GET", "POST"])
def index():
    result = None

    if request.method == "POST":
        file = request.files["image"]
        if file:
            image_path = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(image_path)

            img_tensor = preprocess_image(image_path)
            score, flags = run_inference(model, img_tensor)
            suggestions = generate_suggestions(flags)

            result = {
                "score": round(score, 2),
                "flags": flags,
                "suggestions": suggestions,
                "image": image_path
            }

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
