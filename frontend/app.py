import streamlit as st
import requests


with open("frontend/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.markdown('<div class="full-header">COVID-19 Prediction App</div>', unsafe_allow_html=True)



def yes_no_input(label):
    return 1 if st.selectbox(label, ["No", "Yes"]) == "Yes" else 0

breathing_problem = yes_no_input("Breathing Problem")
fever = yes_no_input("Fever")
dry_cough = yes_no_input("Dry Cough")
sore_throat = yes_no_input("Sore Throat")
running_nose = yes_no_input("Running Nose")
fatigue = yes_no_input("Fatigue")
gastrointestinal = yes_no_input("Gastrointestinal Issue")
contact = yes_no_input("Contact with COVID Patient")
visited = yes_no_input("Visited Public Exposed Places")
masks = yes_no_input("Wearing Masks")

if st.button("Predict"):
    input_data = {
        "breathing_problem": breathing_problem,
        "fever": fever,
        "dry_cough": dry_cough,
        "sore_throat": sore_throat,
        "running_nose": running_nose,
        "fatigue": fatigue,
        "gastrointestinal": gastrointestinal,
        "contact_with_covid_patient": contact,
        "visited_public_exposed_places": visited,
        "wearing_masks": masks
    }

    res = requests.post("http://localhost:8000/predict", json=input_data)

    if res.status_code == 200:
        result = res.json()
        if "prediction" in result:
            popup_class = "result-danger" if result["prediction"] == "COVID Positive" else "result-success"
            st.markdown(
                f'<div class="result-popup {popup_class}">'
                f'Prediction: {result["prediction"]}</div>',
                unsafe_allow_html=True
            )
        else:
            st.error(f"Error: {result.get('error', 'Unknown error')}")
    else:
        st.error("Failed to get prediction from server.")

# <br>Confidence: {result["confidence"]}%