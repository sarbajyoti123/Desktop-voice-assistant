import wolframalpha
import pyttsx3;
import os
# import speech_recognition as sr
import webbrowser
import smtplib
import pyautogui
import os          
from chatterbot import ChatBot
import webbrowser
from chatterbot.trainers import ListTrainer
import cv2
import numpy as np
import time

import pyglet
from PyQt5 import QtGui
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QMainWindow,QPushButton,QTextEdit,QDialog,QVBoxLayout
from PyQt5.QtCore import Qt
import sys
class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = "JARVIS A.I(S.M)"        
        self.top = 100        
        self.left = 100        
        self.width = 350        
        self.height = 600
        self.InitWindow()
    def InitWindow(self):
        # vBox=QVBoxLayout()
        # self.textEdit=QTextEdit(self)
        # # self.textEdit.resize(200,200)
        # self.textEdit.setFont(QFont('Times',15))
        # vBox.addWidget(self.textEdit)
        self.button=QPushButton("START JARVIS",self)
        self.button.clicked.connect(self.sound)
        self.button.move(100,100)
        # vBox.addWidget(self.button)
        # self.setLayout(vBox)
        self.setWindowIcon(QtGui.QIcon("iron.png"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.show()
    def sound(self):
        def speak(audio):
            engine=pyttsx3.init();
            voices = engine.getProperty('voices')
            engine.setProperty('voice', voices[1].id)
            rate = engine.getProperty('rate')
            engine.setProperty('rate',150)
            engine.say(text=audio);
            engine.runAndWait();
        def mySpeech():
            global command
            r=sr.Recognizer()
            with sr.Microphone() as source:
                text=("i am ready sir")
                print(text)
                # self.textEdit.setText(text)
                r.pause_threshold = 1
                r.adjust_for_ambient_noise(source,duration=1)
                r.dynamic_energy_threshold = True
                audio=r.listen(source)
            try:
                command=r.recognize_google(audio)
                text=("you say"+command)
                print(text)
                # self.textEdit.setText(text)
            except sr.UnknownValueError:
                jarvis(mySpeech())
            return command
        def jarvis(Command):
            if command in 'talk':
                bot=ChatBot('Bot')
                bot.set_trainer(ListTrainer)
                while True:
                    # speak('hii sir')
                    content= mySpeech()
                    # message=input(content)

                    # if message.strip()!='bye':
                    a=bot.get_response(content)
                    speak( a )
                    if 'open YouTube' in content:
                        speak('which song sir')
                        song=mySpeech()
                        webbrowser.open_new('https://www.youtube.com/results?search_query='+song)
                    
                    # if message.strip()=='do you love someone':
                        # speak('i love sarbajyoti mallik')
                    # if message.strip()=='open youtube':
                        # song=input(str('which song sir'))
                        # print('chatterbot:which song sir:'+song)
                        # webbrowser.open_new('https://www.youtube.com/results?search_query='+ song)
                    # say=mySpeech()            
                    if 'bye' in content:
                        speak('bye sir')
                        break
            if command in 'hey':          
                speak("love you bro")
            if command in 'increase sound':
                speak('sound level increased')
                os.system(r"D:\nircmd.exe setsysvolume 65535")    
            if "how are you" in command:
                speak("i am good")
            if command in 'video':
                url='https://www.youtube.com/results?search_query='
                speak("which song do u want")
                song=mySpeech()
                webbrowser.open_new(url+song)
            if command in ['hi','darling','hello']:

                song=command
                speak(song)
            if 'music' in command:
                speak('which song sir')
                song=mySpeech()
                os.startfile('C:/Users/SARBAJYOTI/Downloads/Music/'+song +'.mp3')        
            if command in 'mail':
                speak("who is the recipient")
                recipient=mySpeech()
                # recipient='sam'
                if "hello" in recipient:
                    speak('what should i say')
                    content= mySpeech()
                    speak("you say "+content)
                    mail=smtplib.SMTP('smtp.gmail.com',587)
                    mail.ehlo()
                    mail.starttls()
                    mail.login("sarbajyoti123@gmail.com","mallik123")
                    mail.sendmail('sarbajyoti123@gmail.com','mukherjeepurnabrata1998@gmail.com',content)
                    mail.close()
                    speak("mail sent")    
            if command in 'search':

                url='http://google.com/search?q='
                speak("what are you looking for")
                song=mySpeech()
                webbrowser.open_new(url+song)
            if command in 'people':

                url='https://en.wikipedia.org/wiki/'
                speak("about whom sir")
                song=mySpeech()
                webbrowser.open_new(url+song) 
            if command in 'weather':
                # url='https://en.wikipedia.org/wiki/'
                speak("which place sir")
                song=mySpeech()
                webbrowser.open_new("https://www.weather-forecast.com/locations/"+song+"/forecasts/latest")
            if command in 'face':
                url2="https://www.facebook.com/"
                speak("sir am opening facebook")
                song=mySpeech()
                if 'ok' in song:
                    print('sir am opening facebook')
                    webbrowser.open_new(url2)
            if command in 'screen':
                speak("am taking a screenshot")
                song=mySpeech()
                if 'ok' in song:
                    pyautogui.screenshot('C:Users\SARBAJYOTI\OneDrive\Pictures\image1.jpg')
                    time.sleep(1)
            if command in 'game':
                # url='https://en.wikipedia.org/wiki/'
                speak("which game sir")
                song=mySpeech()
                if 'Far Cry' in song:
                    os.startfile(r"C:\Program Files (x86)\R.G. Mechanics\Far Cry 3\bin\farcry3.exe")
            if command in 'app':
                # url='https://en.wikipedia.org/wiki/'
                speak("which app sir")
                song=mySpeech()
                if 'WhatsApp' in song:
                    os.startfile(r"C:\Users\SARBAJYOTI\AppData\Local\WhatsApp\WhatsApp.exe")
            if command in 'image':
                speak("sir i am taking selfie")
                song=mySpeech()
                if 'ok' in song:
                    image=cv2.VideoCapture(0)
                    while(True):
                        check,frame=image.read()
                        cv2.imshow("frame.jpg",frame)
                        cv2.imwrite("frame.jpg",frame)
                        key=cv2.waitKey(1)
                        if key==ord("q"):
                            break
                    image.release()
                    cv2.destroyAllWindows()
            if command in 'find':
                speak("what sir ?")
                song=mySpeech()
                input=song
                app_id="K5H483-YUJATR7UQ6"
                client=wolframalpha.Client(app_id)
                result=client.query(input)
                answer=next(result.results).text
                speak("your answer is "+str(answer))

            if command in 'switch':
                speak("sir am clossing everything")
                sys.exit()    
        speak(" sir am jarvis how can i help you ")
        while True:
            jarvis(mySpeech())
App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec_())