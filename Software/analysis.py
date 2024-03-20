import os
import numpy as np
import lightgbm as lgb
import torch
from features import PEFeatureExtractor
from sklearn.preprocessing import MinMaxScaler
import joblib
from PIL import Image

def create_image(features):
    # Reshape the extended array to have three elements per pixel for RGB channels
    features_extended = features[:2380]
    features_extended0 = np.append(features_extended, features[:2380])
    features_extended1 = np.append(features_extended0, features[:2380])

    # Reshape the array into pixel RGB values
    image_data = features_extended1.reshape(-1, 3)

    # Scale the image data to the range [0, 255] for RGB values
    image_data_scaled = (image_data - np.min(image_data)) / (np.max(image_data) - np.min(image_data)) * 255

    # Convert to uint8 data type
    image_data_scaled = image_data_scaled.astype(np.uint8)

    # Reshape the image data to the adjusted dimensions (height, width, channels)
    height = 20
    width = 119  
    image_data_reshaped = image_data_scaled.reshape((height, width, 3))

    # Create an image object from the array
    image_object = Image.fromarray(image_data_reshaped)

    # Resize the image to fit the GUI
    image = image_object.resize((476, 80)) 
    return image
 
 
# Function to perform MinMax scaling on features
def scale_features(features):
    scaler = MinMaxScaler()
    scaled_features = scaler.fit_transform(features)
    return scaled_features  

def analyze_file(file_path, model, progress_callback=None):
    # Placeholder for actual analysis and feature extraction
    # Here you would implement the logic to extract features from the file using the loaded model
    # For demonstration purposes, let's just load the image and make a prediction
    # Read the contents of the file
    with open(file_path, "rb") as f:
        bytez = f.read()
    extractor = PEFeatureExtractor(feature_version=2)
    features = np.array(extractor.feature_vector(bytez), dtype=np.float32)
    file_data = features.reshape(1, -1)
    # Scale features if needed
    if model != "best_CNN_ES":
        scaled_features = scale_features(file_data)
    else:
        scaled_features = file_data
    # Simulate analysis progress
    for i in range(101):
        if progress_callback:
            progress_callback(i)
    prediction = model.predict(scaled_features)
    result = "Analysis result: Malicious" if prediction > 0.5 else "Analysis result: Benign"
    return result, features

# Function to load a model from the specified model name
def load_model(model_name):
    model_extensions = ['.joblib', '.pth', '.bin'] 
    models_directory = "models"
    
    for ext in model_extensions:
        model_path = os.path.join(models_directory, model_name + ext)
        if os.path.exists(model_path):
            if ext == '.joblib':
                return joblib.load(model_path)
            elif ext == '.pth':
                return torch.load(model_path)
            elif ext == '.bin':
                return lgb.Booster(model_file=model_path)

    print("Model not found:", model_name)
    return None


