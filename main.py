import keyboard
import tkinter as tk
from tkinter import *
import sys
sys.setrecursionlimit(10000)


class App:
    def __init__(self):
        self.keys = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                     'u', 'v',
                     'w', 'x', 'y', 'z', '1', '2', '3', '4', '5',
                     '6', '7', '8', '9', 'enter', 'shift', 'tab', '`', "'", ';', ',', '.', '/', 'alt', 'ctrl']
        self.count = 0
        self.root = Tk()
        self.frame = tk.Frame(self.root)
        # Screen Sizes
        scr_wid = self.root.winfo_screenwidth()
        scr_hei = self.root.winfo_screenheight()
        # Root Stuff
        self.root.wm_attributes("-topmost", True)
        self.root.wm_attributes("-disabled", True)
        self.root.wm_attributes("-transparentcolor", "#444444")
        self.root.overrideredirect(True)
        self.root.geometry(f'300x300+{scr_wid - 300}+{scr_hei - 300}')
        self.root.image = tk.PhotoImage(file='bg.png')
        self.root.attributes('-alpha', '1')
        # Label Stuff
        label = tk.Label(self.root, image=self.root.image, bg='#444444')
        label.pack()

        self.root.lift()
        self.root.after(100000, self.check_keys())
        self.root.mainloop()

    def check_keys(self):
        for key in range(len(self.keys)):
            if keyboard.is_pressed(self.keys[key]):
                print(str(self.count) + self.keys[key])
                self.count += 1
        self.root.after(1000, self.check_keys())

    def close(self):
        print("hi")

        '''
        while True:
            for key in range(len(keys)):
                if keyboard.is_pressed(keys[key]):
                    count += 1
                    print(str(count) + keys[key])
                    time.sleep(.1)
                if key == len(keys):
                    key = 0
        '''


app = App()
