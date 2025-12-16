import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Lead Probability Engine", layout="wide")

st.title("🔬 3D In-Vitro Models – Lead Probability Engine (Demo)")

# -----------------------------
# Input Form
# -----------------------------
st.subheader("Add New Lead")

name = st.text_input("Name")
title = st.text_input("Job Title")
company = st.text_input("Company")
person_location = st.text_input("Person Location (e.g., Remote – Texas)")
hq_location = st.text_input("Company HQ (e.g., Cambridge, MA)")
email = st.text_input("Business Email")
linkedin = st.text_input("LinkedIn Profile URL")

# -----------------------------
# Scoring Logic
# -----------------------------
def calculate_probability(title, person_location):
    score = 0

    role_keywords = ["toxicology", "safety", "preclinical", "investigative", "pharmacology"]
    hub_locations = ["boston", "cambridge", "bay area", "basel", "uk"]

    if any(word in title.lower() for word in role_keywords):
        score += 30

    if any(city in person_location.lower() for city in hub_locations):
        score += 10

    return min(score, 100)

def assign_action(score):
    if score >= 80:
        return "High Priority – Call"
    elif score >= 50:
        return "Email Follow-up"
    else:
        return "Low Priority"

# -----------------------------
# CSV Handling
# -----------------------------
file_path = "leads.csv"

columns = [
    "Rank",
    "Probability",
    "Name",
    "Title",
    "Company",
    "Location",
    "HQ",
    "Email",
    "LinkedIn",
    "Action"
]

if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
    df = pd.read_csv(file_path)
else:
    df = pd.DataFrame(columns=columns)

# -----------------------------
# Submit Button
# -----------------------------
if st.button("Submit Lead"):
    if name and email:
        probability = calculate_probability(title, person_location)
        action = assign_action(probability)

        new_row = {
            "Rank": 0,  # temporary
            "Probability": probability,
            "Name": name,
            "Title": title,
            "Company": company,
            "Location": person_location,
            "HQ": hq_location,
            "Email": email,
            "LinkedIn": linkedin if linkedin else "https://linkedin.com",
            "Action": action
        }

        df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)

        # Sort by probability and assign rank
        df = df.sort_values(by="Probability", ascending=False).reset_index(drop=True)
        df["Rank"] = df.index + 1

        df.to_csv(file_path, index=False)

        st.success("Lead saved and ranked successfully!")
    else:
        st.error("Name and Business Email are required.")

# -----------------------------
# Display Dashboard
# -----------------------------
st.subheader("📊 Lead Generation Dashboard")

st.dataframe(df, use_container_width=True)

st.download_button(
    label="⬇ Download CSV",
    data=df.to_csv(index=False),
    file_name="lead_probability_output.csv",
    mime="text/csv"
)
