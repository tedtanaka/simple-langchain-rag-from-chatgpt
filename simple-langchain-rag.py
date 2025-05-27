import getpass
import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_openai import ChatOpenAI
from langchain.chains import RetrievalQA


try:
    # load environment variables from .env file (requires `python-dotenv`)
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

# Load and split PDF
loader = PyPDFLoader("sample-fidelity-statement.pdf")
docs = loader.load_and_split()

# Embed and store in FAISS
db = FAISS.from_documents(docs, OpenAIEmbeddings())

# Build retrieval-based QA chain
qa_chain = RetrievalQA.from_chain_type(
    llm=ChatOpenAI(model_name="gpt-4"),
    retriever=db.as_retriever()
)

# Ask a question
response = qa_chain.invoke("List the assets in the portfolio.")
print(response)
print()

response = qa_chain.invoke("Analyze this portfolio's asset allocation and risk exposure.")
print(response)
print()
