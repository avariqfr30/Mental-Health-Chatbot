# server.py - Python file for the backend server

from flask import Flask, request, jsonify
from chatbot import chat_with_bot

app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data['user_message']
    chat_history = data.get('chat_history', [])

    bot_reply, updated_chat_history = chat_with_bot(user_message, chat_history)

    return jsonify({"bot_reply": bot_reply, "chat_history": updated_chat_history})

if __name__ == '__main__':
    app.run(debug=True)
