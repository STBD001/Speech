from gtts import gTTS
import os

def speak_with_gtts(text):
    tts = gTTS(text=text, lang='pl')
    tts.save("response.mp3")
    os.system("start response.mp3")
