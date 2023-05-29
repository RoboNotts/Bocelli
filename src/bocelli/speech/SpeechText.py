import speech_recognition as sr
from gtts import gTTS
from tempfile import TemporaryFile
from pygame import mixer
import pyaudio
from time import sleep

# APPROXIMATE READING TIME
def speakDuration(text):
    words = text.split()
    reading_speed = 175 # words per minute
    reading_time = len(words) / reading_speed
    extra_time = 5
    sleep_time = reading_time + extra_time
    return sleep_time

# Provides speaking and listening services
class Speaker:
    
    def __init__(self, micName = ""):
        self.r = sr.Recognizer()
        if micName != "":
            try:
                print(sr.Microphone.list_microphone_names())
                index = sr.Microphone.list_microphone_names().index(micName)
                self.mic = sr.Microphone(index)
                self.adjustMicrophone(3)
                return
                
            except ValueError:
                print("Specified Mic not found. Defaulting...")
                
        self.mic = sr.Microphone()
        self.adjustMicrophone(3)


    # Uses text-to-speech to say something
    def speak(self, text):
        tts = gTTS(text, lang='en', tld='co.uk')
        mixer.init()
        while mixer.music.get_busy() == True:
            continue
        sf = TemporaryFile()
        tts.write_to_fp(sf)
        sf.seek(0)
        mixer.music.load(sf)
        mixer.music.play()

        sleeptime=speakDuration(text)
        sleep(sleeptime)

    def adjustMicrophone(self, dur):
        self.speak("Please give me a moment.")
        with self.mic as source:
            self.r.adjust_for_ambient_noise(source, duration=dur)
        self.speak("Microphone Adjustment Complete")
        
    # Listens for a set amount of time, and returns what was said to it.
    def listen(self, dur):
        with self.mic as source:
            print("")
            print("listening") #prints
            audio = self.r.listen(source)
            try:
                text = self.r.recognize_google(audio, language='en-GB')
                if text == []:
                    raise Exception
            except Exception as e:
                print("There was an error while listening. Try again")
                text = "?"
            
        return text

    def test(self):
        self.speak(f"Testing testing")
        sleep(0.1)

# Testing
if __name__ == "__main__":
    try:
        test = Speaker()
        test.test()
    except Exception as e:
        print(e)
