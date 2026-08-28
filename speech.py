import speech_recognition as sr
recognizer=sr.Recognizer()
def listen():
    with sr.Microphone() as source:
        print("Listening")
        recognizer.adjust_for_ambient_noise(source,duration=1)
        try:
            audio=recognizer.listen(source,timeout=10,phrase_time_limit=5)
            text=recognizer.recognize_google(audio,language="en-IN")
            print("You:",text)
            return text.lower()
        except sr.WaitTimeoutError:
            print("NO speech detected.")
            return""
        except sr.UnknownValueError:
            print("Sorry,I couldn't understand.")
            return""
        except sr.RequestError:
            print("Internet error.")
            return""
