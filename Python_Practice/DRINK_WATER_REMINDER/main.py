import pyttsx3
import time
from plyer import notification

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

while True:
    notification.notify(
        title = "Drink Water",
        message = "Take a few sips of water now",
        timeout = 60*30
        )

    
    speak("Drink Water PLease")

    time.sleep(60 * 30)
    

    


