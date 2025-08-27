import webbrowser
from core.speech import speak
import subprocess
import os


apps = {
    "Github": r"C:\Users\rajpu\AppData\Local\GitHubDesktop\GitHubDesktop.exe",
    "Notepad": "notepad.exe"
}

def handle_command(command):
    if "open browser" in command:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")
    elif "youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")
    elif "open" in command:
        command = command.lower()
        for app in apps:
            if app.lower() in command:
                subprocess.Popen(apps[app])
                speak("Opening Github Sir")
                return
            speak("Can't Find the App")
            

    else:
        speak("Sorry, I don't know how to do that yet.")
