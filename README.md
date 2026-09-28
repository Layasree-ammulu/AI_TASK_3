# Task 3 - Model Deployment Using FastAPI and Docker

## Project Overview

This project deploys a trained **Dogs vs Cats CNN model** as a REST API using **FastAPI**.

The API accepts an image as input and predicts whether the image contains a **dog or a cat**, along with the confidence score.

The FastAPI application is containerized using **Docker** to provide a consistent and portable deployment environment.

## Objective

* Deploy a trained Dogs vs Cats CNN model as an API.
* Create an endpoint for model inference.
* Accept an image as input.
* Preprocess the input image before prediction.
* Return the predicted class and confidence score.
* Containerize the API using Docker.
* Test the API using Swagger UI.

## Technologies Used

* Python
* TensorFlow / Keras
* FastAPI
* Uvicorn
* NumPy
* Pillow
* Docker

## Model

The project uses a trained Dogs vs Cats CNN model:

```text
dog_cat_model.keras
```

The model accepts RGB images of size:

```text
128 × 128 × 3
```

### Image Preprocessing

Before prediction, the uploaded image is:

1. Converted to RGB format.
2. Resized to `128 × 128` pixels.
3. Converted into a NumPy array.
4. Normalized by dividing pixel values by `255`.
5. Converted into a batch for model prediction.

## Project Structure

```text
task 3
│
├── app.py
├── dog_cat_model.keras
├── requirements.txt
├── Dockerfile
├── README.md
├── report.pdf
└── outout.txt
```

## FastAPI Application

The API is implemented using FastAPI in:

```text
app.py
```

The application loads the trained model:

```text
dog_cat_model.keras
```

and provides endpoints for checking the API status and performing model inference.

## API Endpoints

### 1. Home Endpoint

**GET /**

This endpoint checks whether the API is running.

Example response:

```json
{
  "message": "Dogs vs Cats Classification API is running"
}
```

### 2. Health Check Endpoint

**GET /health**

This endpoint checks the health status of the API and model.

Example response:

```json
{
  "status": "healthy",
  "model": "Dogs vs Cats CNN"
}
```

### 3. Model Inference Endpoint

**POST /predict**

This endpoint accepts an image file and predicts whether the image contains a dog or a cat.

Example response:

```json
{
  "prediction": "dog",
  "confidence": 66.11
}
```

## Running the API Locally

### Install Required Packages

Install the required libraries using:

```bash
pip install -r requirements.txt
```

### Run the FastAPI Application

Run:

```bash
uvicorn app:app --reload
```

The API will run at:

```text
http://127.0.0.1:8000
```

## Swagger Documentation

FastAPI provides interactive API documentation using Swagger UI.

Open:

```text
http://127.0.0.1:8000/docs
```

The Swagger interface displays all available API endpoints.

The `/predict` endpoint can be tested by uploading an image.

## Docker

Docker is used to containerize the FastAPI application along with the trained model and required dependencies.

The Docker configuration is provided in:

```text
Dockerfile
```

### Building the Docker Image

Open Command Prompt in the project folder:

```cmd
cd "C:\study\InternShips\AI\task 3"
```

Build the Docker image using:

```cmd
docker build -t dogs-cats-api .
```

The Docker image is created as:

```text
dogs-cats-api:latest
```

### Checking the Docker Image

Run:

```cmd
docker images
```

The created image will appear as:

```text
dogs-cats-api:latest
```

### Running the Docker Container

Run the Docker container using:

```cmd
docker run -d -p 8000:8000 --name dogs-cats-container dogs-cats-api
```

The API will be available at:

```text
http://127.0.0.1:8000
```

### Checking the Running Container

Run:

```cmd
docker ps
```

The running container will appear as:

```text
dogs-cats-container
```

## Example Request and Response

### Request

The model inference endpoint is:

```text
POST /predict
```

The endpoint accepts an image file.

For example:

```text
train_test.jpg
```

The image can be uploaded using the Swagger UI at:

```text
http://127.0.0.1:8000/docs
```

### Response

Example API response:

```json
{
  "prediction": "dog",
  "confidence": 66.11
}
```

HTTP response:

```text
200 OK
```

## Testing

The API was tested using Swagger UI with an input image.

**Test image:**

```text
train_test.jpg
```

### Sample Result

```text
Prediction : dog
Confidence : 66.11%
HTTP Status : 200 OK
```

The API successfully processed the image and returned the prediction.

## Result

The trained Dogs vs Cats CNN model was successfully deployed as a REST API using FastAPI.

The API successfully accepted an image, performed preprocessing, generated a prediction, and returned the predicted class with the confidence score.

The FastAPI application was also successfully containerized using Docker and tested inside a Docker container.

## Conclusion

This project demonstrates the deployment of a trained deep learning model using **FastAPI and Docker**.

The API provides a simple model inference endpoint that accepts an image and returns the predicted class and confidence score.

Docker packages the application, trained model, and required dependencies into a container, making the deployment environment consistent and portable.
