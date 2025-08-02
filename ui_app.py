import streamlit as st
from main import run_agents 
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()
openai_key = os.getenv("OPENAI_API_KEY")

if not openai_key:
    st.error("❌ OPENAI_API_KEY not found in .env file.")
    st.stop()

# Set page config
st.set_page_config(page_title="AI Research Paper Companion", layout="centered")
st.title("📄 AI Research Paper Companion")

# Upload PDF
uploaded_file = st.file_uploader("Upload a research paper (PDF)", type="pdf")

if uploaded_file:
    # Save the uploaded PDF
    with open("paper.pdf", "wb") as f:
        f.write(uploaded_file.read())

    if st.button("🔍 Analyze Paper"):
        with st.spinner("Running AI agents..."):
            output = run_agents()
        st.success("✅ Done!")
        st.write("### 🔬 Analysis Result")
        st.markdown(output)
