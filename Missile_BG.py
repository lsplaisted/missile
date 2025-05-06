import turtle, random

screen = turtle.Screen()
screen.bgcolor('black')
screen.colormode(255)

# set of pionts for big dipper
Big_dipper = [[(-100,64), 40], [(-60,66), 40], [(-35,50), 40], [(0,34), 30], [(20,-6), 35], [(70,-10), 35], [(80, 25), 50]]

# set of pionts for small dipper
Small_dipper = ["TBD"]

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
        pen.goto((image[i][0][0]+offsetX) * distance_scaler * scale, (image[i][0][1]+offsetY) * distance_scaler * scale)
        pen.write(".", font=("Arial", int(image[i][1] * brightness_scaler * scale)))

# draws stars randomly
def draw_random_stars(amount = 200, scale = 1):
    for i in range(amount):
        stardata = [(random.randint(-770, 770) * scale, random.randint(-400, 400) * scale), random.randint(20, 40) * scale]
        turtle.tracer(0)
        pen.color(255,255,255)
        pen.goto(stardata[0])
        pen.write(".", font=("Arial", int(stardata[1] * scale)))

# earases stars
def clear_sky():
    pen.clear()
