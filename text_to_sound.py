# !pip install pyttsx3
import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    engine.setProperty("rate", 170) #konuşma hızı
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[64].id) #Türkçe
    engine.say(text)
    engine.runAndWait()


if __name__ == "__main__":
    my_text = "are you good at coding"
    speak(my_text)
