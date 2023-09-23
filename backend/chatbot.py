# chatbot.py

import openai

# Set your OpenAI API key here
api_key = 'YOUR_OPENAI_API_KEY'

def chat_with_bot(user_message, chat_history):
    # Initialize the OpenAI API client
    openai.api_key = api_key

    # Create a conversation history with user and bot messages
    conversation = chat_history + [f"You: {user_message}", "Bot:"]

    # Generate a response from GPT-3
    response = openai.Completion.create(
        engine="davinci",
        prompt="\n".join(conversation),
        max_tokens=50  # Adjust as needed
    )

    bot_reply = response.choices[0].text.strip()

    # Update the chat history with the user's message and bot's reply
    updated_chat_history = chat_history + [f"You: {user_message}", f"Bot: {bot_reply}"]

    return bot_reply, updated_chat_history
