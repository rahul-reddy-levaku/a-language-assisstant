import speech_recognition as sr
from googletrans import Translator

# initialise translator 
translator = Translator()


# function to recognize speech translate
def recognize_and_translate():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening Speak now!")
        try:
            # Capture audio input
            audio = recognizer.listen(source)
            print("recognizing.")
            text = recognizer.recognize_google(audio)
            print(f"You said: {text}")

            # Translate text
            target_language = input("Enter target language code (e.g., 'telugu' or 'hindi'): ")
            translation = translator.translate(text, dest=target_language)
            print(f"Translated ({target_language}): {translation.text}")
    
            
        except sr.UnknownValueError:
            print("Sorry, I couldn't understand audio.")
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    print("welcome to  RealTime Language Assistant")
    while True:
        recognize_and_translate()
        cont = input("Do you want to continue? (yes/no): ").strip().lower()
        if cont != "yes":
            print("bye")
            break
