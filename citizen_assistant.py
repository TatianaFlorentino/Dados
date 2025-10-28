import streamlit as st
import pandas as pd
from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI  # ou VertexAI
from langchain.chains import LLMChain

# -----------------------------
# 1. Carregar FAQ
# -----------------------------
faq = pd.read_csv("faq.csv")

# -----------------------------
# 2. Criar pipeline com LangChain
# -----------------------------
template = """
Você é um assistente que responde dúvidas de cidadãos sobre um sistema público.
Use as respostas do FAQ abaixo para responder de forma clara e simples:

FAQ:
{faq_data}

Pergunta do usuário: {user_question}
Resposta:
"""

prompt = PromptTemplate(input_variables=["faq_data", "user_question"], template=template)
llm = OpenAI(temperature=0)  # Substitua por VertexAI se quiser
chain = LLMChain(llm=llm, prompt=prompt)

def responder_pergunta(user_question):
    faq_text = "\n".join([f"Q: {q} A: {a}" for q, a in zip(faq["Pergunta"], faq["Resposta"])])
    return chain.run(faq_data=faq_text, user_question=user_question)

# -----------------------------
# 3. Interface Streamlit
# -----------------------------
st.title("Citizen Support Assistant – Manual Interativo")
st.write("Pergunte algo sobre o sistema e receba uma resposta rápida!")

user_input = st.text_input("Digite sua pergunta:")

if user_input:
    resposta = responder_pergunta(user_input)
    st.write(resposta)
