import os
import streamlit as st
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores  import FAISS
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
load_dotenv(override=True)

llm = ChatGroq(model="llama-3.1-8b-instant", api_key= os.getenv("GROQ_API_KEY"), max_tokens=1000)
loader = PyPDFLoader("Hospital_Policy_Single_Document.pdf")
docs = loader.load()
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
splitted_docs = text_splitter.split_documents(docs)
embeddings = OpenAIEmbeddings(model = "text-embedding-3-small", openai_api_key= os.getenv("OPENAI_API_KEY"))
vectorstore = FAISS.from_documents(splitted_docs, embeddings)
retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

prompt = ChatPromptTemplate.from_messages([
    ("system", 
    "You are a helpful assistant that can answer questions about the hospital policy."
    "Use the provided context, If you don't know the answer, say I don't know the answer say so politely. \n\n"
    "Context: \n{context}"
    ),
    ("user","{question}")
])
chain = (
    {
        "context": retriever,
        "question": RunnablePassthrough(),
    } 
    | prompt | llm | StrOutputParser()
)

st.title("Hospital Policy RAG Chatbot")
question = st.text_input("Enter your question", key="input")
if question:
    response = chain.invoke(question)
    st.write(response)
