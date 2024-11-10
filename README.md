# chatbot_llm

Here's a README file for the Flask-based conversational chatbot application that leverages OpenAI's API and LangChain for document-based queries:

---

# Conversational Chatbot with Document Retrieval

This is a Flask-based web application that lets users upload PDF documents and interact with a chatbot to ask questions based on the document content. It uses OpenAI's language model and LangChain's document retrieval and embeddings capabilities to retrieve relevant information from the uploaded PDF.

## Table of Contents
1. [Features](#features)
2. [Technologies Used](#technologies-used)
3. [Installation](#installation)
4. [Usage](#usage)
5. [API Endpoints](#api-endpoints)
6. [Project Structure](#project-structure)
7. [Future Enhancements](#future-enhancements)

## Features
- **PDF Document Upload:** Upload a PDF document to create a searchable knowledge base.
- **Conversational Retrieval:** Query the document using natural language.
- **Chat History Management:** Stores chat history for continuous conversation.
- **Clear Chat History:** Reset the chat history to start a new conversation.

## Technologies Used
- **Python** with **Flask** for the web framework.
- **OpenAI API** for accessing the `gpt-3.5-turbo` language model.
- **LangChain** for document embeddings, retrieval, and conversational chains.
- **DocArrayInMemorySearch** from `langchain_community` for in-memory vector storage.
- **dotenv** to manage environment variables.

## Installation

1. **Clone the repository:**
   
   git clone https://github.com/yourusername/conversational-chatbot.git
   cd conversational-chatbot
  

2. **Install dependencies:**

   pip install -r requirements.txt
 

3. **Set up environment variables:**
   - Create a `.env` file in the root directory.
   - Add your OpenAI API key to the `.env` file:
    
     OPENAI_API_KEY=your_openai_api_key


4. **Create the uploads folder:**
 
   mkdir uploads


5. **Run the application:**
  
   python app.py

   - The app will be available at http://localhost:5006.

## Usage
1. **Load a PDF Document:**
   - Go to `http://localhost:5006`.
   - Upload a PDF file, which will be processed and split into searchable chunks.
   
2. **Ask Questions:**
   - Enter a question in the chat interface, and the chatbot will retrieve relevant information from the document.
   
3. **Clear Chat History:**
   - Use the "Clear Chat" button to reset the conversation.

## API Endpoints
- **`GET /`**: Serves the main interface (`index.html`).
- **`POST /load_db`**: Uploads and processes a PDF document.
  - **Request**: Form data with `file`.
  - **Response**: JSON message indicating success or failure.
- **`POST /chat`**: Sends a user question to the chatbot.
  - **Request**: JSON object with `message`.
  - **Response**: JSON object with the chatbot's response, generated question, and source documents.
- **`POST /clear_history`**: Clears the chat history.
  - **Response**: JSON message indicating success.

## Project Structure
```plaintext
.
├── app.py               # Main Flask application
├── templates
│   └── index.html       # HTML template for the front end
├── uploads              # Folder for uploaded PDF files
├── .env                 # Environment variables file
└── requirements.txt     # Project dependencies
```

## Future Enhancements
- **Multiple Document Support**: Allow users to upload and query multiple documents.
- **User Authentication**: Secure the application for authenticated access.
- **Extended File Types**: Support for other file types, such as DOCX and TXT.
- **Enhanced UI**: Improve the front-end design and add more features for user interaction.

---

This README covers the core details of the chatbot project, including setup, usage, and additional information on the endpoints and structure.
