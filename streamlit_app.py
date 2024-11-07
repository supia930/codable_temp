import streamlit as st
from langchain_ollama import OllamaLLM

llm = OllamaLLM(model="keywordpicker")

st.title("UIUC chatbot")

# with st.chat_message(name="user"):
#   st.write("Hello")

#initialize chat history
if "messages" not in st.session_state:
  st.session_state.messages = []

#display chat messages from history
for message in st.session_state.messages:
  with st.chat_message(message["role"]):
    st.markdown(message["content"])

#react to user input
if prompt := st.chat_input("What's up?"):
  #display user message in chat message container
  with st.chat_message("user"):
    st.markdown(prompt)
    toKeywords = llm.invoke(prompt)
    print(toKeywords)
  
  # add user message to chat history
  st.session_state.messages.append({"role": "user", "content": prompt})

  # response = f"Echo: {prompt}"
  response = toKeywords

  #display assistant response in chat message container
  with st.chat_message("assistant"):
    st.markdown(response)
  
  #add assistant response to chat history
  st.session_state.messages.append({"role": "assistant", "content": response})


#streamlit run streamlit_app.py