import nltk
from nltk.chat.util import Chat, reflections

# Download NLTK resources
nltk.download("punkt")

# Pattern-response pairs for the chatbot
pairs = [
    [
        r"hi|hello|hey",
        ["Hello!", "Hey there!", "Hi! How can I assist you today?"]
    ],
    [
        r"what is your name ?",
        ["I'm ChatBot, your virtual assistant."]
    ],
    [
        r"how are you ?",
        ["I'm doing great, thank you! How can I help you today?"]
    ],
    [
        r"what can you do ?",
        ["I can answer simple questions and chat with you. Try asking about time, help, or saying hi!"]
    ],
    [
        r"(.*) your name ?",
        ["You can call me ChatBot."]
    ],
    [
        r"(.*) help (.*)",
        ["Sure! I'm here to assist. Please let me know your question."]
    ],
    [
        r"(.*) (weather|temperature) (.*)",
        ["I'm not connected to real-time weather right now, but I can help you use APIs like OpenWeatherMap!"]
    ],
    [
        r"(.*) (time|date)",
        ["Try using Python's datetime module to get current time and date! Want help with that?"]
    ],
    [
        r"(.*) (thank you|thanks)",
        ["You're welcome!", "Happy to help :)"]
    ],
    [
        r"bye|exit|quit",
        ["Goodbye! Have a wonderful day!", "See you soon!"]
    ],
    [
        r"(.*)",
        ["I'm not sure how to respond to that. Try asking something else!"]
    ]
]

# Create and start the chatbot
def run_chatbot():
    print("🤖 ChatBot: Hello! Type 'exit' or 'quit' to end the chat.\n")
    chatbot = Chat(pairs, reflections)
    chatbot.converse()

if __name__ == "__main__":
    run_chatbot()
