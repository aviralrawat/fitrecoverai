import streamlit as st
from openai import OpenAI
import os

# Load API key from environment variable
client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

st.title("🏥 FitRecoverAI")
st.subheader("AI-Powered Injury Recovery Assistant")

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

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    st.write("### Recovery Plan:")
    st.write(response.choices[0].message["content"])
