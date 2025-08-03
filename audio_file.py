def audio():
    import tkinter as tk
    from tkinter import filedialog
    from tkinter.messagebox import showinfo
    import speech_recognition as sr

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
            file_path = filedialog.askopenfilename(filetypes=[("Audio Files", ".wav;.mp3")])
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

    __name__ == "__main__"
    root = tk.Tk()
    app = AudioToTextConverter(root)
    root.mainloop()