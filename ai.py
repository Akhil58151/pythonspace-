import speech_recognition as sr
import pyttsx3


class SimpleAI:
    def __init__(self):
        self.responses = {
            "Hii": "Hello!",
            "how are you": "I'm doing well, thank you!",
            "bye": "Goodbye! Have a great day!"
        }

    def respond(self, message):
        message = message.lower()
        for pattern, response in self.responses.items():
            if pattern in message:
                return response
        return "I'm sorry, I don't understand that."


# Initialize the speech recognizer
recognizer = sr.Recognizer()

# Initialize the text-to-speech engine
engine = pyttsx3.init()


def speak(text):
    """Function to convert text to speech"""
    engine.say(text)
    engine.runAndWait()


# Create an instance of the SimpleAI class
ai = SimpleAI()

# Test the AI
print("AI: Hello! I'm a simple AI. Ask me anything or say 'bye' to exit.")

while True:
    try:
        with sr.Microphone() as source:
            print("Listening...")
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)

        print("Recognizing...")
        user_input = recognizer.recognize_google(audio)
        print("You:", user_input)

        if user_input.lower() == 'bye':
            speak("Goodbye! Have a great day!")
            break

        response = ai.respond(user_input)
        speak("AI: " + response)
        print("AI:", response)

    except sr.UnknownValueError:
        print("AI: Sorry, I didn't catch that. Please try again.")
        speak("Sorry, I didn't catch that. Please try again.")
    except sr.RequestError:
        print("AI: Sorry, there was an error with the speech recognition service.")
        speak("Sorry, there was an error with the speech recognition service.")