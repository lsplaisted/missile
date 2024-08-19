import turtle, math, time as t, random, keyboard, mouse, tkinter
from just_playback import Playback
playback = Playback()
root = tkinter.Tk()
screen = turtle.Screen()
screen.colormode(255)
#screenTk = screen.getcanvas().winfo_toplevel()
#screenTk.attributes("-fullscreen", True)

width = root.winfo_screenwidth()
height = root.winfo_screenheight()
root.destroy()

#test = turtle.Turtle()
#test.penup()
#test.shape('square')

bledge = turtle.Turtle()
bledge.penup()
bledge.shape('square')
bledge.speed(0)
#bledge.hideturtle()
tredge = turtle.Turtle()
tredge.penup()
tredge.shape('square')
tredge.speed(0)
#tredge.hideturtle()

while True:
    winwidth = turtle.window_width()
    winheight = turtle.window_height()
    if width/height < 16/9:
        y = (((winwidth/16)*9)/2)
        print(y)
        tredge.goto(0, (y))
        bledge.goto(0,(y*-1))
        tredge.shapesize(1,winwidth/20)
        bledge.shapesize(1,winwidth/20)

    if keyboard.is_pressed('esc'):
        quit()