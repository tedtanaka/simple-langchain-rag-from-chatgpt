# simple-langchain-rag-from-chatgpt
I asked ChatGPT to provide a simple RAG implementation with Langchain.

This code reads in a sample Fidelity statement PDF file and runs a couple queries on it.

To run in Windows CMD shell:

* python -m venv venv
* venv\Scripts\activate.bat
* pip install -r requirements.txt
* update the .env file with your OpenAI api key
* python simple-langchain-rag.py

To run in a Codespace (Linux):

* python -m venv venv
* source venv/bin/activate
* pip install -r requirements.txt
* update the .env file with your OpenAI api key
* python simple-langchain-rag.py
