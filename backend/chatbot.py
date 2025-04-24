import difflib  # Ensure difflib is imported
from difflib import get_close_matches

def get_response(user_input):
    """
    Improved chatbot that recognizes variations of user input
    using fuzzy matching.
    """
    user_input = user_input.lower().strip()

    responses = {
        "who are you": "I am your personal chatbot!",
        "what is your name": "I am Chatbot, your virtual assistant!",
        "what can you do": "I can chat with you and answer questions about myself!",
        "how are you": "I'm just a bot, but I'm feeling great! How about you?",
        "where do you live": "I live in the cloud, always here to assist you!",
        "who created you": "I was created by a developer who wanted to make chatting fun!",
        "are you human": "No, I am just a chatbot, but I try to be as helpful as possible!",
        "can you learn": "I don't learn on my own, but my creator can update me to be smarter!",
        "what is your purpose": "My purpose is to chat with you and answer your questions!",
        "hello": "Hello! How can I assist you today?",
        "hi": "Hi there! What can I do for you?",
        "bye": "Goodbye! Have a great day!",
        "thank you": "You're welcome! Happy to help!"
    }

    # Find the closest matching question
    matches = get_close_matches(user_input, responses.keys(), n=1, cutoff=0.6)

    if matches:
        return responses[matches[0]]

    return "I'm not sure about that. Can you ask me something else?"

# If run directly, start a test chat in the terminal
if __name__ == "__main__":
    print("Chatbot: Hello! Ask me anything about myself. Type 'exit' to stop.")

    while True:
        user_message = input("You: ").strip()

        if user_message.lower() == "exit":
            print("Chatbot: Goodbye!")
            break

        print("Chatbot:", get_response(user_message))
