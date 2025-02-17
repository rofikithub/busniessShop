import speech_recognition as sr

recognizer = sr.Recognizer()


class VoiceController:
    def __init__(self):
        pass
    
    def key(text):
        key ="mobile number"
        if key in text:
            print(text)
    
    def getVoice(self):
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source=source)
            try:
                audio = recognizer.listen(source)
                text = recognizer.recognize_google(audio)
                VoiceController.key(text)
            except sr.UnknownValueError:
                print("Please speak again.")
            except sr.RequestError:
                print("Check your internet connection.")