from recognize_speech_from_mic import recognize_speech_from_mic
from speak_with_gtts import speak_with_gtts
from pyttsx3 import speak_with_pyttsx3
from sipmle_task import open_website, get_weather

def main():
    while True:
        command = recognize_speech_from_mic()

        if command is None:
            continue

        if 'pogoda' in command:
            city = "Kielce"
            weather_info = get_weather(city)
            speak_with_pyttsx3(weather_info)

        elif "otwórz stronę" in command:
            open_website('https://www.instagram.com/wojciechowski_stefan/')
            speak_with_pyttsx3("Otwieram twojego Instagrama")

        elif "koniec" in command or "zakończ" in command:
            speak_with_pyttsx3("Kończę pracę")
            break

        else:
            speak_with_pyttsx3("Nie rozumiem polecenia, spróbuj ponownie")

if __name__ == "__main__":
    main()
