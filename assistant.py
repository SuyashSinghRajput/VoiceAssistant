from core.speech import listen, speak
from core.commands import handle_command

def main():
    speak("Hello sir i am JARVIS your Assistant. Say something!")
    while True:
        cmd = listen()
        if not cmd:
            continue
        if "stop" in cmd:
            speak("Goodbye!")
            break
        handle_command(cmd)

if __name__ == "__main__":
    main()
