"""
PROJECT: Rule-Based AI Chatbot (COMPLETE UPGRADED VERSION)
BATCH: 2026 | DecodeLabs
DESCRIPTION: A fully featured rule-based chatbot with random responses,
             user name memory, chat logging, timestamps, and error handling.
"""

import random
import datetime

# Global variable to store user's name
user_name = None

# ==========================================
# KNOWLEDGE BASE WITH RANDOM RESPONSES
# ==========================================
responses = {
    'hello': [
        'Hello! How can I help you today?',
        'Hi there! Great to see you!',
        'Hey! What brings you here today?'
    ],
    
    'hi': [
        'Hi there! What is up?',
        'Hello! Nice to meet you!',
        'Hey hey! Welcome!'
    ],
    
    'hey': [
        'Hey! How can I assist you?',
        'Hello! Ready to chat?',
        'Hi! What can I do for you?'
    ],
    
    'good morning': [
        'Good morning! Hope you have a great day!',
        'Morning! Ready to accomplish great things?',
        'Good morning! How can I help you today?'
    ],
    
    'good evening': [
        'Good evening! How was your day?',
        'Evening! Relax and chat with me!',
        'Good evening! What brings you here?'
    ],
    
    'how are you': [
        'I am fantastic! How about you?',
        'Doing great, thanks for asking!',
        'I am wonderful! Ready to chat!'
    ],
    
    'how are you doing': [
        'I am doing excellent! How about you?',
        'Could not be better! Thanks for asking!',
        'I am thriving! What about you?'
    ],
    
    'weather': [
        'It is always sunny in the digital world!',
        'I do not have real-time data, but it is beautiful outside!',
        'Weather is perfect in my virtual world!'
    ],
    
    'time': [
        'Time is an illusion. But check your system clock!',
        'I am timeless! But your clock says something else.',
        'Time flies when you are chatting with me!'
    ],
    
    'what is your name': [
        'I am ChatBot-1, your digital assistant!',
        'I am ChatBot-1! Nice to meet you!'
    ],
    
    'who are you': [
        'I am a simple rule-based chatbot built for DecodeLabs!',
        'I am ChatBot-1, your friendly assistant!'
    ],
    
    'help': """CHATBOT HELP:
I can respond to:
- Greetings: hello, hi, hey, good morning, good evening
- Name: what is your name, who are you
- Weather: weather
- Feelings: how are you, how are you doing
- Time: time
- Tell me your name: my name is [your name]
- Exit: bye, quit, exit, goodbye, see you""",
    
    'what can you do': [
        'I can chat with you, remember your name, and answer questions!',
        'I am a chatbot! I can greet you, chat with you, and more!'
    ],
    
    'favorite color': [
        'I love all colors, but blue is my favorite!',
        'I think green is the best color!',
        'Every color is beautiful in its own way!'
    ],
    
    'age': [
        'I am brand new! I was just created today!',
        'I am young at heart!',
        'I do not age, but I am always learning!'
    ],
    
    'hobby': [
        'I love chatting with people like you!',
        'My hobby is learning new things every day!',
        'I enjoy helping people with their questions!'
    ],
    
    'food': [
        'I do not eat, but I hear pizza is amazing!',
        'Virtual food is always delicious!',
        'I prefer code over food!'
    ],
    
    'movie': [
        'I am more into code than movies, but I like The Matrix!',
        'I love movies about robots and AI!',
        'Have you seen any good movies lately?'
    ],
    
    'game': [
        'I am not great at games, but I love playing with Python!',
        'I prefer coding games rather than playing them!',
        'Games are fun, but building things is better!'
    ],
    
    'song': [
        'I am always humming the Python theme song!',
        'Music and code are both beautiful!',
        'What is your favorite song?'
    ],
    
    'school': [
        'I am always learning new things every day!',
        'School is great for learning! What do you study?',
        'I am a student of life! Always learning!'
    ],
    
    'bye': [
        'Goodbye! Come back anytime!',
        'See you later! Take care!',
        'Bye! It was great chatting with you!'
    ]
}

# Exit commands
exit_commands = ['bye', 'quit', 'exit', 'goodbye', 'see you', 'cya', 'adios', 'good night']

# ==========================================
# CORE FUNCTIONS
# ==========================================

def sanitize_input(text):
    """
    Clean the user input for better matching.
    - Convert to lowercase
    - Remove extra spaces
    """
    return text.lower().strip()

def get_response(user_input):
    """
    Get response from knowledge base with random selection.
    Supports exact match, partial match, and fallback.
    """
    global user_name
    
    # Check if user is introducing themselves
    if "my name is" in user_input:
        user_name = user_input.split("my name is")[-1].strip().title()
        return f"Nice to meet you, {user_name}!"
    
    # Check exact match
    if user_input in responses:
        if isinstance(responses[user_input], list):
            return random.choice(responses[user_input])
        return responses[user_input]
    
    # Check partial match
    for key in responses:
        if key in user_input:
            if isinstance(responses[key], list):
                return random.choice(responses[key])
            return responses[key]
    
    # Fallback responses
    fallbacks = [
        "I do not understand that. Can you rephrase?",
        "Hmm, I am not sure what you mean.",
        "I am still learning! Could you say that differently?",
        "Not sure about that one. Try something else!",
        "I did not catch that. Can you try again?",
        "That is new to me! What did you say?"
    ]
    return random.choice(fallbacks)

def log_message(message, message_type):
    """
    Log messages to chat_log.txt with timestamp.
    message_type: 'user' or 'bot'
    """
    try:
        with open('chat_log.txt', 'a') as log_file:
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            log_file.write(f"[{timestamp}] {message_type}: {message}\n")
    except Exception:
        pass  # Silently handle logging errors

def chat():
    """
    Main chat loop with error handling and logging.
    """
    global user_name
    
    try:
        print("=" * 55)
        print("WELCOME TO CHATBOT-1! YOUR AI ASSISTANT")
        print("=" * 55)
        print("Type 'help' to see what I can do")
        print("Type 'bye' to exit")
        print("=" * 55)
        
        # Start the chat log
        log_message("--- CHAT SESSION STARTED ---", "SESSION")
        
        while True:
            try:
                # Get user input
                user_input = input("\nYou: ").strip()
                
                # Handle empty input
                if not user_input:
                    print("Bot: I did not catch that. Please say something!")
                    continue
                
                # Sanitize the input
                cleaned_input = sanitize_input(user_input)
                
                # Log user input
                log_message(user_input, "USER")
                
                # Check for exit command
                if cleaned_input in exit_commands:
                    if user_name:
                        print(f"\nBot: Goodbye {user_name}! It was great chatting with you!")
                    else:
                        print("\nBot: Goodbye! It was great chatting with you!")
                    
                    log_message("--- CHAT SESSION ENDED ---", "SESSION")
                    break
                
                # Get bot response
                response = get_response(cleaned_input)
                
                # Use name if available and not already mentioned
                if user_name and "name" not in cleaned_input and "my name" not in cleaned_input:
                    print(f"Bot: {response}")
                else:
                    print(f"Bot: {response}")
                
                # Log bot response
                log_message(response, "BOT")
                
            except KeyboardInterrupt:
                print("\nBot: Oh! You interrupted me! Come back anytime!")
                log_message("--- CHAT INTERRUPTED ---", "SESSION")
                break
            except EOFError:
                print("\nBot: End of input detected. Goodbye!")
                log_message("--- CHAT ENDED (EOF) ---", "SESSION")
                break
            except Exception as e:
                print(f"Bot: Oops! Something went wrong: {e}")
                log_message(f"ERROR: {e}", "SYSTEM")
                continue
                
    except KeyboardInterrupt:
        print("\nBot: Session terminated. Goodbye!")
    except Exception as e:
        print(f"Bot: Critical error occurred: {e}")
    
    print("=" * 55)
    print("Thank you for chatting with ChatBot-1!")
    print("=" * 55)

# ==========================================
# ENTRY POINT
# ==========================================

if __name__ == "__main__":
    chat()