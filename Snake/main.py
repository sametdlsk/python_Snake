import turtle
import time
import random

speed = 0.08
window = turtle.Screen()
window.title('Snake')
window.bgcolor('darkturquoise')
window.setup(width=640, height=480)
window.tracer(0)

snakehead = turtle.Turtle()
snakehead.speed(0)
snakehead.shape("square")
snakehead.color("black")
snakehead.penup()
snakehead.goto(0, 100)
snakehead.direction = "stop"

food = turtle.Turtle()
food.speed()
food.shape("circle")
food.color("black")
food.penup()
food.goto(0, 0)
food.shapesize (0.60, 0.60)

tail =[]


def move():
    if snakehead.direction == 'up':
        y = snakehead.ycor()
        snakehead.sety(y + 20)
    if snakehead.direction == 'down':
        y = snakehead.ycor()
        snakehead.sety(y - 20)
    if snakehead.direction == 'right':
        x = snakehead.xcor()
        snakehead.setx(x + 20)
    if snakehead.direction == 'left':
        x = snakehead.xcor()
        snakehead.setx(x - 20)

def go_up():
    if snakehead.direction != "down":
        snakehead.direction = "up"

def go_down():
    if snakehead.direction != "up":
        snakehead.direction = "down"
def go_right():
    if snakehead.direction != "left":
        snakehead.direction = "right"
def go_left():
    if snakehead.direction != "right":
        snakehead.direction = "left"

window.listen()
window.onkey(go_up, "Up")
window.onkey(go_down, "Down")
window.onkey(go_right, "Right")
window.onkey(go_left, "Left")


while True:
    window.update()

    if snakehead.xcor() > 300 or snakehead.xcor() < -300 or snakehead.ycor() > 240 or snakehead.ycor() < -240:
        time.sleep(1)
        snakehead.goto(0,0)
        snakehead.direction = 'stop'

        for tail in tail:
            tail.goto(1000,1000)

        tail =[]
        speed = 0.08

    if snakehead.distance(food) <20:
        x = random.randint(-200, 200)
        y = random.randint(-200, 200)
        food.goto(x,y)

        tailnew= turtle.Turtle()
        tailnew.speed(0)
        tailnew.shape('square')
        tailnew.color('white')
        tailnew.penup()
        tail.append(tailnew)

    for i in range(len(tail) - 1, 0, -1):
        x = tail[i - 1].xcor()
        y = tail[i - 1].ycor()
        tail[i].goto(x,y)

    if len(tail) > 0:
        x = snakehead.xcor()
        y = snakehead.ycor()
        tail[0].goto(x, y)

    move()
    time.sleep(speed)
