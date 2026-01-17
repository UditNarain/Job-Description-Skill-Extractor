import streamlit as st
import spacy
from spacy.matcher import PhraseMatcher

st.title("Job Description Skill Extractor")
skills_db = ["python", "sql", "excel", "react", "java", "machine learning"]
jd = st.text_area("Paste job description here")

nlp = spacy.load("en_core_web_sm")
matcher = PhraseMatcher(nlp.vocab, attr="LOWER")
patterns = [nlp.make_doc(skill) for skill in skills_db]
matcher.add("SKILLS", patterns)




if st.button("Extract Skills"):
    doc=nlp(jd)
    matches = matcher(doc)
    found = sorted(doc[start:end].text for match_id, start, end in matches)
    if found:
        st.subheader("Extracted Skills:")
        for skill in found:
            st.write(f"- {skill}")    
    else:
        st.write("No skills found.")

