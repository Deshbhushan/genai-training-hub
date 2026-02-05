# Project Report Update: Banking GenAI Training Hub

## 1. Project Information
**Project Title:** Banking GenAI Training Hub  
**Student Name:** Deshbhushan Patil  
**Email:** 202117b3581@wilp.bits-pilani.ac.in  

## 2. Mentor Details
**Name:** Uday Kumar  
**Designation:** Senior Manager  
**Company:** HCL CANADA INC.  
**Email:** uday-k@hcltech.com  
**Phone:** +1 6178428047  

## 3. Additional Examiner Details
**Name:** Nikhita Suresh  
**Designation:** Technical Lead  
**Company:** HCL AMERICA INC.  
**Email:** nikhita.suresh@hcltech.com  
**Phone:** +1 7819713618  

---

## 4. Broad Academic Area of Work
Generative AI / Natural Language Processing (NLP) / Knowledge Management / Intelligent Tutoring Systems

## 5. Background
In the banking sector, Production Support teams are critical for maintaining the stability and reliability of financial services. These teams rely heavily on a vast array of documentation, including Standard Operating Procedures (SOPs), Knowledge Transfer (KT) documents, and Service Management Technical Documents (SMTDs). 

Currently, this knowledge is often scattered across various file systems or static repositories. New team members face a significant learning curve, often identifying the right document or expert to solve a specific issue takes considerable time. Traditional keyword-based search mechanisms often fail to capture the context of a query, leading to inefficiency. Furthermore, there is a lack of a structured, interactive mechanism to assess whether a team member has truly understood the critical procedures, leading to potential operational risks.

To address these challenges, the **Banking GenAI Training Hub** introduces an AI-driven platform. By leveraging Large Language Models (LLMs) and Retrieval-Augmented Generation (RAG), the system transforms static documentation into an interactive knowledge base, capable of answering queries, generating assessments, and creating structured learning paths.

## 6. Objectives
The main goals of this project are:
1.  **Develop a Centralized Knowledge Hub:** Create a system to ingest and index diverse banking documents (SOPs, KTs, SMTDs) into a vector database.
2.  **Implement Conversational AI (RAG):** Build a chatbot capable of answering user queries with high accuracy by retrieving relevant context from uploaded documents.
3.  **Automate Knowledge Assessment:** Develop a module to automatically generate quizzes and assessments based on document content to verify user understanding.
4.  **Create Dynamic Learning Paths:** Implement functionality to structure concepts into valid learning sequences, guiding users from basic to advanced topics.
5.  **Enhance User Feedback:** Provide immediate feedback on assessments and queries to facilitate continuous learning.
6.  **Ensure Data Privacy:** Utilize local or secure LLM implementations (e.g., Ollama) to ensure sensitive banking data remains secure.

## 7. Scope of Work
*   **Data Ingestion:** Implement PDF parsing and chunking strategies optimized for technical documentation.
*   **Vector Database Integration:** Set up ChromaDB/FAISS to store and retrieve document embeddings efficiently.
*   **LLM Integration:** Integrate with LLMs (via Ollama or APIs) for reasoning and content generation.
*   **RAG Pipeline:** Develop the retrieval and generation pipeline to ensure answers are grounded in the provided documents (reducing hallucinations).
*   **Assessment Engine:** Design prompt engineering strategies to generate multiple-choice and open-ended questions from text.
*   **Learning Path Algorithm:** Develop logic to identify key concepts and arrange them in a logical learning order.
*   **User Interface:** detailed Streamlit-based UI for uploading, chatting, and taking assessments.
*   **Evaluation:** Test the system with real-world banking SOPs to validate answer accuracy and assessment relevance.

## 8. Plan of Work
*   **Week 1–2:** Literature review, requirement gathering, and dataset collection (dummy banking SOPs). Setup of development environment (Python, Streamlit).
*   **Week 3–4:** Development of the "Training Hub" module: Document upload, PDF processing, and Vector Database setup (ChromaDB).
*   **Week 5–6:** Implementation of the "Chatbot" module: RAG pipeline, LLM integration, and context retrieval logic.
*   **Week 7:** Development of the "Assessment" module: Quiz generation logic and user scoring systems.
*   **Week 8:** Implementation of "Learning Paths": Logic to extract concepts and structure them into a guided curriculum.
*   **Week 9–10:** System integration, UI refinement, and performance optimizations (latency reduction).
*   **Week 11–12:** Testing and Validation: Assessing accuracy of answers and relevance of generated quizzes. Bug fixing.
*   **Week 13–14:** Final Documentation, Project Report preparation, and presentation.

## 9. Literature Reference
*   **Retrieval-Augmented Generation (RAG):** Lewis et al., "Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks."
*   **LangChain Framework:** Documentation on modular LLM application development.
*   **Vector Databases:** Research on efficient similarity search (HNSW algorithms) used in Chroma/FAISS.
*   **Educational Taxonomies:** Bloom’s Taxonomy for educational learning objectives, applied here for generating tiered assessment questions.
*   **LLM Fine-tuning vs RAG:** Comparative studies on knowledge injection in LLMs.
