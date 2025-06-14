from pydantic import BaseModel

class PredictRequest(BaseModel):
    breathing_problem: int
    fever: int
    dry_cough: int
    sore_throat: int
    running_nose: int
    fatigue: int
    gastrointestinal: int
    contact_with_covid_patient: int
    visited_public_exposed_places: int
    wearing_masks: int
