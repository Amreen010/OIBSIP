import speech_recognition as sr
import pyttsx3

# Initialize recognizer and speech engine
listener = sr.Recognizer()
engine = pyttsx3.init()

# Set voice to female or male
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # [0]=male, [1]=female

def talk(text):
    """Speak out the text"""
    engine.say(text)
    engine.runAndWait()

def take_command():
    """Listen to user voice and return as text"""
    try:
        with sr.Microphone() as source:
            print("🎙 Listening...")
            audio = listener.listen(source)
            command = listener.recognize_google(audio)
            command = command.lower()
            print("You said:", command)
            return command
    except:
        return ""

def run_assistant():
    talk("Hello! I am your simple voice assistant. How can I help you?")
    while True:
        command = take_command()

        if 'hello' in command:
            talk("Hi there! How are you?")
        elif 'your name' in command:
            talk("I am your Python voice assistant.")
        elif 'time' in command:
            from datetime import datetime
            time = datetime.now().strftime('%I:%M %p')
            talk(f"The time is {time}")
        elif 'stop' in command or 'exit' in command or 'bye' in command:
            talk("Goodbye! Have a nice day!")
            break
        elif command != "":
            talk("Sorry, I didn't understand that.")
        else:
            talk("Please say something.")

# Run the assistant
run_assistant() 