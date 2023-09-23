# app.py

from fastapi import FastAPI
from pydantic import BaseModel
from chatbot import chat_with_bot

app = FastAPI()

class UserInput(BaseModel):
    user_message: str
    chat_history: list

@app.post("/chat")
def chat(user_input: UserInput):
    user_message = user_input.user_message
    chat_history = user_input.chat_history

    # Call your chatbot logic
    bot_reply, updated_chat_history = chat_with_bot(user_message, chat_history)

    return {"bot_reply": bot_reply, "chat_history": updated_chat_history}
