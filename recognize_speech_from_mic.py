import speech_recognition as sr

def recognize_speech_from_mic():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("I'm listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognition...")
        text = recognizer.recognize_google_cloud(audio, language='pl-PL')
        print(f"Recognized text: {text}")
        return text
    except sr.UnknownValueError:
        print("Speech recognition failed")
        return None
    except sr.RequestError:
        print("Error connecting to the speech recognition server")
        return None
