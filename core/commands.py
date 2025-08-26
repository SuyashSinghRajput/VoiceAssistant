import webbrowser
from core.speech import speak

def handle_command(command):
    if "open browser" in command:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")
    elif "youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")
    else:
        speak("Sorry, I don't know how to do that yet.")
