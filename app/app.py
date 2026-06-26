
import streamlit as st
import pandas as pd
from pathlib import Path

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(
    page_title="AI Resume Screening System",
    page_icon="📄",
    layout="wide"
)

# -----------------------------
# Get Project Root
# -----------------------------
BASE_DIR = Path(__file__).resolve().parent.parent

CSV_PATH = BASE_DIR / "outputs" / "ranked_candidates.csv"

# -----------------------------
# Debug
# -----------------------------


# -----------------------------
# Stop if file doesn't exist
# -----------------------------
if not CSV_PATH.exists():
    st.error("ranked_candidates.csv not found!")
    st.stop()

# -----------------------------
# Load CSV
# -----------------------------
results = pd.read_csv(CSV_PATH)

# -----------------------------
# Sidebar
# -----------------------------
st.sidebar.title("Select Job Role")

job = st.sidebar.selectbox(
    "Job",
    [
        "Machine Learning Engineer",
        "Data Scientist",
        "Python Developer"
    ]
)

# -----------------------------
# Title
# -----------------------------
st.title("📄 AI Resume Screening & Candidate Ranking System")

st.success(f"Selected Job Role: {job}")

# -----------------------------
# Top Table
# -----------------------------
st.subheader("Top Ranked Candidates")

st.dataframe(results.head(10), use_container_width=True)

# -----------------------------
# Best Candidate
# -----------------------------
top = results.iloc[0]

col1, col2 = st.columns(2)

with col1:
    st.metric(
        "Similarity Score",
        f"{top['Similarity Score']}%"
    )

    st.write("### Matched Skills")
    matched = eval(top["Matched Skills"]) if isinstance(top["Matched Skills"], str) else top["Matched Skills"]

if matched:
    for skill in matched:
        st.success(skill)
else:
    st.warning("No matched skills found.")

with col2:
    st.write("### Missing Skills")
    missing = eval(top["Missing Skills"]) if isinstance(top["Missing Skills"], str) else top["Missing Skills"]

if missing:
    for skill in missing:
        st.error(skill)
else:
    st.success("No missing skills.")

# -----------------------------
# Chart
# -----------------------------
st.subheader("Candidate Scores")

chart = results.head(10).set_index("Rank")["Similarity Score"]
st.bar_chart(chart)

