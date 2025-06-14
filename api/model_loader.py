import joblib
import os

# Construct the model path
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
model_path = os.path.join(BASE_DIR, 'models', 'best_model.pkl')

# Load the model
model = joblib.load(model_path)
