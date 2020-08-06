'''
Created on Jun 10, 2020

@author: Sumit
'''
import speech_recognition as sr

# obtain audio from the microphone

r = sr.Recognizer()
r.energy_threshold=650
r.dynamic_energy_threshold=False
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)
try:
    print("Sphinx thinks you said " + r.recognize_google(audio))
except sr.UnknownValueError:
    print("Sphinx could not understand audio")
except sr.RequestError as e:
    print("Sphinx error; {0}".format(e))