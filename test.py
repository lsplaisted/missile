import turtle,math, time as t, random, keyboard, mouse, tkinter,pygame
from just_playback import Playback
playback = Playback()
root = tkinter.Tk()
screen = turtle.Screen()
screen.colormode(255)
screenTk = screen.getcanvas().winfo_toplevel()
screenTk.attributes("-fullscreen", True)


width = root.winfo_screenwidth()
height = root.winfo_screenheight()
root.destroy()

# test = turtle.Turtle()
# test.penup()
# test.shape('square')
# tx=0
# ty=0

while True:
    print(x,y)
    if keyboard.is_pressed('esc'):
        quit()