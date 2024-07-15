# Business Contract Comparator

## Overview
The Business Contract Comparator is a web application designed to streamline and enhance the analysis of business contracts. It leverages natural language processing (NLP) techniques to highlight key terms, identify textual differences, and extract relevant entities from contractual documents.

## Features
- **Keyword Highlighting**: Highlights important terms such as "agreement," "party," "confidential," "termination," "liability," and "termination date."
- **Text Comparison**: Compares two contracts and highlights the differences.
- **Named Entity Recognition (NER)**: Extracts entities such as dates, organizations, and individuals from the contract text.
- **Interactive Web Interface**: Built using Streamlit, providing an easy-to-use platform for contract analysis.

## Technology Stack
- **Python**: Primary programming language.
- **Streamlit**: Framework for building the web interface.
- **Transformers (Hugging Face)**: Library for NER.
- **Difflib**: Library for text comparison.
- **Regular Expressions (re)**: Used for keyword highlighting.

## Installation

1. **Clone the repository**:
   ```sh
   git clone https://github.com/your-username/business-contract-comparator.git
   cd business-contract-comparator
