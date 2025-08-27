from core.speech import listen, speak
from core.commands import handle_command
import keyboard

def main():
    speak("Say 'Jarvis' to wake me up, or press ESC to exit.")
    
    while True:
        if keyboard.is_pressed("esc"):
            speak("Goodbye Sir")
            print("Exiting Code")
            break

        cmd = listen()
        if not cmd:
            continue
        cmd = cmd.lower()

        if "jarvis" in cmd:
            speak("Hello sir, I am JARVIS your assistant. What should I do?")
            
            while True:
                sub_cmd = listen()
                if not sub_cmd:
                    continue
                sub_cmd = sub_cmd.lower()

                if "stop" in sub_cmd:
                    speak("Goodbye!")
                    return

                handle_command(sub_cmd)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        speak("Goodbye Sir")
        print("Program stopped by user")
