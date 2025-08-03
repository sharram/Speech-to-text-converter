import tkinter as tk 
import audio_file
import Language

win=tk.Tk()
win.title("speech to text converter")
win.geometry("500x500")
win.configure(bg='light yellow')
tk.Label(win, text='Choose kind of input', font=("Cordia New",15), bg='light green').place(x=75, y=25)
tk.Button(win, text='Audio File', font=("Cordia New",12), bg='light blue',command=audio_file.audio).place(x=100,y=100)
tk.Button(win, text='Microphone', font=("Cordia New",12), bg='Pink',command=Language.lang).place(x=100,y=200)
win.mainloop()

