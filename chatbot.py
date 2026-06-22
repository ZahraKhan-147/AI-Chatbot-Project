"""
PROJECT: Rule-Based AI Chatbot
BATCH: 2026 | DecodeLabs
"""

responses = {
    'hello': 'Hello! How can I help you today? ',
    'hi': 'Hi there! What brings you here? ',
    'hey': 'Hey! Nice to see you! ',
    'good morning': 'Good morning! Hope you have a great day! ',
    'good evening': 'Good evening! How was your day? ',
    'what is your name': "I'm ChatBot-1, your digital assistant! ",
    'who are you': "I'm a simple rule-based chatbot built for DecodeLabs!",
    'weather': "I don't have real-time data, but it's sunny in my world! ",
    'how are you': "I'm great, thanks for asking! How can I help you? ",
    'time': "Time is an illusion. But you can check your system clock! ",
    'help': """ CHATBOT HELP:
I can respond to:
• Greetings: hello, hi, hey
• Name: what is your name
• Weather: weather
• Feelings: how are you
• Time: time
• Exit: bye, quit, exit""",
    'bye': "Goodbye! Come back anytime! "
}

exit_commands = ['bye', 'quit', 'exit', 'goodbye', 'see you']

def sanitize_input(text):
    return text.lower().strip()

def get_response(user_input):
    if user_input in responses:
        return responses[user_input]
    
    for key in responses:
        if key in user_input:
            return responses[key]
    
    return "I don't understand that. Can you rephrase? "

def chat():
    print("=" * 50)
    print(" WELCOME TO CHATBOT-1! ")
    print("=" * 50)
    print("Type 'help' to see what I can do")
    print("Type 'bye' to exit")
    print("=" * 50)
    
    while True:
        user_input = input("\nYou: ").strip()
        
        if not user_input:
            continue
        
        cleaned = sanitize_input(user_input)
        
        if cleaned in exit_commands:
            print("Bot: Goodbye! It was great chatting with you! ")
            break
        
        response = get_response(cleaned)
        print(f"Bot: {response}")

if __name__ == "__main__":
    chat()