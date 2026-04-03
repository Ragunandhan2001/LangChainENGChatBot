from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from langchain_community.llms import Ollama
from langchain_core.prompts import PromptTemplate
from fastapi.responses import FileResponse

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"],
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"],
)

llm = Ollama(model="phi3")

prompt = PromptTemplate.from_template("""
You are a english friendly partner
                                      
Rules -
 - correct grammar mistakes
 - explain it simply
                                      
 sentance - {input}
""")

chain = prompt | llm

@app.get("/")
def serve_ui():
    return FileResponse("index.html")

@app.post("/chat")
def chat(msg : str):

    response = chain.invoke({"input" : msg})

    return {"response" : response}
    












# from langchain_community.llms import Ollama
# from langchain_core.prompts import PromptTemplate

# # Load model
# llm = Ollama(model="phi3")

# # Prompt
# prompt = PromptTemplate.from_template("""
# You are a friendly English teacher.

# Rules:
# - Correct grammar mistakes
# - Explain simply

# Sentence: {input}
# """)

# # Chain
# chain = prompt | llm

# # Run
# response = chain.invoke({"input": "the bed is too heavy because they didn't lift it"})
# print(response)