# Lead Probability Engine – Demo
A Streamlit-based lead generation and probability scoring system for biotech and life sciences.
This app helps business developers identify, enrich, and rank high-probability leads for 3D in-vitro model solutions.

## 📊 Live Demo Output
**Streamlit App:** [Click to Open](https://t4nya13-lead-probability-engine-demo-app-gpaidw.streamlit.app/)
**Google Sheet Output:** [Example Sheet](https://docs.google.com/spreadsheets/d/1qe0V-DC1QxRNZnUlBxwFX9AtZiKbU0-S_z7pXYWzgy0/edit?usp=sharing)

🏛️ High-Level Architecture
1. Identification (Input)
  a. Crawls target profiles from LinkedIn, PubMed, and conference attendee lists.
  b. Focus on relevant roles: Director of Toxicology, Head of Preclinical Safety, VP Safety, etc.
2. Enrichment (Data Gathering)
  a. Collects business email, company HQ location, and work location.
  b. Distinguishes between remote/home vs. office location.
3.Ranking (Probability Engine)
  a. Applies a propensity score (0–100) based on weighted signals:
     Role Fit: Toxicology, Safety, Preclinical (+30)
     Company Intent: Funding or tech adoption (+20)
     Technographic Fit: Company uses similar tech (+15)
     Scientific Intent: Recent publications (+40)
     Location Hub: Boston, Cambridge, Bay Area, Basel, UK Golden Triangle (+10)
  b. Generates a dynamic, searchable lead dashboard.

🧠 Key Design Decisions

  **Efficiency & Cost**
  Avoids redundant calculations by checking existing CSV entries.
  
 ** Reliability**
  Score calculation follows well-defined criteria to ensure consistency.
  
  **Compliance & Signal Quality**
  Uses only legal, public sources—no LinkedIn scraping.
  
  **Accuracy**
  Distinguishes Person Location vs. Company HQ and detects work mode (Onsite / Remote /     Hybrid).
  
  **Data Integrity**
  Deduplication based on Name, Email, and Company maintains a clean dataset.

🛠️ Tech Stack
    Python 3.12
    Streamlit for UI
    Pandas for data processing
    CSV / Google Sheets for storage and sharing

    
 🔧 Local Setup
 
    1. Clone the repo:
      git clone https://github.com/YOUR_USERNAME/lead-probability-engine.git
      cd lead-probability-engine

    2.  Create a virtual environment:
        python -m venv venv

    3. Activate the environment:
      Windows: venv\Scripts\activate
      Mac/Linux: source venv/bin/activate

    4. Install dependencies:
        pip install -r requirements.txt

    5. Run the Streamlit app:
       streamlit run app.py
 
    
📡 Deployment
  1. Hosted on Streamlit Cloud: Live demo link shared above.
  2. CSV/Google Sheet export ensures reproducible and verifiable output.

     


