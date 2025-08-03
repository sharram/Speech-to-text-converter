def lang():    
    import tkinter as tk
    import English
    import Hindi
    import Kannada
    import Tamil
    import Korean
    import Japanese
    micro=tk.Tk()
    micro.title('Choose the input Language')
    micro.geometry('400x400')
    micro.resizable(0,0)
    micro.configure(bg='Light Blue')

    tk.Button(micro,text='English', bg='Pink',command=English.eng).place(x=100,y=50)
    tk.Button(micro,text='Hindi', bg='Pink',command=Hindi.hin).place(x=100,y=100)
    tk.Button(micro,text='Kannada', bg='Pink', command=Kannada.kan).place(x=100,y=150)
    tk.Button(micro,text='Tamil', bg='Pink',command=Tamil.tam).place(x=100,y=200)
    tk.Button(micro,text='Korean', bg='Pink', command=Korean.korean).place(x=100,y=250)
    tk.Button(micro,text='Japanese', bg='Pink',command=Japanese.jap).place(x=100,y=300)
    micro.mainloop()






















"""
from tkinter.messagebox import showinfo
from tkinter import filedialog
from gtts import gTTS
from tkinter import*
import speech_recognition as sr
import os
root=tk.Tk()
root.geometry('500x500')
root.title("Speech to Text Converter")
v=tk.IntVar()

#tk.Radiobutton(root,text="Audio file").pack()

#tk.Radiobutton(root,text="Microphone").pack()

#v=tk.IntVar()
#tk.Radiobutton(root,text='Audio file',variable=v, value=1).pack()
#tk.Radiobutton(root,text='MIcrophone',variable=v, value=2).pack()

if (v.get()==0):
  def abc(self):
    class AudioToTextConverter:
        def __init__(self, root):
            self.root = root
            self.root.title("Audio to Text Converter")

            self.label = tk.Label(root, text="Select an audio file:")
            self.label.pack(pady=10)

            self.browse_button = tk.Button(root, text="Browse", command=self.browse_audio_file)
            self.browse_button.pack(pady=10)

            self.convert_button = tk.Button(root, text="Convert", command=self.convert_audio_to_text)
            self.convert_button.pack(pady=10)

            self.text_output = tk.Text(root, height=10, width=50)
            self.text_output.pack(pady=10)

        def browse_audio_file(self):
            file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.wav;*.mp3")])
            self.label.config(text=f"Selected file: {file_path}")
            self.audio_file_path = file_path

        def convert_audio_to_text(self):
            if hasattr(self, 'audio_file_path') and self.audio_file_path:
                recognizer = sr.Recognizer()
                with sr.AudioFile(self.audio_file_path) as source:
                    audio_data = recognizer.record(source)
                    try:
                        text = recognizer.recognize_google(audio_data)
                        self.text_output.delete(1.0, tk.END)
                        self.text_output.insert(tk.END, text)
                    except sr.UnknownValueError:
                        self.text_output.delete(1.0, tk.END)
                        self.text_output.insert(tk.END, "Speech Recognition could not understand the audio.")
                    except sr.RequestError as e:
                        self.text_output.delete(1.0, tk.END)
                        self.text_output.insert(tk.END, f"Error with the speech recognition service: {e}")
            else:
                self.text_output.delete(1.0, tk.END)
                self.text_output.insert(tk.END, "Please select an audio file first.")

    if __name__ == "__main__":
        root = tk.Tk()
        app = AudioToTextConverter(root)
        root.mainloop()

elif (v.get()==1):
  def xyz():  
    mainwindow= tk()
    mainwindow.title('Text-To-Speech Converter')
    mainwindow.geometry('500x500')
    mainwindow.resizable(0, 0)
    mainwindow.configure(bg='blue')
    def say(text1):
        language = 'en'
        speech = gTTS(text = text1, lang = language, slow = False)
        speech.save("text.mp3")
        os.system("start text.mp3")
 
    def recordvoice():
        while True:
            r = sr.Recognizer()
            with sr.Microphone() as source:
                audio=r.listen(source)
                try:    
                    text1 = r.recognize_google(audio,language="en-IN")
                except:
                    pass
                return text1

    def SpeechToText():
        speechtotextwindow = tk.Toplevel(mainwindow)
        speechtotextwindow.title('Speech-to-Text Converter by DataFlair')
        speechtotextwindow.geometry("500x500")
        speechtotextwindow.configure(bg='white')
 
        tk.Label(speechtotextwindow, text='Speech-to-Text Converter', font=("Comic Sans MS", 15), bg='white').place(x=50)
 
        text = tk.Text(speechtotextwindow, font=12, height=3, width=30)
        text.place(x=7, y=100)
   
        recordbutton = tk.Button(speechtotextwindow, text='Record', bg='red', command=lambda: text.insert(tk.END, recordvoice()))
        recordbutton.place(x=140, y=50)
 
    tk.Label(mainwindow, text='Speech-To-Text Converter',
        font=('Times New Roman', 16), bg='yellow', wrap=True, wraplength=450).place(x=25, y=0)
 
 
    speechtotextbutton = tk.Button(mainwindow, text='Speech-To-Text Conversion', font=('Times New Roman', 16), bg='Purple', command=SpeechToText)
    speechtotextbutton.place(x=100, y=250)
 
    mainwindow.update()
    mainwindow.mainloop()
"""





