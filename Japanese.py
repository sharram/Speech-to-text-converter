def jap():    
    import tkinter as tk
    from tkinter.messagebox import showinfo
    from gtts import gTTS
    import speech_recognition as sr
    import os
    mainwindow= tk.Tk()
    mainwindow.geometry('500x500')
    mainwindow.resizable(0, 0)
    mainwindow.configure(bg='black')

    def say(text1):
        language = 'ja-JP'
        speech = gTTS(text = text1, lang = language, slow = False)
        speech.save("text.mp3")
        os.system("start text.mp3")


    def recordvoice():
        while True:
            r = sr.Recognizer()
            with sr.Microphone() as source:
                audio=r.listen(source)
                try:    
                    text1 = r.recognize_google(audio,language="ja-JP")
                except:
                    pass
                return text1


    

    def SpeechToText():
        speechtotextwindow = tk.Toplevel(mainwindow)
        speechtotextwindow.title('Speech-to-Text Converter')
        speechtotextwindow.geometry("500x500")
        speechtotextwindow.configure(bg='white')
    
        tk.Label(speechtotextwindow, text='Speech-to-Text Using Audio', font=("Comic Sans MS", 15), bg='cyan').place(x=75)
    
        text = tk.Text(speechtotextwindow, font=12, height=3, width=30)
        text.place(x=7, y=100)
    
        recordbutton = tk.Button(speechtotextwindow, text='Record', bg='red', command=lambda: text.insert(tk.END, recordvoice()))
        recordbutton.place(x=140, y=50)
    
    tk.Label(mainwindow, text='Speech-To-Text Converter',
        font=('Times New Roman', 16), bg='yellow', wrap=True, wraplength=450).place(x=100, y=0)
    
    
    speechtotextbutton = tk.Button(mainwindow, text='Speech-To-Text Using Audio', font=('Times New Roman', 16), bg='cyan', command=SpeechToText)
    speechtotextbutton.place(x=100, y=250)
    
    mainwindow.update()
    mainwindow.mainloop()