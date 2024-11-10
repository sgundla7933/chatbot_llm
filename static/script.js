async function uploadFile() {
    const fileInput = document.getElementById('file-input');
    const formData = new FormData();
    formData.append('file', fileInput.files[0]);

    try {
        const response = await fetch('/load_db', {
            method: 'POST',
            body: formData
        });
        const data = await response.json();
        alert(data.message || data.error);
    } catch (error) {
        console.error('Error loading document:', error);
    }
}

async function sendMessage() {
    const userMessage = document.getElementById('user-message').value;
    if (!userMessage) return;

    try {
        const response = await fetch('/chat', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ message: userMessage })
        });
        const data = await response.json();

        // Display messages in chat history
        const chatHistory = document.getElementById('chat-history');
        chatHistory.innerHTML += `<p><strong>User:</strong> ${userMessage}</p>`;
        chatHistory.innerHTML += `<p><strong>Bot:</strong> ${data.bot_response}</p>`;
        
        // Display source documents if available
        if (data.source_documents.length > 0) {
            chatHistory.innerHTML += `<p><em>Source Documents:</em> ${data.source_documents.join('<br>')}</p>`;
        }

        document.getElementById('user-message').value = '';  // Clear input
    } catch (error) {
        console.error('Error sending message:', error);
    }
}

async function clearHistory() {
    try {
        const response = await fetch('/clear_history', { method: 'POST' });
        const data = await response.json();
        alert(data.message);

        // Clear chat history on frontend
        document.getElementById('chat-history').innerHTML = '';
    } catch (error) {
        console.error('Error clearing chat history:', error);
    }
}
