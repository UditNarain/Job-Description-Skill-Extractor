import streamlit as st

st.title("Job Description Skill Extractor")

jd = st.text_area("Paste job description here")

if st.button("Extract Skills"):
    if jd.strip() == "":
        st.write("No input")
    else:
        st.write(["Python", "SQL", "Excel"])
