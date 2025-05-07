import turtle, random

screen = turtle.Screen()
screen.bgcolor('black')
screen.colormode(255)

# set of pionts for big dipper
Big_dipper = [[(-100,64), 40, (255, 255, 255)], [(-60,66), 40, (200,200,255)], [(-35,50), 40, (255,230,200)], [(0,34), 30, (200,200,255)], [(20,-6), 35, (255, 255, 255)], [(70,-10), 35, (200,200,255)], [(80, 25), 50, (255,230,200)]]

# set of pionts for small dipper
Small_dipper = [[(50, -10), 30, (255, 255, 255)], [(35,0), 20, (255,255,255)], [(20,8), 20, (255,230,230)], [(0,9), 20, (255,255,255)], [(-20,7), 25, (255,200,200)], [(-23,17), 20, (255,200,200)], [(-3,20), 20, (255,255,255)]]

# set up pen
pen = turtle.Turtle()
pen.penup()
pen.color('white')
pen.hideturtle()
pen.speed(0)

# draws the selected image
def draw_bg_shape(image, offsetX=0, offsetY=0, distance_scaler=1, brightness_scaler=1, scale = 1):
    for i in range(len(image)):
        turtle.tracer(0)
        pen.color(image[i][2])
        pen.goto((image[i][0][0]+offsetX) * distance_scaler * scale, (image[i][0][1]+offsetY) * distance_scaler * scale)
        pen.write(".", font=("Arial", int(image[i][1] * brightness_scaler * scale)))

# draws stars randomly
def draw_random_stars(amount = 200, scale = 1):
    for i in range(amount):
        stardata = [(random.randint(-740, 740) * scale, random.randint(-470, 470) * scale), random.randint(10, 35) * scale, random.choice([(255,255,255), (200,200,255), (255,230,200), (255, 200, 255)])]
        turtle.tracer(0)
        pen.color(stardata[2])
        pen.goto(stardata[0])
        pen.write(".", font=("Arial", int(stardata[1] * scale)))

# earases stars
def clear_sky():
    pen.clear()
