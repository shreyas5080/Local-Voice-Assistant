import pyttsx3
import os
from src.ear import listen_and_transcribe
from src.brain import ask_brain

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 175)


def speak(text):
    print(f"🤖 AI: {text}")
    engine.say(text)
    engine.runAndWait()


def main():
    speak("System online. Hello Shreyas, I am listening.")

    try:
        while True:
            user_input = listen_and_transcribe()

            if user_input:
                print(f"👤 You: {user_input}")
                if any(word in user_input.lower() for word in ["exit", "stop", "goodbye"]):
                    speak("Shutting down. Goodnight, bro!")
                    break

                response = ask_brain(user_input)
                speak(response)
            else:
                print("... (Listening) ...")

    except KeyboardInterrupt:
        print("\nProgram stopped by user.")


if __name__ == "__main__":
    main()