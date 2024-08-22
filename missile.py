import turtle, math, time as t, random, keyboard, mouse, tkinter, os
from just_playback import Playback
playback = Playback()
root = tkinter.Tk()

width = root.winfo_screenwidth()
height = root.winfo_screenheight()
print(width,height)
root.destroy()

turtle.tracer(0)
screen = turtle.Screen()
screenTk = screen.getcanvas().winfo_toplevel()
screenTk.attributes("-fullscreen", True)
screen.colormode(255)
screen.bgcolor('black')

missile_shape=((7,20),(0,30),(-7,20),(-7,-17),(-2,-17),(-3.5,-22),(3.5,-22),(2,-17),(7,-17))
screen.register_shape('missile',missile_shape)
missile=turtle.Turtle()
missile.penup()
missile.shape('missile')
missile.speed(0)
missile.color('white')

misflame=((3.5,-22),(5,-25),(10,-40),(12,-60),(-12,-60),(-10,-40),(-5,-25),(-3.5,-22))
screen.register_shape('misflame',misflame)
misflame = turtle.Turtle()
misflame.penup()
misflame.shape('misflame')
misflame.speed(0)
misflame.color(255,193,7)
misflame.goto(0,-150)
misflame.hideturtle()

sp=((30,8),(-30,8),(-30,-8),(30,-8))
screen.register_shape('panel',sp)
panel=turtle.Turtle()
panel.penup()
panel.speed(0)
panel.shape('panel')
panel.color(0,0,102)

satilite=((10,10),(-10,10),(-10,-10),(-4,-10),(-7,-15),(7,-15),(4,-10),(10,-10))
screen.register_shape('satilite',satilite)
satilite=turtle.Turtle()
satilite.penup()
satilite.shape('satilite')
satilite.speed(0)
satilite.color(255, 215, 0)

satflame=((7,-15),(8,-20),(10,-40),(-10,-40),(-8,-20),(-7,-15))
screen.register_shape('satflame',satflame)
satflame = turtle.Turtle()
satflame.penup()
satflame.shape('satflame')
satflame.speed(0)
satflame.color(255,193,7)
satflame.goto(0,150)
satflame.hideturtle()

pen=turtle.Turtle()
pen.hideturtle()
pen.penup()
pen.color('white')
pen.speed(0)

bledge = turtle.Turtle()
bledge.penup()
bledge.shape('square')
bledge.speed(0)
bledge.color(64,64,64)
bledge.hideturtle()
tredge = turtle.Turtle()
tredge.penup()
tredge.shape('square')
tredge.speed(0)
tredge.color(64,64,64)
tredge.hideturtle()

display=turtle.Turtle()
display.hideturtle()
display.penup()
display.color('white')
display.speed(0)
display.goto(-730,400)

satdir = 0 
satrot =0
misdir = 0
misrot = 0
time = -3
satxvel = 0
satyvel = 0
misxvel = 0
misyvel = 0
satx = 0
saty = 150
misx = 0
misy = -150
mode = ''
gtime = 20
running = False
sattemp = 0
mistemp = 0
astroids = []
astxy = []
astvel = []
swapped = False

panel.goto(satx,saty)
satilite.goto(satx,saty)
missile.goto(misx,misy)
turtle.tracer(1)

def is_within(x1,y1,x2,y2):# x1 and y1 must be greater than x2 and y2
    global width, height, posx, posy 
    posx,posy = mouse.get_position()
    posx -= width/2
    posy -= height/2
    posy *= -1
    if (x1 >= posx and y1 >= posy) and (x2 <= posx and y2 <= posy):
        return True
    else:
        return False

def litterbox():
    global height, width, scalefactor
    winwidth = turtle.window_width()
    winheight = turtle.window_height()
    bledge.showturtle()
    tredge.showturtle()
    if winwidth/winheight < 16/9:
        y = (((winwidth/16)*9)/2)
        bandheight = winheight / 2 - y
        tredge.goto(0, winheight / 2 - bandheight / 2 )
        bledge.goto(0, (winheight / 2 - bandheight / 2) * -1 )
        tredge.shapesize(bandheight/20, winwidth/20)
        bledge.shapesize(bandheight/20, winwidth/20)
        scalefactor = winwidth/1536
    if winwidth/winheight > 16/9:
        x = (((winheight/9)*16)/2)
        bandwidth = winwidth / 2 - x
        tredge.goto(winwidth / 2 - bandwidth / 2, 0)
        bledge.goto((winwidth / 2 - bandwidth / 2) * -1, 0)
        tredge.shapesize( winheight/20,bandwidth/20)
        bledge.shapesize( winheight/20,bandwidth/20)
        scalefactor = winheight/960
litterbox()
bledge.hideturtle()
tredge.hideturtle()

def scale(target):
    global height,width
    winwidth = turtle.window_width()
    winheight = turtle.window_height()
    if winwidth/winheight < 16/9:
        scalefactor = winwidth/1536
    if winwidth/winheight >= 16/9:
        scalefactor = winheight/960
    target.shapesize(scalefactor,scalefactor)

scale(missile)
scale(satilite)
scale(panel)

def showtime(rtime):
    global time
    display.clear()
    if time>0.1:
        display.goto(-730,350)
        display.write('TIME: '+str(rtime),font=('Verdana',25,'normal'))
    else:
        display.goto(0,0)
        display.write(rtime,font=('Verdana',40,'normal'),align='center')

def controls():
    global swapped
    pen.clear()
    panel.goto(-700*scalefactor,330*scalefactor)
    satilite.goto(-700*scalefactor,330*scalefactor)
    missile.goto(-700*scalefactor,180*scalefactor)
    missile.setheading(90)
    screen.bgcolor(0,43,50)
    turtle.tracer(0)
    t.sleep(.2)
    if not swapped:
        pen.goto(-650*scalefactor,310*scalefactor)
        pen.write('SATELITE CONTROLS:',font=('Yu Gothic UI Semibold', round(30*scalefactor)))
        pen.goto(-650*scalefactor,280*scalefactor)
        pen.write('W; ACCELERATE',font=('Yu Gothic UI Semibold', round(18*scalefactor)))
        pen.goto(-650*scalefactor,255*scalefactor)
        pen.write('A/D; ROTATE',font=('Yu Gothic UI Semibold', round(18*scalefactor)))
        pen.goto(-650*scalefactor,230*scalefactor)
        pen.write('S+A/S+D; ACCELERATE SIDEWAYS',font=('Yu Gothic UI Semibold', round(18*scalefactor)))
        pen.goto(-650*scalefactor,170*scalefactor)
        pen.write('MISSILE CONTROLS:',font=('Yu Gothic UI Semibold', round(30*scalefactor)))
        pen.goto(-650*scalefactor,140*scalefactor)
        pen.write('UP ACCELERATE',font=('Yu Gothic UI Semibold', round(18*scalefactor)))
        pen.goto(-650*scalefactor,115*scalefactor)
        pen.write('LEFT/RIGHT; ROTATE',font=('Yu Gothic UI Semibold', round(18*scalefactor)))
        pen.goto(-650*scalefactor,90*scalefactor)
        pen.write('DOWN+LEFT/DOWN+RIGHT; ACCELERATE SIDEWAYS',font=('Yu Gothic UI Semibold', round(18*scalefactor)))
    else:
        pen.goto(-650*scalefactor,310*scalefactor)
        pen.write('SATELITE CONTROLS:',font=('Yu Gothic UI Semibold', round(30*scalefactor)))
        pen.goto(-650*scalefactor,280*scalefactor)
        pen.write('UP; ACCELERATE',font=('Yu Gothic UI Semibold', round(18*scalefactor)))
        pen.goto(-650*scalefactor,255*scalefactor)
        pen.write('LEFT/RIGHT; ROTATE',font=('Yu Gothic UI Semibold', round(18*scalefactor)))
        pen.goto(-650*scalefactor,230*scalefactor)
        pen.write('DOWN+LEFT/DOWN+RIGHT; ACCELERATE SIDEWAYS',font=('Yu Gothic UI Semibold', round(18*scalefactor)))
        pen.goto(-650*scalefactor,170*scalefactor)
        pen.write('MISSILE CONTROLS:',font=('Yu Gothic UI Semibold', round(30*scalefactor)))
        pen.goto(-650*scalefactor,140*scalefactor)
        pen.write('W ACCELERATE',font=('Yu Gothic UI Semibold', round(18*scalefactor)))
        pen.goto(-650*scalefactor,115*scalefactor)
        pen.write('D/A; ROTATE',font=('Yu Gothic UI Semibold', round(18*scalefactor)))
        pen.goto(-650*scalefactor,90*scalefactor)
        pen.write('S+A/S+D; ACCELERATE SIDEWAYS',font=('Yu Gothic UI Semibold', round(18*scalefactor)))
    pen.goto(-650*scalefactor,30*scalefactor)
    pen.write('OTHER CONTROLS:',font=('Yu Gothic UI Semibold', round(30*scalefactor)))
    pen.goto(-650*scalefactor,0*scalefactor)
    pen.write('NUMBER KEYS/CLICKING; SELECTING OPTIONS',font=('Yu Gothic UI Semibold', round(18*scalefactor)))
    pen.goto(-650*scalefactor,-25*scalefactor)
    pen.write('ESC; QUIT WHILE PLAYING',font=('Yu Gothic UI Semibold', round(18*scalefactor)))
    pen.goto(-650*scalefactor,-50*scalefactor)
    pen.write('S+DOWN SWAP CONTROLS(ONLY WORKS ON CONTROLS SCREEN)',font=('Yu Gothic UI Semibold', round(18*scalefactor)))
    pen.goto(0*scalefactor,310*scalefactor)
    pen.write('OBJECT OF THE GAME: SATELITE',font=('Yu Gothic UI Semibold', round(30*scalefactor)))
    pen.goto(0*scalefactor,280*scalefactor)
    pen.write('The object of the game for the satelite to survive',font=('Yu Gothic UI Semibold', round(18*scalefactor)))
    pen.goto(0*scalefactor,255*scalefactor)
    pen.write('until the time runs out by dodging the missile and',font=('Yu Gothic UI Semibold', round(18*scalefactor)))
    pen.goto(0*scalefactor,230*scalefactor)
    pen.write('avoiding the astroids.',font=('Yu Gothic UI Semibold', round(18*scalefactor)))
    pen.goto(0*scalefactor,170*scalefactor)
    pen.write('OBJECT OF THE GAME: MISSILE',font=('Yu Gothic UI Semibold', round(30*scalefactor)))
    pen.goto(0*scalefactor,140*scalefactor)
    pen.write('The object of the game for the missile is to hit',font=('Yu Gothic UI Semibold', round(18*scalefactor)))
    pen.goto(0*scalefactor,115*scalefactor)
    pen.write('the satelite and avoid the astroids.',font=('Yu Gothic UI Semibold', round(18*scalefactor)))
    pen.goto(430*scalefactor,-430*scalefactor)
    pen.write('ESC; MAIN MENU',font=('Verdana', round(25*scalefactor)))
    turtle.tracer(1)
    pressed = False
    while not pressed:
        screenTk.attributes("-fullscreen", True)
        litterbox()
        bledge.color(0,30,40)
        tredge.color(0,30,40)
        if keyboard.is_pressed('esc') or (mouse.is_pressed('left') and is_within(725*scalefactor,-400*scalefactor,450*scalefactor,-425*scalefactor)):
            pressed = True
            reset()
        if keyboard.is_pressed('s+down'):
            if not swapped:
                swapped = True
            else:
                swapped = False
            pressed = True
            pen.clear()
            controls()

def ask_mode():
    global mode
    turtle.tracer(0)
    pen.goto(0*scalefactor,80*scalefactor)
    pen.write('SELECT MODE',font=("Verdana",round(35*scalefactor)),align='center')
    pen.goto(-120*scalefactor,30*scalefactor)
    pen.write('1. SATELITE MODE',font=("Verdana",round(20*scalefactor)),align='left')
    pen.goto(-120*scalefactor,0*scalefactor)
    pen.write('2. MISSILE MODE',font=("Verdana",round(20*scalefactor)),align='left')
    pen.goto(-120*scalefactor,-30*scalefactor)
    pen.write('3. BACK',font=("Verdana",round(20*scalefactor)),align='left')
    turtle.tracer(1)
    pressed = False
    t.sleep(.2)
    while not pressed:
        screenTk.attributes("-fullscreen", True)
        if keyboard.is_pressed('1') or (mouse.is_pressed('left') and is_within(120*scalefactor,55*scalefactor,-120*scalefactor,25*scalefactor)):
            pen.clear()
            pressed = True
            mode = 'sat'
            ask_time()
        if keyboard.is_pressed('2') or (mouse.is_pressed('left') and is_within(120*scalefactor,25*scalefactor,-120*scalefactor,-5*scalefactor)):
            pen.clear()
            pressed = True
            mode = 'mis'
            ask_time()
        if keyboard.is_pressed('3') or (mouse.is_pressed('left') and is_within(120*scalefactor,-5*scalefactor,-120*scalefactor,-35*scalefactor)):
            pen.clear()
            pressed = True
            askplay()

def ask_time():
    global gtime
    global players
    turtle.tracer(0)
    pen.goto(0*scalefactor,80*scalefactor)
    pen.write('SELECT GAME TIME',font=("Verdana",round(35*scalefactor)),align='center')
    pen.goto(-160*scalefactor,30*scalefactor)
    pen.write('1. 10 SEC',font=("Verdana",round(20*scalefactor)),align='left')
    pen.goto(-160*scalefactor,0*scalefactor)
    pen.write('3. 30 SEC',font=("Verdana",round(20*scalefactor)),align='left')
    pen.goto(-160*scalefactor,-30*scalefactor)
    pen.write('5. 1 MIN',font=("Verdana",round(20*scalefactor)),align='left')
    pen.goto(20*scalefactor,30*scalefactor)
    pen.write('2. 20 SEC',font=("Verdana",round(20*scalefactor)),align='left')
    pen.goto(20*scalefactor,0*scalefactor)
    pen.write('4. 45 SEC',font=("Verdana",round(20*scalefactor)),align='left')
    pen.goto(20*scalefactor,-30*scalefactor)
    pen.write('6. BACK',font=("Verdana",round(20*scalefactor)),align='left')
    pressed = False
    turtle.tracer(1)
    t.sleep(.2)
    while not pressed:
        screenTk.attributes("-fullscreen", True)
        if keyboard.is_pressed('1') or (mouse.is_pressed('left') and is_within(0*scalefactor,55*scalefactor,-160*scalefactor,25*scalefactor)):
            pressed = True
            gtime = 10
        elif keyboard.is_pressed('2') or (mouse.is_pressed('left') and is_within(160*scalefactor,55*scalefactor,0*scalefactor,25*scalefactor)):
            pressed = True
            gtime = 20
        elif keyboard.is_pressed('3') or (mouse.is_pressed('left') and is_within(0*scalefactor,25*scalefactor,-160*scalefactor,-5*scalefactor)):
            pressed = True
            gtime = 30
        elif keyboard.is_pressed('4') or (mouse.is_pressed('left') and is_within(160*scalefactor,25*scalefactor,0*scalefactor,-5*scalefactor)):
            pressed = True
            gtime = 45 
        elif keyboard.is_pressed('5') or (mouse.is_pressed('left') and is_within(0*scalefactor,-5*scalefactor,-160*scalefactor,-35*scalefactor)):
            pressed = True
            gtime = 60
        elif keyboard.is_pressed('6') or (mouse.is_pressed('left') and is_within(160*scalefactor,-5*scalefactor,0*scalefactor,-35*scalefactor)):
            pen.clear()
            pressed = True
            if players == 1:
                ask_mode()
            if players == 2:
                askplay()
    pen.clear()
    playback.stop()
    thisdir = os.path.dirname(os.path.abspath(__file__))
    mp3Path = os.path.join(thisdir, 'game_song.mp3')
    playback.load_file(mp3Path)
    playback.play()
    playback.loop_at_end(True)
    start()
    return

def askplay():
    global players
    turtle.tracer(0)
    thisdir = os.path.dirname(os.path.abspath(__file__))
    mp3Path = os.path.join(thisdir, 'menu_song.mp3')
    playback.load_file(mp3Path)
    playback.play()
    playback.loop_at_end(True)
    pen.goto(0*scalefactor,80*scalefactor)
    pen.write('MISSILE',font=("Verdana",round(35*scalefactor)),align='center')
    pen.goto(-80*scalefactor,30*scalefactor)
    pen.write('1. 1 PLAYER',font=("Verdana",round(20*scalefactor)),align='left')
    pen.goto(-80*scalefactor,0*scalefactor)
    pen.write('2. 2 PLAYERS',font=("Verdana",round(20*scalefactor)),align='left')
    pen.goto(-80*scalefactor,-30*scalefactor)
    pen.write('3. CONTROLS',font=("Verdana",round(20*scalefactor)),align='left')
    pen.goto(-80*scalefactor,-60*scalefactor)
    pen.write('4. EXIT',font=("Verdana",round(20*scalefactor)),align='left')
    turtle.tracer(1)
    pressed = False
    t.sleep(.2)
    while not pressed:
        screenTk.attributes("-fullscreen", True)
        if keyboard.is_pressed('1') or (mouse.is_pressed('left') and is_within(90*scalefactor,55*scalefactor,-90*scalefactor,25*scalefactor)):
            pen.clear()
            pressed = True
            players = 1
            ask_mode()
        if keyboard.is_pressed('2') or (mouse.is_pressed('left') and is_within(90*scalefactor,25*scalefactor,-90*scalefactor,-5*scalefactor)):
            pen.clear()
            pressed = True
            players = 2
            ask_time()
        if keyboard.is_pressed('3') or (mouse.is_pressed('left') and is_within(90*scalefactor,-5*scalefactor,-90*scalefactor,-35*scalefactor)):
            pressed = True
            controls()
        if keyboard.is_pressed('4') or (mouse.is_pressed('left') and is_within(90*scalefactor,-35*scalefactor,-90*scalefactor,-65*scalefactor)):
            quit()

def start():
    global running
    global targx
    global targy
    running=True
    targx=random.randint(-738,738)
    targy=random.randint(-450,450)
    run()

def explode(target): #improve later
    playback.stop()
    turtle.tracer(1)
    circle_diameter = 1
    r=255
    g=255
    b=255
    misflame.hideturtle()
    satflame.hideturtle()
    target.shape('circle')
    thisdir = os.path.dirname(os.path.abspath(__file__))
    mp3Path = os.path.join(thisdir, 'explosion.mp3')
    playback.load_file(mp3Path)
    playback.play()
    for i in range(25):
        turtle.tracer(0)
        t.sleep(.025)
        if i < 4:
            r -= 0
            g -= 8
            b -= 32
            if r < 0:
                r = 0
            if g < 0:
                g = 0
            if b < 0:
                b = 0
            circle_diameter *= 1.45
            target.shapesize(circle_diameter*scalefactor,circle_diameter*scalefactor)
        elif i < 15:
            r -= 16
            g -= 18
            b -= 32
            if r < 0:
                r = 0
            if g < 0:
                g = 0
            if b < 0:
                b = 0
            circle_diameter *= 1.15
            target.shapesize(circle_diameter*scalefactor,circle_diameter*scalefactor)
        else:
            r -= 32
            g -= 19
            b -= 0
            if r < 0:
                r = 0
            if g < 0:
                g = 0
            if b < 0:
                b = 0
        litterbox()
        target.color(r, g, b)
        turtle.tracer(1)
def reset():
    turtle.tracer(0)
    global satdir
    global misdir
    global running
    global satrot
    global misrot
    global time, gtime
    global satx
    global saty
    global misx
    global misy
    global satxvel
    global satyvel
    global misxvel
    global misyvel
    global mode
    global astroids, astxy, astvel
    screenTk.attributes("-fullscreen", True)
    turtle.tracer(0)
    screen.bgcolor('black')
    running=False
    panel.showturtle()
    missile.showturtle()
    satdir=0
    satrot=0
    misdir=0
    misrot=0
    time=-3
    satxvel=0
    satyvel=0
    misxvel=0
    misyvel=0
    satx=0
    saty=150
    misx=0
    misy=-150
    mode=''
    gtime=20
    for astriod in astroids:
        astriod.hideturtle()
    astroids = []
    astxy = []
    astvel = []
    missile.goto(misx,misy)
    missile.right(missile.heading()-360)
    satilite.goto(satx,saty)
    satilite.right(satilite.heading()-360)
    panel.goto(satx,saty)
    panel.right(panel.heading()-360)
    satilite.shapesize(1,1)
    satilite.shape('satilite')
    satilite.color(255, 215, 0)
    missile.color('white')
    missile.shape('missile')
    missile.shapesize(1*scalefactor,1*scalefactor)
    satflame.hideturtle()
    misflame.hideturtle()
    bledge.hideturtle()
    tredge.hideturtle()
    pen.clear()
    display.clear()
    turtle.tracer(1)
    askplay()

def run():
    global satdir
    global misdir
    global running
    global satrot
    global misrot
    global time
    global satx
    global saty
    global misx
    global misy
    global satxvel
    global satyvel
    global misxvel
    global misyvel
    global mode
    global gtime
    global targx
    global targy
    global astroids, astxy, astvel
    global swapped
    screenTk.attributes("-fullscreen", True)
    if running:
        if keyboard.is_pressed('esc'):
            reset()
            return
        screen.tracer(0)
        time += .025
        if time >=- .1 and time <= .1:
            showtime("GO!")
        elif time %1 <= .1 and time %1 >=- .1 and time > 0:
            showtime(gtime-round(time))
        elif time %1 <=.1 and time %1 >=-.1 and time<0:
            showtime(round(abs(time)))
        satdir=satilite.heading()
        misdir=missile.heading()
        if (satdir>panel.heading()+1) or (satdir<panel.heading()-1):
            panel.right(panel.heading()-360-satilite.heading())
        if misdir<0:
            misdir+=360
        satilite.right(satrot)
        panel.right(satrot)
        if time>0:
            missile.right(misrot)
            if time>gtime:
                playback.stop()
                pen.goto(0,0)
                display.clear()
                turtle.tracer(1)
                pen.write('SATILITE WINS',font=("Verdana",35, "normal"),align='center')
                t.sleep(1)
                reset()
                return
            satx += satxvel*scalefactor
            saty += satyvel*scalefactor
            satilite.goto(satx*scalefactor,saty*scalefactor)
            panel.goto(satx*scalefactor,saty*scalefactor)
            misx += misxvel
            misy += misyvel
            missile.goto(misx,misy)
            if (misx <= satx + 30*scalefactor) and (misx >= satx - 30*scalefactor) and (misy <= saty+30*scalefactor) and (misy >= saty - 30*scalefactor):
                missile.hideturtle()
                explode(satilite)
                pen.goto(0,0)
                display.clear()
                pen.write('MISSILE WINS',font=("Verdana",round(35*scalefactor)),align='center')
                t.sleep(1.0)
                reset()
                return
            for pos in astxy:
                if (pos[0] <= satx + 30*scalefactor and pos[0] >= satx - 30*scalefactor) and (pos[1] <= saty + 30*scalefactor and pos[1] >= saty - 30*scalefactor):
                    explode(satilite)
                    pen.goto(0,0)
                    display.clear()
                    pen.write('MISSILE WINS',font=("Verdana",round(35*scalefactor)),align='center')
                    t.sleep(1.0)
                    reset()
                    return
            for pos in astxy:
                if (pos[0] <= misx + 30*scalefactor and pos[0] >= misx - 30*scalefactor) and (pos[1] <= misy + 30*scalefactor and pos[1] >= misy - 30*scalefactor):
                    explode(missile)
                    pen.goto(0,0)
                    display.clear()
                    pen.write('SATELITE WINS',font=("Verdana",35, "normal"),align='center')
                    t.sleep(1.0)
                    reset()
                    return
            if gtime - time > 20:
                astrng = 10
            elif gtime - time < 20:
                astrng = 20
            elif gtime - time < 5:
                astrng = 40
            if random.randrange(1,round(gtime-time)+astrng) == 1:
                side = random.randrange(1,5)
                if side == 1:
                    astroids.append(turtle.Turtle())
                    astxy.append([800*scalefactor,random.randint(round(-300*scalefactor),round(300*scalefactor))])
                    astvel.append((random.randrange(round(-8*scalefactor),round(-3*scalefactor)),random.randrange(round(-4*scalefactor),round(4*scalefactor))))
                    ast = len(astroids) - 1
                    astroids[ast].color(128,128,128)
                    astroids[ast].shapesize(1.5*scalefactor,1.5*scalefactor)
                    astroids[ast].penup()
                    astroids[ast].speed(0)
                    astroids[ast].shape('circle')
                    astroids[ast].goto(astxy[ast])
                if side == 2:
                    astroids.append(turtle.Turtle())
                    astxy.append([random.randrange(round(-600*scalefactor),round(600*scalefactor)),-500*scalefactor])
                    astvel.append((random.randrange(round(-4*scalefactor),round(4*scalefactor)),random.randrange(round(3*scalefactor),round(8*scalefactor))))
                    ast = len(astroids) - 1
                    astroids[ast].color(128,128,128)
                    astroids[ast].shapesize(1.5*scalefactor,1.5*scalefactor)
                    astroids[ast].penup()
                    astroids[ast].speed(0)
                    astroids[ast].shape('circle')
                    astroids[ast].goto(astxy[ast])
                if side == 3:
                    astroids.append(turtle.Turtle())
                    astxy.append([-800*scalefactor,random.randint(round(-300*scalefactor),round(300*scalefactor))])
                    astvel.append((random.randrange(round(3*scalefactor),round(8*scalefactor)),random.randrange(round(-4*scalefactor),round(4*scalefactor))))
                    ast = len(astroids) - 1
                    astroids[ast].color(128,128,128)
                    astroids[ast].shapesize(1.5*scalefactor,1.5*scalefactor)
                    astroids[ast].penup()
                    astroids[ast].speed(0)
                    astroids[ast].shape('circle')
                    astroids[ast].goto(astxy[ast])
                if side == 4:
                    astroids.append(turtle.Turtle())
                    astxy.append([random.randrange(round(-600*scalefactor),round(600*scalefactor)),500*scalefactor])
                    astvel.append((random.randrange(round(-4*scalefactor),round(4*scalefactor)),random.randrange(round(-8*scalefactor),round(-3*scalefactor))))
                    ast = len(astroids) - 1
                    astroids[ast].color(128,128,128)
                    astroids[ast].shapesize(1.5*scalefactor,1.5*scalefactor)
                    astroids[ast].penup()
                    astroids[ast].speed(0)
                    astroids[ast].shape('circle')
                    astroids[ast].goto(astxy[ast])
            if len(astroids) > 0:
                for astroid in range(len(astroids)):
                    astxy[astroid][0] += astvel[astroid][0]
                    astxy[astroid][1] += astvel[astroid][1]
                    astroids[astroid].goto(astxy[astroid][0]*scalefactor,astxy[astroid][1]*scalefactor)
            if players == 2:
                if not swapped:
                    if keyboard.is_pressed('w'):
                        satyvel+=(math.sin(math.radians(satdir)))/6
                        satxvel+=(math.cos(math.radians(satdir)))/6
                        satflame.goto(satx,saty)
                        satflame.setheading(satdir)
                        satflame.showturtle()
                    else:
                        satflame.hideturtle()
                    if keyboard.is_pressed('a+s'):
                        satyvel+=(math.sin(math.radians(satdir+90)))/15
                        misxvel+=(math.cos(math.radians(satdir+90)))/15
                    elif keyboard.is_pressed('d+s'):
                        satyvel+=(math.sin(math.radians(satdir-90)))/15
                        satxvel+=(math.cos(math.radians(satdir-90)))/15
                    elif keyboard.is_pressed('a'):
                        satrot -= .2
                    elif not keyboard.is_pressed('a') and satrot < 0:
                        satrot += .4
                    elif keyboard.is_pressed('d'):
                        satrot += .2
                    elif not keyboard.is_pressed('d') and satrot > 0:
                        satrot -= .4
                    if keyboard.is_pressed('up'):
                        misyvel+=(math.sin(math.radians(misdir)))/5
                        misxvel+=(math.cos(math.radians(misdir)))/5
                        misflame.goto(misx,misy)
                        misflame.setheading(misdir)
                        misflame.showturtle()
                    else:
                        misflame.hideturtle()
                    if keyboard.is_pressed('left+down'):
                        misyvel+=(math.sin(math.radians(misdir+90)))/15
                        misxvel+=(math.cos(math.radians(misdir+90)))/15
                    elif keyboard.is_pressed('right+down'):
                        misyvel+=(math.sin(math.radians(misdir-90)))/15
                        misxvel+=(math.cos(math.radians(misdir-90)))/15
                    elif keyboard.is_pressed('left'):
                        misrot -= .2
                    elif not keyboard.is_pressed('left') and misrot < 0:
                        misrot += .4
                    elif keyboard.is_pressed('right'):
                        misrot += .2
                    elif not keyboard.is_pressed('right') and misrot > 0:
                        misrot -= .4
                else:
                    if keyboard.is_pressed('up'):
                        satyvel+=(math.sin(math.radians(satdir)))/6
                        satxvel+=(math.cos(math.radians(satdir)))/6
                        satflame.goto(satx,saty)
                        satflame.setheading(satdir)
                        satflame.showturtle()
                    else:
                        satflame.hideturtle()
                    if keyboard.is_pressed('left+down'):
                        satyvel+=(math.sin(math.radians(satdir+90)))/15
                        misxvel+=(math.cos(math.radians(satdir+90)))/15
                    elif keyboard.is_pressed('right+down'):
                        satyvel+=(math.sin(math.radians(satdir-90)))/15
                        satxvel+=(math.cos(math.radians(satdir-90)))/15
                    elif keyboard.is_pressed('left'):
                        satrot -= .2
                    elif not keyboard.is_pressed('left') and satrot < 0:
                        satrot += .4
                    elif keyboard.is_pressed('right'):
                        satrot += .2
                    elif not keyboard.is_pressed('right') and satrot > 0:
                        satrot -= .4
                    if keyboard.is_pressed('w'):
                        misyvel+=(math.sin(math.radians(misdir)))/5
                        misxvel+=(math.cos(math.radians(misdir)))/5
                        misflame.goto(misx,misy)
                        misflame.setheading(misdir)
                        misflame.showturtle()
                    else:
                        misflame.hideturtle()
                    if keyboard.is_pressed('a+s'):
                        misyvel+=(math.sin(math.radians(misdir+90)))/15
                        misxvel+=(math.cos(math.radians(misdir+90)))/15
                    elif keyboard.is_pressed('d+s'):
                        misyvel+=(math.sin(math.radians(misdir-90)))/15
                        misxvel+=(math.cos(math.radians(misdir-90)))/15
                    elif keyboard.is_pressed('a'):
                        misrot -= .2
                    elif not keyboard.is_pressed('a') and misrot < 0:
                        misrot += .4
                    elif keyboard.is_pressed('d'):
                        misrot += .2
                    elif not keyboard.is_pressed('d') and misrot > 0:
                        misrot -= .4
            if mode == 'sat':
                col = False
                for ast in range(len(astroids)):
                    if (astxy[ast][0] <= misx + 400*scalefactor and astxy[ast][0] >= misx - 400*scalefactor) and (astxy[ast][1] <= misy + 400*scalefactor and astxy[ast][1] >= misy - 400*scalefactor):
                        colxy = [[],[0,0]]
                        colxy[0] = astxy[ast].copy()
                        colxy[1][0] = misx
                        colxy[1][1] = misy
                        for i in range(60):
                            colxy[0][0] += astvel[ast][0]
                            colxy[0][1] += astvel[ast][0]
                            colxy[1][0] += misxvel
                            colxy[1][1] += misyvel
                            if (colxy[0][0] <= colxy[1][0] + 30*scalefactor and colxy[0][0] >= colxy[1][0] - 30*scalefactor) and (colxy[0][1] <= colxy[1][1] + 30*scalefactor and colxy[0][1] >= colxy[1][1] - 30*scalefactor):
                                col = True
                                mistar = missile.towards(astroids[ast])+90
                                if misx-satx>0:
                                    mistar += 180
                if satx-misx != 0 and not col:
                    mistar=math.degrees(math.atan((saty-misy)/(satx-misx)))
                    if misx-satx>0:
                        mistar += 180
                elif satx-misx==0 and saty-misy>0:
                    mistar=90
                elif satx-misx==0 and saty-misy<0:
                    mistar=270
                if mistar<0:
                    mistar+=360

                target_change = mistar - misdir
                target_change = target_change % 360
                if target_change > 180:
                    target_change = target_change - 360
                if target_change > 5:
                    if misrot > -90 and not col:
                        misrot -= .2
                    else:
                        misrot -= .6
                elif target_change < -5:
                    if misrot <90 and not col:
                        misrot += .2
                    else:
                        misrot += .6
                else:
                    misrot = 0
                if mistar-misdir<=45 and mistar-misdir>=-45 and not col:
                    misyvel+=(math.sin(math.radians(misdir)))/5
                    misxvel+=(math.cos(math.radians(misdir)))/5
                    misflame.goto(misx,misy)
                    misflame.setheading(misdir)
                    misflame.showturtle()
                elif mistar-misdir<=90 and mistar-misdir>=-45:
                    misyvel+=(math.sin(math.radians(misdir)))/5
                    misxvel+=(math.cos(math.radians(misdir)))/5
                    misflame.goto(misx,misy)
                    misflame.setheading(misdir)
                    misflame.showturtle()
                else:
                    misflame.hideturtle()
                if keyboard.is_pressed('w') or keyboard.is_pressed('up'):
                    satyvel+=(math.sin(math.radians(satdir)))/6
                    satxvel+=(math.cos(math.radians(satdir)))/6
                    satflame.goto(satx,saty)
                    satflame.setheading(satdir)
                    satflame.showturtle()
                else:
                    satflame.hideturtle()
                if keyboard.is_pressed('a+s') or keyboard.is_pressed('left+down'):
                    satyvel+=(math.sin(math.radians(satdir+90)))/15
                    satxvel+=(math.cos(math.radians(satdir+90)))/15
                elif keyboard.is_pressed('d+s') or keyboard.is_pressed('right+down'):
                    satyvel+=(math.sin(math.radians(satdir-90)))/15
                    satxvel+=(math.cos(math.radians(satdir-90)))/15
                elif keyboard.is_pressed('a') or keyboard.is_pressed('left'):
                    satrot -= .2
                elif not keyboard.is_pressed('a') and not keyboard.is_pressed('left') and satrot < 0:
                    satrot += .4
                elif keyboard.is_pressed('d') or keyboard.is_pressed('right'):
                    satrot += .2
                elif not keyboard.is_pressed('d') and not keyboard.is_pressed('right') and satrot > 0:
                    satrot -= .4
            elif mode == 'mis':
                col = False
                if (targx-satx<25 and targx-satx>25) and (targy-saty<25 and targy-saty>25):
                    targx=random.randint(-738,738)
                    targy=random.randint(-450,450)
                for ast in range(len(astroids)):
                    if (astxy[ast][0] <= satx + 400*scalefactor and astxy[ast][0] >= satx - 400*scalefactor) and (astxy[ast][1] <= saty + 400*scalefactor and astxy[ast][1] >= saty - 400*scalefactor):
                        colxy = [[],[0,0]]
                        colxy[0] = astxy[ast].copy()
                        colxy[1][0] = satx
                        colxy[1][1] = saty
                        for i in range(60):
                            colxy[0][0] += astvel[ast][0]
                            colxy[0][1] += astvel[ast][0]
                            colxy[1][0] += satxvel
                            colxy[1][1] += satyvel
                            if (colxy[0][0] <= colxy[1][0] + 30*scalefactor and colxy[0][0] >= colxy[1][0] - 30*scalefactor) and (colxy[0][1] <= colxy[1][1] + 30*scalefactor and colxy[0][1] >= colxy[1][1] - 30*scalefactor):
                                col = True
                                satar = satilite.towards(astroids[ast])+90
                                if satx-targx>0:
                                    satar += 180
                if targx-satx!=0 and not col:
                    satar=math.degrees(math.atan((targy-saty)/(targx-satx)))
                    if satx-targx>0:
                        satar += 180
                elif targx-satx==0 and targy-saty>0:
                    satar=90
                elif targx-satx==0 and targy-saty<0:
                    satar=270
                if satar<0:
                    satar+=360

                target_change = satar - satdir
                target_change = target_change % 360
                if target_change > 180:
                    target_change = target_change - 360
                if target_change > 5:
                    if satrot > -9 and not col:
                        satrot -= .2
                    else:
                        satrot -= 6
                elif target_change < -5:
                    if satrot <9 and not col:
                        satrot += .2
                    else: 
                        satrot += .6
                else:
                    satrot = 0
                if satar-satdir<=45 and satar-satdir>=-45 and not col:
                    satyvel+=(math.sin(math.radians(satdir)))/6
                    satxvel+=(math.cos(math.radians(satdir)))/6
                    satflame.goto(satx,saty)
                    satflame.setheading(satdir)
                    satflame.showturtle()
                elif satar-satdir<=90 and satar-satdir>=-45:
                    satyvel+=(math.sin(math.radians(satdir)))/6
                    satxvel+=(math.cos(math.radians(satdir)))/6
                    satflame.goto(satx,saty)
                    satflame.setheading(satdir)
                    satflame.showturtle()
                else:
                    satflame.hideturtle()
                if keyboard.is_pressed('w') or keyboard.is_pressed('up'):
                    misyvel+=(math.sin(math.radians(misdir)))/5
                    misxvel+=(math.cos(math.radians(misdir)))/5
                    misflame.goto(misx,misy)
                    misflame.setheading(misdir)
                    misflame.showturtle()
                else:
                    misflame.hideturtle()
                if keyboard.is_pressed('a+s') or keyboard.is_pressed('left+down'):
                    misyvel+=(math.sin(math.radians(misdir+90)))/15
                    misxvel+=(math.cos(math.radians(misdir+90)))/15
                elif keyboard.is_pressed('d+s') or keyboard.is_pressed('right+down'):
                    misyvel+=(math.sin(math.radians(misdir-90)))/15
                    misxvel+=(math.cos(math.radians(misdir-90)))/15
                elif keyboard.is_pressed('a') or keyboard.is_pressed('left'):
                    misrot -= .3
                elif not keyboard.is_pressed('a') and not keyboard.is_pressed('left') and misrot < 0:
                    misrot += .5
                elif keyboard.is_pressed('d') or keyboard.is_pressed('right'):
                    misrot += .3
                elif not keyboard.is_pressed('d') and not keyboard.is_pressed('right') and misrot > 0:
                    misrot -= .5
            if satx>740*scalefactor:
                satxvel=-2.5*scalefactor
                satyvel=0
            if satx<-740*scalefactor:
                satxvel=2.5*scalefactor
                satyvel=0
            if saty>400*scalefactor:
                satxvel=0
                satyvel=-2.5*scalefactor
            if saty<-400*scalefactor:
                satxvel=0
                satyvel=2.5*scalefactor
            if misx>740*scalefactor:
                misxvel=-2.5*scalefactor
                misyvel=0
            if misx<-740*scalefactor:
                misxvel=2.5*scalefactor
                misyvel=0
            if misy>400*scalefactor:
                misxvel=0
                misyvel=-2.5*scalefactor
            if misy<-400*scalefactor:
                misxvel=0
                misyvel=2.5*scalefactor
        litterbox()
        screen.tracer(1)
        screen.ontimer(run, 20)

askplay()
turtle.mainloop()