import streamlit as st
import pandas as pd
import os

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="Lead Generation Demo", layout="centered")

st.title("3D In-Vitro Models – Lead Intelligence System")

# ---------------- INPUT FIELDS ----------------
st.subheader("Lead Information")

name = st.text_input("Name")
email = st.text_input("Business Email")
company = st.text_input("Company")
title = st.text_input("Job Title")
location = st.text_input("Location (City / Country)")

st.subheader("Intent Signals")
funded = st.checkbox("Recently Funded Company")
nam_ready = st.checkbox("Uses In-Vitro / NAM Technologies")
published = st.checkbox("Published Relevant Research Recently")

# ---------------- SCORING LOGIC ----------------
def calculate_score(title, location, funded, nam_ready, published):
    score = 0

    if title:
        t = title.lower()
        if any(x in t for x in ["director", "head", "vp"]):
            score += 30
        elif any(x in t for x in ["toxicology", "safety", "preclinical", "hepatic", "3d"]):
            score += 20
        elif "scientist" in t:
            score += 10

    if funded:
        score += 20

    if nam_ready:
        score += 15

    if published:
        score += 25

    if location:
        l = location.lower()
        if any(x in l for x in ["boston", "cambridge", "bay area", "basel", "uk"]):
            score += 10

    return min(score, 100)

def score_breakdown(title, location, funded, nam_ready, published):
    reasons = []

    if title:
        t = title.lower()
        if any(x in t for x in ["director", "head", "vp"]):
            reasons.append("Senior decision-maker role (+30)")
        elif any(x in t for x in ["toxicology", "safety", "preclinical", "hepatic", "3d"]):
            reasons.append("Strong scientific role match (+20)")
        elif "scientist" in t:
            reasons.append("Relevant scientist role (+10)")

    if funded:
        reasons.append("Recently funded company (+20)")

    if nam_ready:
        reasons.append("Uses NAM / in-vitro models (+15)")

    if published:
        reasons.append("Recent relevant publications (+25)")

    if location:
        l = location.lower()
        if any(x in l for x in ["boston", "cambridge", "bay area", "basel", "uk"]):
            reasons.append("Located in biotech hub (+10)")

    return reasons

# ---------------- SUBMIT LOGIC ----------------
if st.button("Submit Lead"):
    if name.strip() and email.strip():

        score = calculate_score(title, location, funded, nam_ready, published)
        reasons = score_breakdown(title, location, funded, nam_ready, published)

        new_lead = {
            "Name": name,
            "Email": email,
            "Company": company,
            "Title": title,
            "Location": location,
            "Funded": funded,
            "NAM Ready": nam_ready,
            "Published": published,
            "Score": score
        }

        file_path = "leads.csv"
        columns = list(new_lead.keys())

        if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
            df = pd.read_csv(file_path)
        else:
            df = pd.DataFrame(columns=columns)

        df = pd.concat([df, pd.DataFrame([new_lead])], ignore_index=True)
        df.to_csv(file_path, index=False)

        st.success("✅ Lead saved successfully")

        st.subheader("Why this lead scored this way")
        if reasons:
            for r in reasons:
                st.write("•", r)
        else:
            st.write("• Basic lead information provided")

    else:
        st.error("❌ Name and Business Email are required")

# ---------------- DISPLAY LEADS ----------------
st.divider()
st.subheader("Top Ranked Leads")

file_path = "leads.csv"
if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
    df = pd.read_csv(file_path)

    search = st.text_input("Search leads (role, city, company, etc.)")

    filtered_df = df
    if search:
        filtered_df = df[df.apply(
            lambda row: search.lower() in " ".join(row.astype(str)).lower(),
            axis=1
        )]

    st.dataframe(filtered_df.sort_values("Score", ascending=False).head(10))

    st.download_button(
        label="📥 Download Leads as CSV",
        data=df.to_csv(index=False),
        file_name="ranked_leads.csv",
        mime="text/csv"
    )
else:
    st.info("No leads saved yet.")
