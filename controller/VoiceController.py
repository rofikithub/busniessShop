import speech_recognition as sr

recognizer = sr.Recognizer()


class VoiceController:
    def __init__(self):
        pass
    
    def voice(self):
        end = False
        while not end:
            audio = VoiceController.capture_voice_input()
            text  = VoiceController.convert_voice_to_text(audio)
            end   = VoiceController.process_voice_command(text)
        
        
    def capture_voice_input():
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source=source)
            audio = recognizer.listen(source)
        return audio


    def convert_voice_to_text(audio):
        try:
            text = recognizer.recognize_google(audio)
        except sr.UnknownValueError:
            text = ""
            print("Sorry, I didn't understand that.")
        except sr.RequestError as e:
            text = ""
            print("Error; {0}".format(e))
        return text


    def process_voice_command(text):
        if "hello system" in text.lower():
            print("Hello! How can I help you?")
            return True
        elif "goodbye system" in text.lower():
            print("Goodbye! Have a great day!")
            return True
        else:
            print("Please try again...")
        return False            
                