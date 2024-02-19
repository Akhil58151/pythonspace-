import random

class SimpleChatbot:
    def __init__(self):
        self.responses = {
            "hi": ["Hello!", "Hi there!", "Hey!"],
            "how are you": ["I'm doing well, thank you!", "I'm great, thanks for asking!"],
            "bye": ["Goodbye!", "See you later!", "Bye!"],
            "what's your name": ["I'm just a simple chatbot.", "You can call me Chatbot!"],
            "tell me a joke": ["Why don't scientists trust atoms? Because they make up everything!",
                               "Did you hear about the mathematician who's afraid of negative numbers? He'll stop at nothing to avoid them!",
                               "Why did the scarecrow win an award? Because he was outstanding in his field!"]
        }

        self.questions = {
            "what is your favorite color": "I'm just a chatbot, so I don't have a favorite color!",
            "what is the meaning of life": "The meaning of life is a philosophical question. Different people may have different answers."
        }

        self.recommendations = {
            "movie": ["You should watch 'The Shawshank Redemption'. It's a classic!",
                      "I recommend 'Inception'. It's mind-bending!",
                      "Check out 'The Godfather'. It's a must-watch!"]
        }

    def respond(self, message):
        message = message.lower()
        if message in self.responses:
            return random.choice(self.responses[message])
        elif message in self.questions:
            return self.questions[message]
        elif "recommend" in message:
            topic = message.split()[-1]
            if topic in self.recommendations:
                return random.choice(self.recommendations[topic])
            else:
                return "Sorry, I don't have any recommendations for that."
        else:
            return "I'm sorry, I don't understand."

if __name__ == "__main__":
    chatbot = SimpleChatbot()
    print("AI: Hello! How can I help you?")

    while True:
        user_input = input("You: ")
        response = chatbot.respond(user_input)
        print("AI:", response)

        if user_input.lower() == "bye":
            break
