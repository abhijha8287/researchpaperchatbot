from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate, load_prompt

# Load environment variables (like OPENAI_API_KEY)
load_dotenv()

# Load model
model = ChatOpenAI(model_name="gpt-4", api_key=st.secrets['api_key'], temperature=0)

# Streamlit UI
st.header('Research Tool')

paper_input = st.selectbox(
    "Select Research Paper Name",
    [
        "Attention Is All You Need",
        "BERT: Pre-training of Deep Bidirectional Transformers",
        "GPT-3: Language Models are Few-Shot Learners",
        "Diffusion Models Beat GANs on Image Synthesis"
    ]
)

style_input = st.selectbox(
    "Select Explanation Style",
    ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"]
)

length_input = st.selectbox(
    "Select Explanation Length",
    ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"]
)

# ✅ Proper use of PromptTemplate with keyword arguments
template = PromptTemplate(
    template="Please generate a {length_input} explanation of {paper_input} in {style_input} style.",
    input_variables=["paper_input", "style_input", "length_input"]
)
# When the button is clicked
if st.button('Summarize'):
    # ✅ Send the final string to the model
    chain = template | model
    result = chain.invoke(
        {
            "paper_input": paper_input,
            "style_input": style_input,
            "length_input": length_input
        }
    )

    # ✅ Show model output
    st.write(result.content)