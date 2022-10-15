import glob
import shutil

import keyboard
import win32api
import win32con
import win32gui
from pygame import *
import pygame as pg
import os
from screeninfo import get_monitors

myScreen = get_monitors()[0]
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (myScreen.width - 300, myScreen.height - 300)
homeDir = os.path.expanduser("~\\AppData\\Local\\KeyCount")

keys = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
        'u', 'v',
        'w', 'x', 'y', 'z', '1', '2', '3', '4', '5',
        '6', '7', '8', '9', '0', 'enter', 'tab', '`', "'", ';', ',', '.', '/', 'alt', 'ctrl', 'backspace']
count = 0

init()
clock = time.Clock()
screen = display.set_mode((300, 300), NOFRAME)


class App:
    def __init__(self):
        display.set_caption("Key Counter")

        self.font = font.Font(None, 60)

        self.bgImg = image.load(os.path.join(homeDir + '\\bg.png'))
        self.catImg = image.load(os.path.join(homeDir + '\\cat0.png'))
        self.draw()

    def change_cat(self):
        if (count % 2) == 0:
            tempcount = 0
        else:
            tempcount = 1
        self.catImg = image.load(os.path.join(homeDir + '\\cat' + str(tempcount) + '.png'))

    def draw(self):
        hwnd = display.get_wm_info()["window"]
        win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE,
                               win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE) | win32con.WS_EX_LAYERED)
        win32gui.SetLayeredWindowAttributes(hwnd, win32api.RGB(68, 68, 68), 0, win32con.LWA_COLORKEY)

        screen.fill('#444444')

        if len(str(count)) > 8:
            self.font = font.Font(None, 60 - len(str(count)) * 2)

        screen.blit(self.bgImg, (0, 0))
        screen.blit(self.catImg, (47, 20))
        sp_txt_surface = self.font.render(str(count), True, 'black')
        screen.blit(sp_txt_surface, (50, 230))

        display.flip()


def load_files():
    global homeDir
    try:
        os.mkdir(homeDir, 0o777)
        for file in glob.glob("*.png"):
            shutil.move(file, homeDir)
    except FileExistsError:
        for file in glob.glob("*.png"):
            shutil.move(file, homeDir)
    os.remove('main.py')


load_files()
app = App()

while True:
    for ev in pg.event.get():
        if ev.type == pg.QUIT:
            quit()
        if ev.type == pg.K_END:
            quit()
        if ev.type == pg.K_ESCAPE:
            quit()
        if ev.type == pg.K_q:
            quit()
    for key in range(len(keys)):
        if keyboard.is_pressed(keys[key]):
            count += 1
            app.change_cat()
            app.draw()
            clock.tick(8)
        if key == len(keys):
            key = 0
