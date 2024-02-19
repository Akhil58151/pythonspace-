import speech_recognition as sr
import pyttsx3

# Initialize the speech recognizer
recognizer = sr.Recognizer()

# Initialize the text-to-speech engine
engine = pyttsx3.init()


def speak(text):
    """Function to convert text to speech"""
    engine.say(text)
    engine.runAndWait()


def listen():
    """Function to listen for voice commands"""
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        command = recognizer.recognize_google(audio).lower()
        print("You said:", command)
        return command
    except sr.UnknownValueError:
        print("Sorry, I didn't catch that. Please try again.")
        return ""
    except sr.RequestError:
        print("Sorry, there was an error with the speech recognition service.")
        return ""


def alexa():
    """Function to simulate Alexa functionality"""
    speak("Hello! How can I help you?")

    while True:
        command = listen()

        if "hello" in command:
            speak("Hello! How are you?")
        elif "how are you" in command:
            speak("I'm doing well, thank you for asking!")
        elif "what time is it" in command:
            speak("I'm sorry, I cannot tell the time.")
        elif "bye" in command or "goodbye" in command:
            speak("Goodbye! Have a great day!")
            break
        else:
            speak("Sorry, I don't understand that command.")


if __name__ == "__main__":
    alexa()
