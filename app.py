from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from tensorflow.keras.models import load_model
from PIL import Image
import numpy as np
import io
import os

app = FastAPI(
    title="Dogs vs Cats Image Classification API",
    description="API for predicting whether an image is a dog or a cat.",
    version="1.0"
)

MODEL_PATH = "dog_cat_model.keras"

# Load trained model
model = load_model(MODEL_PATH)

print("Dogs vs Cats model loaded successfully!")


@app.get("/")
def home():
    return {
        "message": "Dogs vs Cats Classification API is running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "model": "Dogs vs Cats CNN"
    }


@app.post("/predict")
async def predict(file: UploadFile = File(...)):

    # Check file type
    if not file.content_type.startswith("image/"):
        return JSONResponse(
            status_code=400,
            content={"error": "Please upload a valid image file."}
        )

    try:
        # Read uploaded image
        image_data = await file.read()
        image = Image.open(io.BytesIO(image_data)).convert("RGB")

        # Resize according to model input
        image = image.resize((128, 128))

        # Convert image to array
        image_array = np.array(image)

        # Normalize pixel values
        image_array = image_array.astype("float32") / 255.0

        # Add batch dimension
        image_array = np.expand_dims(image_array, axis=0)

        # Prediction
        prediction = model.predict(image_array, verbose=0)[0][0]

        # Binary classification
        if prediction >= 0.5:
            predicted_class = "dog"
            confidence = prediction * 100
        else:
            predicted_class = "cat"
            confidence = (1 - prediction) * 100

        return {
            "prediction": predicted_class,
            "confidence": round(float(confidence), 2)
        }

    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"error": str(e)}
        )