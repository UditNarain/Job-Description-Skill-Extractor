import streamlit as st

st.title("Job Description Skill Extractor")

jd = st.text_area("Paste job description here")

skills_db = ["python", "sql", "excel", "react", "java", "machine learning"]

if st.button("Extract Skills"):
    found = []
    text = jd.lower()
    for skill in skills_db:
        if skill in text:
            found.append(skill.title())
    st.write(found if found else "No skills found")

