from fastapi import FastAPI
from api.schema import PredictRequest
from api.model_loader import model
import numpy as np

app = FastAPI()

@app.get("/health")
def health_check():
    return {"status": "running"}

@app.post("/predict")
def predict(data: PredictRequest):
    try:
        features = [
            data.breathing_problem,
            data.fever,
            data.dry_cough,
            data.sore_throat,
            data.running_nose,
            data.fatigue,
            data.gastrointestinal,
            data.contact_with_covid_patient,
            data.visited_public_exposed_places,
            data.wearing_masks
        ]

        prediction = model.predict([features])[0]
        probability = model.predict_proba([features])[0][1]

        return {
            "prediction": "COVID Positive" if prediction == 1 else "COVID Negative",
            "confidence": round(float(probability) * 100, 2)  # Cast to float here
        }

    except Exception as e:
        return {"error": str(e)}
