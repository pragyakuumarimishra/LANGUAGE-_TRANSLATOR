import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
import os

# Supported languages and their corresponding language codes
languages = {'english': 'en', 'hindi': 'hi'}

def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source, timeout=600)  # Setting timeout to 10 minutes (600 seconds)
    try:
        text = recognizer.recognize_google(audio, language='en')
        print("You said:", text)
        return text
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand what you said.") 
        return None
    except sr.RequestError:
        print("Sorry, I couldn't request results from Google Speech Recognition service.")
        return None


def translate_text(text, target_language='hi'):
    translator = Translator()
    try:
        translated_text = translator.translate(text, dest=target_language).text
        return translated_text
    except Exception as e:
        print("Translation failed. Error:", e)
        return None


def text_to_speech(text, language='hi'):
    tts = gTTS(text=text, lang=language)
    tts.save("translated_audio.mp3")
    os.system("start translated_audio.mp3")

def main():
    while True:
        input_text = recognize_speech()
        if input_text:
            # Check if input text is in English and not longer than 10 minutes
            if len(input_text) > 10 * 60:  # Check if text length exceeds 10 minutes in seconds
                print("Input text exceeds 10 minutes. Please speak shorter sentences.")
                continue
            target_language = 'hindi'
            translated_text = translate_text(input_text, target_language)
            print("Translated text:", translated_text)
            text_to_speech(translated_text, language='hi')

if __name__ == "__main__":
    main()
