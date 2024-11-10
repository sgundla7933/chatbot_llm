import os
import openai
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv, find_dotenv
from langchain.embeddings import OpenAIEmbeddings
from langchain.chat_models import ChatOpenAI

from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import DocArrayInMemorySearch
from langchain_community.document_loaders import PyPDFLoader
from langchain.chains import ConversationalRetrievalChain

load_dotenv(find_dotenv())
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'

openai.api_key = os.getenv('OPENAI_API_KEY')

# Initialize chatbot chain
chat_history = []
qa = None  # Initialized after document is loaded

def load_db(file_path, chain_type, k):
    loader = PyPDFLoader(file_path)
    documents = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=150)
    docs = text_splitter.split_documents(documents)
    embeddings = OpenAIEmbeddings()
    llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
    db = DocArrayInMemorySearch.from_documents(docs, embeddings)
    retriever = db.as_retriever(search_type="similarity", search_kwargs={"k": k})
    
    global qa
    qa = ConversationalRetrievalChain.from_llm(
        llm=ChatOpenAI(model="gpt-3.5-turbo", temperature=0),
        chain_type=chain_type,
        retriever=retriever,
        return_source_documents=True,
        return_generated_question=True,
    )

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/load_db', methods=['POST'])
def load_document():
    file = request.files['file']
    if file:
        # Ensure the uploads directory exists
        os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
        
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], 'temp.pdf')
        file.save(file_path)
        load_db(file_path, "stuff", 4)
        return jsonify({"message": "Document loaded successfully!"})
    return jsonify({"error": "No file uploaded!"}), 400


@app.route('/chat', methods=['POST'])
def chat():
    global chat_history, qa
    user_message = request.json.get('message')
    if not user_message or not qa:
        return jsonify({"error": "Invalid message or no document loaded!"}), 400

    result = qa({"question": user_message, "chat_history": chat_history})
    chat_history.append((user_message, result["answer"]))
    
    response = {
        "user_message": user_message,
        "bot_response": result["answer"],
        "generated_question": result["generated_question"],
        "source_documents": [str(doc) for doc in result["source_documents"]]
    }
    return jsonify(response)

@app.route('/clear_history', methods=['POST'])
def clear_history():
    global chat_history
    chat_history = []
    return jsonify({"message": "Chat history cleared!"})

if __name__ == '__main__':
    app.run(port=5006, debug=True)
