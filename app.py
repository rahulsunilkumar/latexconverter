import streamlit as st

# Function to convert text into LaTeX math symbols
def latex_converter(input_text):
    # Replace common phrases with their LaTeX equivalents
    replacements = {
        "for all": "\\forall",                 # ∀
        "there exists": "\\exists",            # ∃
        "such that": "\\text{s.t.}",           # s.t.
        " in ": " \\in ",                      # ∈
        "and": "\\wedge",                      # ∧
        "or": "\\vee",                         # ∨
        "not": "\\neg",                        # ¬
        "if and only if": "\\iff",             # ↔
        "implies": "\\implies",                # →
        "sqrt": "\\sqrt",                      # √
        "^": "^",                              # Exponentiation
        "_": "_"                               # Subscripts
        # Add more as needed
    }
    
    # Replace text with corresponding LaTeX symbols
    for key, value in replacements.items():
        input_text = input_text.replace(key, value)
    
    return input_text

# Streamlit app layout
st.title("Text to LaTeX Math Symbol Converter")

# Text input from user
input_text = st.text_area("Enter text with math phrases:")

# Button to trigger conversion
if st.button("Convert to LaTeX"):
    latex_output = latex_converter(input_text)
    st.text_area("LaTeX Output", value=latex_output, height=200)

    # Display LaTeX code for copying
    st.write("Copy the LaTeX code below:")
    st.code(latex_output, language='latex')
