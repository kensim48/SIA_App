import time
import tkinter as tk
from tkinter import END
import cv2
from PIL import Image, ImageTk
import _thread
import queue
import scan_webcam

class App():
    root = tk.Tk()
    video_panel = None
    listbox = None
    variable_queue_1 = queue.Queue()
    photo_panel = None

    def VideoLoop(self, null1=None, null2=None):
        video_feed = scan_webcam.qr_scanner(cv2.VideoCapture(0), self.variable_queue_1)
        while True:
            frame = video_feed.qr_scan_frame()
            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image = Image.fromarray(image)
            image = ImageTk.PhotoImage(image)
            # if the panel is not None, we need to initialize it
            if self.video_panel is None:
                self.video_panel = tk.Label(image=image)
                self.video_panel.image = image
                self.video_panel.pack(side="left")

            # otherwise, simply update the panel
            else:
                self.video_panel.configure(image=image)
                self.video_panel.image = image

    def TextLoop(self,null1=None, null2=None):
        self.listbox = tk.Listbox(self.root,height=60,width=90)
        self.listbox.pack(side="right")
        while True:
            self.listbox.insert(END, self.variable_queue_1.get())

    def main(self):
        _thread.start_new_thread(self.VideoLoop, (None, None))
        _thread.start_new_thread(self.TextLoop, (None, None))
        self.root.mainloop()

app = App()
app.main()
