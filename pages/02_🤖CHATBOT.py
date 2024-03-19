
import streamlit as st
import google.generativeai as genai

with st.sidebar:
    st.title("Gemini API")
    # Set API key
    api_key = ...
    if api_key:
        genai.configure(api_key=api_key)
    else:
        # Display error message
        # TODO
        pass
    select_model = ...
    
    # Clear chat
    if st.button("Clear chat"):
        st.session_state["messages"] = []
        st.rerun()

# Function to get response
def get_response(messages, model="gemini-pro"):
    model = genai.GenerativeModel(model)
    res = model.generate_content(messages, stream=True,
                                safety_settings={'HARASSMENT':'block_none'})
    return res

# initialize messages in session state
if "messages" not in st.session_state:
    st.session_state["messages"] = []
messages = st.session_state["messages"]

# Display chat messages
for item in messages:
    role, parts = item.values()
    # Display message
    # TODO

# Chat input
chat_message = ...

# Get response
if chat_message:
    # TODO
    pass
