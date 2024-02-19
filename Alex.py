import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os

class Alexa:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.engine = pyttsx3.init()

    def speak(self, text):
        """Function to convert text to speech"""
        self.engine.say(text)
        self.engine.runAndWait()

    def listen(self):
        """Function to listen for voice commands"""
        with sr.Microphone() as source:
            print("Listening...")
            self.recognizer.adjust_for_ambient_noise(source)
            audio = self.recognizer.listen(source)

        try:
            print("Recognizing...")
            command = self.recognizer.recognize_google(audio).lower()
            print("You said:", command)
            return command
        except sr.UnknownValueError:
            print("Sorry, I didn't catch that. Please try again.")
            return ""
        except sr.RequestError:
            print("Sorry, there was an error with the speech recognition service.")
            return ""

    def greet(self):
        """Function to greet the user"""
        hour = datetime.datetime.now().hour
        if 0 <= hour < 12:
            self.speak("Good morning!")
        elif 12 <= hour < 18:
            self.speak("Good afternoon!")
        else:
            self.speak("Good evening!")

    def tell_time(self):
        """Function to tell the current time"""
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        self.speak(f"The current time is {current_time}.")

    def search_wikipedia(self, query):
        """Function to search Wikipedia"""
        try:
            summary = wikipedia.summary(query, sentences=2)
            self.speak(summary)
        except wikipedia.exceptions.PageError:
            self.speak("Sorry, I couldn't find any information on that topic.")
        except wikipedia.exceptions.DisambiguationError:
            self.speak("There are multiple results for that query. Please be more specific.")

    def open_website(self, website):
        """Function to open a website"""
        webbrowser.open(f"https://www.{website}.com")
        self.speak(f"Opening {website} in your web browser.")

    def play_music(self):
        """Function to play music"""
        music_dir = "C:\\Users\\YourUsername\\Music"  # Change this to your music directory
        songs = os.listdir(music_dir)
        if songs:
            os.startfile(os.path.join(music_dir, songs[0]))
        else:
            self.speak("Sorry, I couldn't find any music in your music directory.")

    def run(self):
        """Function to run the Alexa virtual assistant"""
        self.greet()
        self.speak("I'm Alexa. How can I help you?")

        while True:
            user_input = self.listen()

            if "bye" in user_input:
                self.speak("Goodbye! Have a great day!")
                break
            elif "time's the time now" in user_input:
                self.tell_time()
            elif "search" in user_input:
                query = user_input.replace("search", "").strip()
                self.search_wikipedia(query)
            elif "open website" in user_input:
                website = user_input.replace("open website", "").strip()
                self.open_website(website)
            elif "play music" in user_input:
                self.play_music()
            else:
                self.speak("Sorry, I didn't understand that. Can you please repeat?")

if __name__ == "__main__":
    alexa = Alexa()
    alexa.run()
