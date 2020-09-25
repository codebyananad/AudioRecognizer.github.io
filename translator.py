from googletrans import Translator
import speech_recognition as sr
import pyaudio
import pyttsx3


r = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices') 
engine.setProperty('voice', voices[0].id)


audioFile = sr.AudioFile('test4.wav')


with audioFile as source:
    text = r.record(source)
    
try:    
    print("\nYou said: " + r.recognize_google(text))
    engine.say(r.recognize_google(text))
    engine.runAndWait()
except Exception as e:
    print(e)

translator = Translator()

destText = translator.translate(r.recognize_google(text),dest='hi')
translated = destText.text
pronounce = destText.pronunciation

#print(destText)
print("Translated: " + translated)
engine.say(pronounce)

engine.runAndWait()

engine.stop()
              

