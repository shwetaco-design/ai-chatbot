import streamlit as st
from groq import Groq


client = Groq(api_key="your-key-here")

st.title("My AI Chatbot")

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "You are a helpful study assistent for indian students. You explain everything simply with examples"}
    ]

for message in st.session_state.messages:
    st.write(message["role"]  + ":" + message["content"])

user_message = st.text_input("Ask anything: ")

if st.button("Send"):
    st.session_state.messages.append({"role": "user", "content": user_message})

    response = client.chat.completions.create(
       model="llama-3.3-70b-versatile",
       temperature=1,
       messages=st.session_state.messages
   )

    reply = response.choices[0].message.content
    st.session_state.messages.append({"role": "assistant", "content": reply})
    st.write("Assistant: " + reply)