import streamlit as st
from langchain_ollama import OllamaLLM

# Initialize the LLM model
llm = OllamaLLM(model="keywordpicker")

def get_keywords(prompt):
    """Takes a prompt and returns the processed keywords."""
    toKeywords = llm.invoke(prompt)
    return toKeywords

def display_response(response):
    """Displays the response in the Streamlit app and appends it to the session state."""
    with st.chat_message("assistant"):
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})

# Streamlit UI setup
st.title("UIUC chatbot")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("What's up?"):
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Get keywords
    toKeywords = get_keywords(prompt)
    print(toKeywords)

    # Use the response (e.g., echoing the keywords for demonstration)
    response = toKeywords  # Modify as needed based on your use case

    # Display the response
    display_response(response)