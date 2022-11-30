import speech_recognition as sr
import pyttsx3
from time import sleep as zzz

# Provides speaking and listening services
class Speaker:
    
    def __init__(self):
        self.r = sr.Recognizer()
        self.engine = pyttsx3.init()
        voices = self.engine.getProperty("voices") 
        self.engine.setProperty("voice", voices[14].id) 
        self.engine.setProperty("rate", 110)
        self.engine.setProperty("volume", 2)

    # Uses text-to-speech to say something
    def Speak(self, command):
        self.engine.say(command)
        self.engine.runAndWait()
        
    # Listens for a set amount of time, and returns what was said to it.
    def Listen(self, dur):
        with sr.Microphone() as source:
            self.Speak("Please give me a moment.")
            self.r.adjust_for_ambient_noise(source, duration=dur)
            self.Speak("Okay, tell me what you're doing please.") # Temporary addition for METRICS
            print("listening") #prints
            audio = self.r.listen(source)
            text = self.r.recognize_google(audio)
        return text

    def test(self):
        for i in range(19, 50):
            self.engine.setProperty("rate", 130)
            voices = self.engine.getProperty("voices") 
            self.engine.setProperty("voice", voices[i].id) 
            self.Speak(f"This is voice {i}. Testing testing")
            zzz(0.1)

# Testing
if __name__ == "__main__":
    try:
        test = Speaker()
        print(test.test())
    except Exception as e:
        print(e)
