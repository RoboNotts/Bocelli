import speech_recognition as sr
import pyttsx3

class Speaker:
    
    def __init__(self):
        self.r = sr.Recognizer()
        self.engine = pyttsx3.init() 
        voices = self.engine.getProperty("voices") 
        self.engine.setProperty("voice", voices[1].id) 

    def Speak(self, command):
        self.engine.say(command)
        self.engine.runAndWait()
        
    def Listen(self, dur):
        with sr.Microphone() as source:
            self.Speak("Please give me a moment.")
            self.r.adjust_for_ambient_noise(source, duration=dur)
            self.Speak("Okay, tell me what you're doing please.")
            print("listening") #prints
            audio = self.r.listen(source)
            text = self.r.recognize_google(audio)
        return text
        
if __name__ == "__main__":
    try:
        test = Speaker()
        print(test.Listen(5))
    except Exception as e:
        print(e)
