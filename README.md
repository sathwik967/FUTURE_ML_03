# FUTURE_ML_03
 Machine Learning

# AI Resume Screening & Candidate Ranking System

## Overview

The **AI Resume Screening & Candidate Ranking System** is a Natural Language Processing (NLP) and Machine Learning project that automates resume screening by comparing candidate resumes against a job description.

The system extracts skills, preprocesses textual information, computes semantic similarity using TF-IDF and Cosine Similarity, ranks candidates based on relevance, and identifies missing skills.

This project demonstrates how Applicant Tracking Systems (ATS) assist recruiters in shortlisting candidates efficiently.

---

## Features

* Resume text preprocessing
* Job description preprocessing
* Skill extraction using NLP
* Resume-to-job similarity scoring
* Candidate ranking
* Missing skill detection
* Skill frequency analysis
* Word Cloud visualization
* Candidate score visualization
* Export ranked candidates to CSV

---

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* NLTK
* spaCy
* Matplotlib
* WordCloud
* Streamlit (Optional)

---

## Project Workflow

Resume Dataset

↓

Text Cleaning

↓

Text Preprocessing

↓

Skill Extraction

↓

Job Description Processing

↓

TF-IDF Vectorization

↓

Cosine Similarity

↓

Candidate Ranking

↓

Skill Gap Analysis

↓

Visualization & Export

---

## Machine Learning Techniques

* Natural Language Processing (NLP)
* TF-IDF Vectorization
* Cosine Similarity
* Text Preprocessing
* Feature Extraction
* Skill Matching

---

## Dataset

### Resume Dataset

* 2,484 resumes
* Multiple job categories
* Text-based resumes

### Job Description Dataset

* 22,000 real-world job descriptions
* Various industries and job roles

---

## Outputs

* Ranked Candidates
* Similarity Scores
* Matched Skills
* Missing Skills
* Ranking Chart
* Word Cloud
* Skill Frequency Graph

---

## Installation

```bash
git clone https://github.com/yourusername/Resume-Screening-System.git

cd Resume-Screening-System

pip install -r requirements.txt
```

---

## Run Notebook

Open

```
notebooks/Resume_Screening_System.ipynb
```

Run all cells.

---

## Streamlit App

```
streamlit run app/app.py
```

---

## Future Improvements

* Transformer-based Resume Matching
* BERT Sentence Embeddings
* PDF Resume Upload
* Resume Parsing using spaCy
* Experience Extraction
* Education Detection
* Certification Matching

---

## Author

Sathwik Salian
Future Interns – Machine Learning Task 3 (2026)
