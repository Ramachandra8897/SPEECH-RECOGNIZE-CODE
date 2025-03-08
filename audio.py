#speech_recognition → Used to capture and recognize voice commands.
#webbrowser → Used to open YouTube in the web browser.

import speech_recognition as sr
import webbrowser

# sr.Recognizer() → Creates a speech recognition object.
# sr.Microphone() → Captures audio from the microphone.
# recognizer.adjust_for_ambient_noise(source) → Reduces background noise for better accuracy.
# User Prompt: Prints "Listening..." so the user knows when to speak.



def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening... Say 'Alexa, open YouTube'")
        recognizer.adjust_for_ambient_noise(source)  # Reduce background noise
#        recognizer.listen(source, timeout=5) → Listens for voice input for 5 seconds.
# recognizer.recognize_google(audio).lower() → Converts speech to text using Google Speech Recognition.
# .lower() → Converts the text to lowercase for better matching.

        try:
            audio = recognizer.listen(source, timeout=5)  # Listen for 5 seconds
            command = recognizer.recognize_google(audio).lower()
            print("You said:", command)
            return command
        
# sr.UnknownValueError → If speech is unclear or not recognized, it prints an error message.
# sr.RequestError → If there's an internet issue, it prints an error message.


        except sr.UnknownValueError:
            print("Sorry, I could not understand.")
            return ""
        except sr.RequestError:
            print("Could not request results, check your internet connection.")
            return ""

# Checks if "Alexa" and "open YouTube" are in the recognized speech.
# If the command is detected, it opens YouTube in the web browser.


def execute_command(command):
    if "alexa" in command and "open youtube" in command:
        print("Opening YouTube...")
        webbrowser.open("https://www.youtube.com")


# if __name__ == "__main__": → Ensures the script runs only when executed directly.
# Calls recognize_speech() to listen to voice input.
# Calls execute_command(command) to process and execute the command.

if __name__ == "__main__":
    command = recognize_speech()
    execute_command(command)
