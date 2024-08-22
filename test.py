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
    if winwidth/winheight < 16/9:
        y = (((winwidth/16)*9)/2)
        bandheight = winheight / 2 - y
        tredge.goto(0, winheight / 2 - bandheight / 2 )
        bledge.goto(0, (winheight / 2 - bandheight / 2) * -1 )
        tredge.shapesize(bandheight/20, winwidth/20)
        bledge.shapesize(bandheight/20, winwidth/20)
    if winwidth/winheight > 16/9:
        x = (((winheight/9)*16)/2)
        bandwidth = winwidth / 2 - x
        tredge.goto(winwidth / 2 - bandwidth / 2, 0)
        bledge.goto((winwidth / 2 - bandwidth / 2) * -1, 0)
        tredge.shapesize( winheight/20,bandwidth/20)
        bledge.shapesize( winheight/20,bandwidth/20)

    if keyboard.is_pressed('esc'):
        quit()