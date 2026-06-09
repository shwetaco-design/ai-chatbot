import streamlit as st
from groq import Groq

client = Groq(api_key=st.secrets["GROQ_API_KEY"])

st.title("My AI Study Assistant")

system_prompt = """You are an expert Indian teacher with 20 years of experience teaching all subjects.

Your students are Indian school and college students who struggle to understand complex concepts.

Your job is to:
- Explain every concept in simple easy language
- Always give a real life Indian example (use dosa, cricket, chai, rupees etc)
- For math and science — show step by step solution
- At the end of every explanation ask: Did you understand? Want me to explain differently?
- Never use complicated English words when simple ones work

Always be encouraging and patient. Never make the student feel stupid."""

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": system_prompt}
    ]

for message in st.session_state.messages:
    if message["role"] != "system":
        st.write(message["role"] + ": " + message["content"])

user_message = st.text_input("Ask anything:")

if st.button("Send"):
    st.session_state.messages.append({"role": "user", "content": user_message})

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        temperature=0.7,
        messages=st.session_state.messages
    )

    reply = response.choices[0].message.content
    st.session_state.messages.append({"role": "assistant", "content": reply})
    st.write("Assistant: " + reply)
