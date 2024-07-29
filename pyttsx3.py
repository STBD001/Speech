import pyttsx3

def speak_with_pyttsx3(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)  # speech speed
    for voice in engine.getProperty('voices'):
        if 'pl' in voice.languages:
            engine.setProperty('voice', voice.id)
            break
    engine.say(text)
    engine.runAndWait()
