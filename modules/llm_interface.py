from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

def get_llm():
    return ChatOllama(model="llama3")

def query_llm(question, context):
    """
    Queries the LLM with a question and context (RAG).
    """
    prompt_template = ChatPromptTemplate.from_template(
        """
        You are a helpful banking support assistant. Use the following context to answer the question.
        If the answer is not in the context, say "I don't have enough information in the provided documents."
        
        Context:
        {context}
        
        Question:
        {question}
        """
    )
    
    model = get_llm()
    chain = prompt_template | model | StrOutputParser()
    
    response = chain.invoke({"context": context, "question": question})
    return response

def generate_assessment(topic, context):
    """
    Generates a quiz based on the provided context.
    """
    prompt_template = ChatPromptTemplate.from_template(
        """
        Based on the following content about "{topic}", generate 3 multiple-choice questions (MCQs) to test understanding.
        Format the output clearly with the question, options, and the correct answer.
        
        Content:
        {context}
        """
    )
    
    model = get_llm()
    chain = prompt_template | model | StrOutputParser()
    
    response = chain.invoke({"context": context, "topic": topic})
    return response
