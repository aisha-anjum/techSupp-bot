import streamlit as st
import google.generativeai as genai
import os

# Configure the API key
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

# Initialize the model
model = genai.GenerativeModel('gemini-pro')

st.title("💻 Code & Technical Support Assistant")
st.write("Ask me any programming or technical questions!")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("What's your technical question?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Generate response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                # Create a context-aware prompt
                system_prompt = """You are a helpful technical support assistant specializing in programming and code-related questions. 
                Provide clear, accurate explanations and code examples when appropriate. Be concise but thorough."""
                
                full_prompt = f"{system_prompt}\n\nUser Question: {prompt}"
                
                response = model.generate_content(full_prompt)
                answer = response.text
                
                st.markdown(answer)
                st.session_state.messages.append({"role": "assistant", "content": answer})
                
            except Exception as e:
                error_msg = f"Sorry, I encountered an error: {str(e)}"
                st.error(error_msg)