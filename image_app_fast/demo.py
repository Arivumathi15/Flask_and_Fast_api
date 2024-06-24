from transformers import AutoFeatureExtractor, ViTForImageClassification
from PIL import Image
import io
import requests
import torch
from flask import Request



# Define the model and feature extractor (place outside any function)
model_name = "facebook/deit-tiny-patch16-224"
feature_extractor = AutoFeatureExtractor.from_pretrained(model_name)
model = ViTForImageClassification.from_pretrained(model_name)


async def predict(info: Request):
    # Check if an image file is present in the request
    #if 'image' not in request.files:
        #return jsonify({'error': 'No image file found in request'}), 400
    #response = Request.get_json()
    response = await info.json()
    print(response)

    image = Image.open(requests.get(response["url"], stream=True).raw)

    # Preprocess the image
    inputs = feature_extractor(images=image, return_tensors="pt")

    # Make prediction
    # with torch.no_grad():  # Disable gradient calculation for efficiency
    outputs = model(**inputs)
    logits = outputs.logits
    predicted_class_idx = logits.argmax(-1).item()
    result = {'result': model.config.id2label[predicted_class_idx], 'message': 'Success'}

    return result





