import streamlit as st
import re

# Function to convert text into LaTeX math symbols
def latex_converter(input_text):
    # Replace common phrases with their LaTeX equivalents
    replacements = {
        "for all": "\\forall",                 # ∀
        "there exists": "\\exists",            # ∃
        "such that": "\\text{s.t.}",           # s.t.
        " in ": " \\in ",                      # ∈
        "real numbers": "\\mathbb{R}",         # ℝ
        "rational numbers": "\\mathbb{Q}",     # ℚ
        "integers": "\\mathbb{Z}",             # ℤ
        "natural numbers": "\\mathbb{N}",      # ℕ
        "complex numbers": "\\mathbb{C}",      # ℂ
        " and ": "\\wedge",                      # ∧
        " or ": "\\vee",                         # ∨
        " not ": "\\neg",                        # ¬
        "if and only if": "\\iff",             # ↔
        "implies": "\\implies",                # →
        "integral of": "\\int",                # ∫
        "sum of": "\\sum",                     # Σ
        "equals": "=",                         # =
        "converges to": "\\to",                # →
        "function": "f : ",                    # function notation
        " to ": "\\to",                          # →
        "sqrt": "\\sqrt",                      # √
        "^": "^",                              # Exponentiation
        "_": "_"                               # Subscripts
        # Add more as needed
    }
    
    # Replace text with corresponding LaTeX symbols
    for key, value in replacements.items():
        input_text = input_text.replace(key, value)

    # Capture any remaining text that was not replaced and convert it to \text{}
    # This regex matches any alphabetic word (not already in a LaTeX format) and wraps it in \text{}
    input_text = re.sub(r'([a-zA-Z]+)', r'\\text{\1}', input_text)

    return input_text

# Streamlit app layout
st.title("Text to LaTeX Math Symbol Converter")

# Text input from user
input_text = st.text_area("Enter text with math phrases:")

# Button to trigger conversion
if st.button("Convert to LaTeX"):
    latex_output = latex_converter(input_text)

    # Render LaTeX instead of just displaying the code
    st.latex(latex_output)

    # Optionally show the LaTeX code for users who want to copy it
    st.text_area("LaTeX Code", value=latex_output, height=100, disabled=True)
