import streamlit as st
import requests

st.title("Simple AI Chatbot Test")

api_key = st.text_input("OpenRouter API Key", type="password")
question = st.text_input("Ask a question:")

if api_key and question:
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "anthropic/claude-3-haiku:beta",
        "messages": [{"role": "user", "content": question}]
    }
    
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        result = response.json()
        st.write("Answer:", result['choices'][0]['message']['content'])
    else:
        st.error(f"Error: {response.status_code} - {response.text}")