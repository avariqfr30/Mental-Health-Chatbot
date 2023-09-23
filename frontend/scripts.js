// script.js

document.addEventListener('DOMContentLoaded', function () {
    const chatBody = document.getElementById('chat-body');
    const userInput = document.getElementById('user-input');
    const sendButton = document.getElementById('send-button');

    sendButton.addEventListener('click', function () {
        const userMessage = userInput.value.trim();
        if (userMessage === '') return;

        appendMessage('You', userMessage);
        userInput.value = '';

        // Make a POST request to the FastAPI endpoint (/chat)
        fetch('/chat', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                user_message: userMessage,
                chat_history: []  // Add your chat history logic here
            })
        })
        .then(response => response.json())
        .then(data => {
            // Handle the response from the server
            const botReply = data.bot_reply;
            appendMessage('Virtual Therapist', botReply);
        })
        .catch(error => {
            console.error('Error:', error);
        });
    });

    function appendMessage(sender, message) {
        const messageElement = document.createElement('div');
        messageElement.innerHTML = `<strong>${sender}:</strong> ${message}`;
        chatBody.appendChild(messageElement);
    }
});