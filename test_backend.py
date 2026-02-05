from modules.llm_interface import query_llm
from langchain_core.documents import Document
from modules.vector_db import create_vector_db, get_retriever

print("--- Testing LLM Integration ---")
try:
    response = query_llm("What is the capital of France?", "The capital of France is Paris.")
    print(f"LLM Response: {response}")
except Exception as e:
    print(f"LLM Error: {e}")

print("\n--- Testing Vector DB ---")
try:
    docs = [Document(page_content="The sky is blue.", metadata={"source": "test"})]
    create_vector_db(docs)
    retriever = get_retriever()
    results = retriever.invoke("What color is the sky?")
    print(f"Retrieved: {results[0].page_content}")
except Exception as e:
    print(f"Vector DB Error: {e}")
