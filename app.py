import streamlit as st
import os
import shutil
from modules.document_processor import process_pdf
from modules.vector_db import create_vector_db, get_retriever
from modules.llm_interface import query_llm, generate_assessment

# Page Config
st.set_page_config(page_title="GenAI Training Hub", layout="wide")

st.title("🏦 Banking GenAI Training Hub")
st.markdown("""
Welcome to the **AI-powered Knowledge & Training System**. 
Upload your SOPs/KT documents, ask questions, and take assessments.
""")

# Tabs
tab1, tab2, tab3 = st.tabs(["📂 Training Hub", "🤖 Chatbot", "📝 Assessment"])

# --- Tab 1: Training Hub ---
with tab1:
    st.header("Upload Knowledge Documents")
    uploaded_file = st.file_uploader("Upload a PDF (SOP, KT, SMTD)", type="pdf")
    
    if uploaded_file:
        # Save file locally
        os.makedirs("data/uploaded_docs", exist_ok=True)
        file_path = os.path.join("data/uploaded_docs", uploaded_file.name)
        
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        
        st.success(f"File '{uploaded_file.name}' saved successfully!")
        
        if st.button("Process & Index Document"):
            with st.spinner("Processing PDF and creating vector embeddings..."):
                try:
                    chunks = process_pdf(file_path)
                    st.write(f"Split into {len(chunks)} chunks.")
                    
                    create_vector_db(chunks)
                    st.success("✅ Document processed and added to Knowledge Base!")
                except Exception as e:
                    st.error(f"Error processing document: {e}")

# --- Tab 2: Chatbot ---
with tab2:
    st.header("Conversational Knowledge Assistant")
    
    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # User input
    if prompt := st.chat_input("Ask a question about your documents..."):
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # Generate response
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                try:
                    retriever = get_retriever()
                    # Retrieve relevant docs
                    relevant_docs = retriever.invoke(prompt)
                    context = "\n\n".join([doc.page_content for doc in relevant_docs])
                    
                    if not context:
                        response = "I couldn't find any relevant information in the uploaded documents."
                    else:
                        response = query_llm(prompt, context)
                    
                    st.markdown(response)
                    st.session_state.messages.append({"role": "assistant", "content": response})
                except Exception as e:
                    st.error(f"Error generating response: {e}")

# --- Tab 3: Assessment ---
with tab3:
    st.header("Knowledge Assessment")
    
    topic = st.text_input("Enter a topic to generate a quiz for (e.g., 'Payment Process', 'Incident Management')")
    
    if st.button("Generate Quiz"):
        if not topic:
            st.warning("Please enter a topic.")
        else:
            with st.spinner(f"Generating quiz for '{topic}'..."):
                try:
                    retriever = get_retriever()
                    relevant_docs = retriever.invoke(topic)
                    context = "\n\n".join([doc.page_content for doc in relevant_docs])
                    
                    if not context:
                        st.error("No content found for this topic in the knowledge base.")
                    else:
                        quiz = generate_assessment(topic, context)
                        st.markdown("### Quiz")
                        st.markdown(quiz)
                except Exception as e:
                    st.error(f"Error generating quiz: {e}")
