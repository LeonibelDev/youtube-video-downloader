from tkinter import ttk
from tkinter import *
from yt_dl import download_video
import time
import re

patterns = [
    r"https://www.youtube.com/([\w\.-]+)", 
    r"www.youtube.com/([\w\.-]+)"
    ]

class Main:
    def __init__(self, window):
        self.wind = window
        self.wind.title("Download Videos")
        self.wind.configure(background = "#f1f1f1", pady = 9, padx = 9)

        # TITLE
        self.message = Label(text = '', fg = '#000')
        self.message.grid(row = 1, column = 0, columnspan = 2, sticky = W + E)    

        # GUI
        Label(text = 'Copy Your Link: ').grid(row = 2, column = 0)
        self.url = Entry()
        self.url.grid(row = 2, column = 1, padx = 10)
        self.url.focus()

        # STATUS


        # BUTTON
        btn = ttk.Button(text = "Download", command = self.download)
        btn.grid(row = 3, column = 1, padx = 10, pady = 10)

        # RUN
        window.mainloop()

    def download(self):
        value = self.url

        validator = list(filter(lambda x: re.match(x, value.get()), patterns))
        
        if bool(validator):
            try:
                self.message["text"] = "Wait..."
                self.message["fg"] = "#000"

                download_video(value.get())
                
                self.message["text"] = "Downloaded :)"
                self.message["fg"] = "green"

            except:
                self.message["text"] = "Process Error :("
            
            finally:
                value.delete(0, END)

        else:
            self.message["text"] = "Invalid URL"
            self.message["fg"] = "red"
            value.delete(0, END)

            # time.sleep(3)
            # self.message["text"] = ""


if __name__ == '__main__':
    window = Tk()
    Main(window)