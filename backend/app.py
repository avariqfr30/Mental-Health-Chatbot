# app.py - FastAPI route handler with chatbot logic

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class UserInput(BaseModel):
    user_message: str
    chat_history: list

@app.post("/chat")
def chat(user_input: UserInput):
    user_message = user_input.user_message
    chat_history = user_input.chat_history

    # Replace this example logic with your chatbot implementation
    bot_reply = generate_bot_response(user_message)

    # Update the chat history with the user's message and bot's reply
    updated_chat_history = chat_history + [f'User: {user_message}', f'Bot: {bot_reply}']

    return {"bot_reply": bot_reply, "chat_history": updated_chat_history}

def generate_bot_response(user_message):
    # Example: A simple chatbot that echoes the user's message
    return f"You said: {user_message}"

