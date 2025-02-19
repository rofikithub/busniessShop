import os
import langid
import playsound
from gtts import gTTS
from langdetect import detect
import speech_recognition as sr
from googlesearch import search
from easygoogletranslate import EasyGoogleTranslate


from controller.ProductController import ProductController


recognizer = sr.Recognizer()
class VoiceController:
    def __init__(self):
        pass
    
    def google_translate(text,source,target):
        translator = EasyGoogleTranslate(
            source_language=source,
            target_language=target,
            timeout=10
        )
        return (translator.translate(text))
    
    def play(lan,text):
        if lan=="bn":
            toSpeak = gTTS(text=text, lang ='bn', slow = False)
        elif lan=="en":
            toSpeak = gTTS(text=text, lang ='en', slow = False)
        file = "audio.mp3"
        toSpeak.save(file)
        playsound.playsound(file, True)
        os.remove(file)
    
    def voice(self):
        if self.speek_image["toggle"]:
            self.speek_button.config(image=self.mp_of)
            self.speek_button.image = self.mp_of
            while True:
                with sr.Microphone() as source:
                    recognizer.adjust_for_ambient_noise(source=source)
                    audio = recognizer.listen(source)
                try:
                    self.language = detect(recognizer.recognize_google(audio))
                    if self.language=="en":
                        text = recognizer.recognize_google(audio, language ='en-US')
                    else:
                        text = recognizer.recognize_google(audio, language ='bn-BD')
                except sr.UnknownValueError:
                    text = "Sorry, I can't hear you. Please say it again."
                except sr.RequestError as e:
                    text = "Your computer does not have an Internet connection."
                    
                if self.language=="en":
                    VoiceController.bangla_command(self,text)
                else:
                    VoiceController.bangla_command(self,text)
                break
        else:
            self.speek_button.config(image=self.mp_on)
            self.speek_button.image = self.mp_on
        self.speek_image["toggle"] = not self.speek_image["toggle"]
            
    def google_search(text):
        query = "পৃথিবীতে মোট জনসংখ্যা কত ?"
        for result in search(query, num_results=5, lang="bn", advanced=True, unique=True):
            print(result)
        
        
    def bangla_command(self,text):
        if text=="কে তুমি" or text=="তুমি কে" or text=="আপনি কে" or text=="কে আপনি":
            VoiceController.play("bn"," আমি বাণিজ্যের সচিব ।  ব্যবসার সকল হিসেব সংরক্ষণ করি ।")        
        elif text =="তোমার নাম কি" or text=="আপনার নাম কি" or text=="তোর নাম কি":
            VoiceController.play("bn"," আমার নাম বি, এম, এস ।  বিজনেস ম্যানেজমেন্ট সিস্টেম")
        elif text =="কখন থেকে যাত্রা শুরু" or text=="যাত্রা শুরু কবে" or text=="তোমার যাত্রা শুরু কবে" or text=="কখন যাত্রা শুরু করে":
            VoiceController.play("bn"," আমি একুশে ফেব্রুয়ারি ২০২৫ হইতে আমার যাত্রা শুরু করি। ")
        elif text =="আমাকে পণ্যের তালিকা দাও" or text=="পণ্যের তালিকা দেখি" or text=="মোট পণ্য" or text=="পণ্যের তালিকা" or text=="পণ্যের তালিকা দাও":
            VoiceController.play("bn"," জ্বী স্যার, পণ্যের তালিকা পিডিএফ ফরমেটে ওপেন করে দিচ্ছি ।")
            ProductController.print(self)