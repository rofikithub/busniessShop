import os
import langid
import playsound
from gtts import gTTS
from langdetect import detect
import speech_recognition as sr
from googlesearch import search
from easygoogletranslate import EasyGoogleTranslate


from controller.CustomerController import CustomerController
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
        file = os.path.abspath(os.path.expanduser( '~' )+"\\AppData\\Local\\BMS\\audio.mp3")
        toSpeak.save(file)
        playsound.playsound(file, True)
        os.remove(file)
    
    def voice(self):
        if self.speek_image["toggle"]:
            self.speek_button.config(image=self.mp_of)
            self.speek_button.image = self.mp_of
            i=0
            while True:
                with sr.Microphone() as source:
                    recognizer.adjust_for_ambient_noise(source=source)
                    audio = recognizer.listen(source)
                try:
                    self.language = detect(recognizer.recognize_google(audio))
                    if self.language=="en":
                        text = recognizer.recognize_google(audio, language ='en-US')
                        VoiceController.english_command(self,text)
                    else:
                        text = recognizer.recognize_google(audio, language ='bn-BD')
                        VoiceController.bangla_command(self,text)
                except sr.UnknownValueError:
                    if i>=2:
                        break
                    else:
                        VoiceController.play("bn","দুঃখিত, আমি আপনার কথা শুনতে পারিনি।")
                except sr.RequestError as e:
                    VoiceController.play("bn","দুঃখিত, আপনার কম্পিউটারে ইন্টানেট সংযোগ নেই।")
                    break
                i=i+1
        else:
            self.speek_button.config(image=self.mp_on)
            self.speek_button.image = self.mp_on
        self.speek_image["toggle"] = not self.speek_image["toggle"]
            
    def google_search(text):
        query = "পৃথিবীতে মোট জনসংখ্যা কত ?"
        for result in search(query, num_results=5, lang="bn", advanced=True, unique=True):
            print(result)
        
        
    def bangla_command(self,text):
        if text=="আসসালামু ওয়ালাইকুম" or text=="আসসালামুয়ালাইকুম":
            VoiceController.play("bn","ওয়ালাইকুম আসসালাম, ওয়ারাহমাতুল্লাহি ওয়াবারাকাতুহ।")  
        elif text=="কে তুমি" or text=="তুমি কে" or text=="আপনি কে" or text=="কে আপনি" or text=="কে":
            VoiceController.play("bn"," আমি বাণিজ্যের সচিব ।  ব্যবসার সকল হিসেব সংরক্ষণ করি ।")        
        elif text =="তোমার নাম কি" or text=="আপনার নাম কি" or text=="তোর নাম কি" or text=="নাম কি":
            VoiceController.play("bn"," আমার নাম বি, এম, এস ।  বিজনেস ম্যানেজমেন্ট সিস্টেম")        
        elif text =="কাজ কি" or text=="আপনার কাজ কি" or text=="তোমার কাজ কি" or text=="আপনি কি করেন":
            VoiceController.play("bn","আমি আপনার ব্যবসার সকল হিসেব সংরক্ষণ করি ।")        
        elif text =="কেন তৈরি করা হলো" or text=="আপনাকে কেন তৈরি করা হলো" or text=="তোমাকে কেন তৈরি করা হলো" or text=="কেন তোমাকে তৈরি করল" or text=="তোমাকে কেন তৈরি করল":
            VoiceController.play("bn","আমাকে আপনার ব্যবসার সকল হিসেব সংরক্ষণ করার জন্য তৈরি করা হয়েছে ।")
        elif text =="কখন থেকে যাত্রা শুরু" or text=="যাত্রা শুরু কখন" or text=="যাত্রা শুরু কবে" or text=="কখন যাত্রা শুরু করে" or text=="কবে থেকে":
            VoiceController.play("bn"," আমি একুশে ফেব্রুয়ারি ২০২৫ হইতে আমার যাত্রা শুরু করি। ")
        elif text =="কে তৈরি করেছে" or text=="তোমার সৃষ্টিকর্তা কে" or text=="কে বানাল" or text=="কার তৈরি" or text=="কে তোমাকে বানাল" or text=="কে তোমাকে তৈরি":
            VoiceController.play("bn"," আমাকে তৈরি করেছে, জনাব, রফিক তালুকদার, তিনি আমার সৃষ্টিকর্তা । মোবাইল নাম্বার, ০১৭৩৭,০৩,৪৩,৩৮ ।")
        elif text =="পণ্যের তালিকা" or text=="প্রডাক্ট লিস্ট" or text=="মোট পণ্য" or text=="প্রডাক্ট সমূহ":
            ProductController.print(self)
            VoiceController.play("bn","স্যার, পণ্যের তালিকা তৈরি করেছি।")
        elif text =="গ্রাহকের তালিকা" or text=="কাস্টমার লিস্ট" or text=="মোট গ্রাহক" or text=="গ্রাহক সমূহ":
            CustomerController.print(self)
            VoiceController.play("bn","স্যার, গ্রাহকের তালিকা তৈরি করেছি।")
        print(text)
        
        
        
    def english_command(self,text):
        print(text)
        VoiceController.play("en",text)