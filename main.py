from langchain_ollama import OllamaLLM

llm = OllamaLLM(model="keywordpicker")

que = "what is the tution for the computer science major student"
que1 = "what is the tution for the international business major student"

response = llm.invoke(que1)
print(response)

# with open("output1.txt", "a") as file:
#     file.write(response + "\n")

#.venv\Scripts\activate
#pip install -U langchain-ollama
#ollama pull llama3.1
#python main.py
#python main.py > output.txt

#pip install streamlit --upgrade