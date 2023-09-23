# chatbot.py - Python file for handling chatbot API calls

import openai

# Replace 'YOUR_API_KEY' with your actual OpenAI API key
api_key = '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'

def chat_with_bot(user_input, chat_history=None):
    openai.api_key = api_key

    if chat_history is None:
        chat_history = []

    prompt = '\n'.join(chat_history + [f'User: {user_input}', 'AI:'])

    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=50,  # Adjust the length of the response as needed
        temperature=0.7,  # Adjust the temperature for creativity
        stop=None  # Allow the AI to determine when to stop
    )

    ai_reply = response.choices[0].text.strip()
    chat_history.append(f'User: {user_input}')
    chat_history.append(f'AI: {ai_reply}')

    return ai_reply, chat_history
