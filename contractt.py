import streamlit as st
from transformers import pipeline
import os
import re
import difflib  # Import difflib module

# Initialize NER pipeline
ner_pipeline = pipeline("ner", grouped_entities=True)

# Keywords to highlight in the contract
keywords = ["agreement", "party", "confidential", "termination", "liability", "termination date"]

def load_synthetic_contracts():
    contracts = {}
    for filename in os.listdir():
        if filename.startswith("contract_") and filename.endswith(".txt"):
            with open(filename, "r") as file:
                contracts[filename] = file.read()
    return contracts

# Highlight specific terms in the text using regex
def highlight_keywords(text, keywords):
    for keyword in keywords:
        pattern = re.compile(rf'\b{keyword}\b', re.IGNORECASE)
        text = pattern.sub(f"**{keyword}**", text)
    return text

# Highlight specific terms like "termination date" using regex
def highlight_specific_terms(text, terms):
    for term in terms:
        pattern = re.compile(rf'\b{term}\b', re.IGNORECASE)
        text = pattern.sub(f"**{term}**", text)
    return text

# Compare two texts and highlight differences
def highlight_differences(text1, text2):
    diff = difflib.ndiff(text1.splitlines(), text2.splitlines())
    diff_text = '\n'.join(diff)
    return diff_text

# Streamlit app
st.title("Business Contract Comparator")

st.write("Upload your business contracts or select synthetic contracts to compare and see the highlighted terms and differences.")

# Load synthetic contracts
synthetic_contracts = load_synthetic_contracts()

# Select boxes for synthetic contracts
selected_contract1 = st.selectbox("Select the first synthetic contract", list(synthetic_contracts.keys()))
selected_contract2 = st.selectbox("Select the second synthetic contract", list(synthetic_contracts.keys()))

# File uploaders for user-uploaded contracts
uploaded_file1 = st.file_uploader("Or upload your first document", key="file1")
uploaded_file2 = st.file_uploader("Or upload your second document", key="file2")

# Read the contract texts
if uploaded_file1 is not None:
    contract_text1 = uploaded_file1.read().decode("utf-8")
elif selected_contract1:
    contract_text1 = synthetic_contracts[selected_contract1]
else:
    contract_text1 = None

if uploaded_file2 is not None:
    contract_text2 = uploaded_file2.read().decode("utf-8")
elif selected_contract2:
    contract_text2 = synthetic_contracts[selected_contract2]
else:
    contract_text2 = None

# Display the original and highlighted contract texts
if contract_text1 and contract_text2:
    st.subheader("Original Contracts")
    st.text_area("First Contract", contract_text1, height=300)
    st.text_area("Second Contract", contract_text2, height=300)

    highlighted_text1 = highlight_specific_terms(contract_text1, keywords)
    highlighted_text2 = highlight_specific_terms(contract_text2, keywords)

    st.subheader("Highlighted Contracts")
    st.markdown("### First Contract")
    st.markdown(highlighted_text1)
    st.markdown("### Second Contract")
    st.markdown(highlighted_text2)

    st.subheader("Differences Between Contracts")
    differences = highlight_differences(contract_text1, contract_text2)
    st.text_area("Differences", differences, height=300)

    st.subheader("Entities Detected in First Contract")
    entities1 = ner_pipeline(contract_text1)
    for entity in entities1:
        st.write(f"Entity: {entity['word']}, Label: {entity['entity_group']}, Score: {entity['score']:.2f}")

    st.subheader("Entities Detected in Second Contract")
    entities2 = ner_pipeline(contract_text2)
    for entity in entities2:
        st.write(f"Entity: {entity['word']}, Label: {entity['entity_group']}, Score: {entity['score']:.2f}")
