from turtle import Turtle, Screen
import time
import random

# Variables
score = 0
h_score = 0

screen = Screen()
screen.bgcolor("green")
screen.title("Sname makes hsss")
screen.setup(width=600, height=600)
screen.tracer(False)

# Snake head and apple and score
head = Turtle("square")
head.color("black")
head.speed(0)
head.penup()
head.goto(0, 0)
head.direction = "stop"

apple = Turtle("circle")
apple.color("red")
apple.penup()
apple.goto(100, 100)

score_sign = Turtle("square")
score_sign.speed(0)
score_sign.color("white")
score_sign.penup()
score_sign.hideturtle()
score_sign.goto(0, 265)
score_sign.write(f"Score: {score}, Highest one: {h_score}", align="center", font=("Arial", 18))

body_parts = []

# Funx
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

def move_up():
    if head.direction != "down":
        head.direction = "up"

def move_down():
    if head.direction != "up":
        head.direction = "down"

def move_left():
    if head.direction != "right":
        head.direction = "left"

def move_right():
    if head.direction != "left":
        head.direction = "right"

# Keyboard input
screen.listen()
screen.onkeypress(move_up, "w")
screen.onkeypress(move_left, "a")
screen.onkeypress(move_down, "s")
screen.onkeypress(move_right, "d")

# Main cycle
while True:
    screen.update()

    # Colision / fail checker
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(2)
        head.goto(0 ,0)
        head.direction = "stop"

        # Hiding body_parts
        for one_body_part in body_parts:
            one_body_part.goto(1500, 1500)

        body_parts.clear()

        # Score reset
        score = 0
        score_sign.clear()
        score_sign.write(f"Score: {score}, Highest one: {h_score}", align="center", font=("Arial", 18))

    # Head / apple colision
    if head.distance(apple) < 20:
        x = random.randint(-14, 14) * 20
        y = random.randint(-14, 14) * 20
        apple.goto(x, y)

        # Adding body
        new_body_part = Turtle("square")
        new_body_part.speed(0)
        new_body_part.color("grey")
        new_body_part.penup()
        body_parts.append(new_body_part)

        # Score increase
        score += 10
        if score > h_score:
            h_score = score

        score_sign.clear()
        score_sign.write(f"Score: {score}, Highest one: {h_score}", align="center", font=("Arial", 18))

    for index in range(len(body_parts) - 1, 0, -1):
        x = body_parts[index - 1].xcor()
        y = body_parts[index - 1].ycor()
        body_parts[index].goto(x,y)

    if len(body_parts) > 0:
        x = head.xcor()
        y = head.ycor()
        body_parts[0].goto(x, y)

    move()

    # Head / body crash
    for one_body_part in body_parts:
        if one_body_part.distance(head) < 20:
            time.sleep(2)
            head.goto(0, 0)
            head.direction = "stop"

            for one_body_part in body_parts:
                one_body_part.goto(1500, 1500)

            body_parts = []

            score_sign.clear()
            score_sign.write(f"Score: {score}, Highest one: {h_score}", align="center", font=("Arial", 18))


    time.sleep(0.1)


screen.exitonclick()