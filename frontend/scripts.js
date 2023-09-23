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

        // Call your chatbot function here and append its response
        // Example: chatWithBot(userMessage);

        // For this example, we'll simulate a response
        const botMessage = 'This is a simulated response from the bot.';
        setTimeout(() => {
            appendMessage('Virtual Therapist', botMessage);
        }, 500);
    });

    function appendMessage(sender, message) {
        const messageContainer = document.createElement('div');
        messageContainer.className = 'message';
        messageContainer.innerHTML = `<strong>${sender}:</strong> ${message}`;
        chatBody.appendChild(messageContainer);

        // Scroll to the bottom to show the latest message
        chatBody.scrollTop = chatBody.scrollHeight;
    }
});