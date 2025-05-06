import turtle, random

screen = turtle.Screen()
screen.bgcolor('black')

# set of pionts for big dipper
Big_dipper = [[(-100,64), 40], [(-60,66), 40], [(-35,50), 40], [(0,34), 30], [(20,-6), 35], [(70,-10), 35], [(80, 25), 50]]

# set up pen
pen = turtle.Turtle()
pen.penup()
pen.color('white')
pen.hideturtle()
pen.speed(0)

# draws the selected image
def draw_bg_shape(image, offsetX=0, offsetY=0, distance_scaler=1, brightness_scaler=1):
    for i in range(len(image)):
        pen.goto((image[i][0][0]+offsetX) * distance_scaler, (image[i][0][1]+offsetY) * distance_scaler)
        pen.write(".", font=("Arial", image[i][1] * brightness_scaler))

draw_bg_shape(Big_dipper, 60, -40)
turtle.mainloop()