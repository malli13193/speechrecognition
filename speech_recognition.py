#1.speech_recognition 
#pip install SpeechRecognition
#pip install pyaudio

import speech_recognition as sr

def main():
    r = sr.Recognizer()
    audio = None

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Please say something")
        print("Recognizing now...")
        audio = r.listen(source)

    return r.recognize_google(audio)

while True:
    print(main())
