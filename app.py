import streamlit as st
from groq import Groq
import os

# Load Groq API key from environment
client = Groq(api_key=os.environ["GROQ_API_KEY"])

st.title("🏥 FitRecoverAI")
st.subheader("AI-Powered Injury Recovery Assistant (FREE using Groq API)")

injury = st.text_input("Enter your injury:")
pain = st.slider("Pain level (1–10):", 1, 10)
sport = st.text_input("Sport you play:")

if st.button("Analyze"):
    prompt = f"""
    You are FitRecoverAI.
    Injury: {injury}
    Pain level: {pain}
    Sport: {sport}

    Provide:
    1. Possible causes
    2. Immediate steps
    3. 24–48 hour recovery plan
    4. When to see a doctor
    """

chat = client.chat.completions.create(
    model="llama3-70b-8192",
    messages=[{
        "role": "user",
        "content": prompt
    }]
)


    result = chat.choices[0].message["content"]

    st.write("### Recovery Plan:")
    st.write(result)

