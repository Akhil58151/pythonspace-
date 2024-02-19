# Import statements remain the same as before

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

    def get_weather(self):
        """Function to get weather information"""
        api_key = "your_api_key"  # Replace with your OpenWeatherMap API key
        city = "New York"  # Replace with the desired city
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        response = requests.get(url)
        data = response.json()
        temperature = data["main"]["temp"]
        description = data["weather"][0]["description"]
        self.speak(f"The current temperature in {city} is {temperature} degrees Celsius with {description}.")

    def get_news(self):
        """Function to get news headlines"""
        api_key = "your_api_key"  # Replace with your News API key
        url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}"
        response = requests.get(url)
        data = response.json()
        articles = data["articles"]
        self.speak("Here are the latest news headlines:")
        for article in articles:
            title = article["title"]
            self.speak(title)

    def set_reminder(self, task, time):
        """Function to set a reminder"""
        # Implement reminder functionality based on your requirements
        pass

    def calculate(self, expression):
        """Function to perform basic calculations"""
        try:
            result = eval(expression)
            self.speak(f"The result of {expression} is {result}.")
        except Exception as e:
            self.speak("Sorry, I couldn't perform the calculation.")

    def tell_joke(self):
        """Function to tell a random joke"""
        jokes = [
            "Why don't scientists trust atoms? Because they make up everything!",
            "Did you hear about the mathematician who's afraid of negative numbers? He'll stop at nothing to avoid them!",
            "Why did the scarecrow win an award? Because he was outstanding in his field!"
        ]
        joke = random.choice(jokes)
        self.speak(joke)

    def open_application(self, application):
        """Function to open an application"""
        # Implement application opening based on your system and available applications
        pass

    def translate_text(self, text, target_language):
        """Function to translate text"""
        # Implement text translation using a translation API
        pass

    def tell_story(self):
        """Function to tell a story"""
        # Implement storytelling functionality, e.g., narrate a short story or fun fact
        pass

    def run(self):
        """Function to run the Alexa virtual assistant"""
        self.greet()
        self.speak("I'm Alexa. How can I help you?")

        while True:
            user_input = self.listen()

            if "bye" in user_input:
                self.speak("Goodbye! Have a great day!")
                break
            elif "time" in user_input:
                self.tell_time()
            elif "weather" in user_input:
                self.get_weather()
            elif "news" in user_input:
                self.get_news()
            elif "reminder" in user_input:
                # Extract task and time from user_input and call set_reminder() function
                pass
            elif "calculate" in user_input:
                expression = user_input
