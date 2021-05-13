import turtle
import winsound

# Game Window
wn = turtle.Screen()
wn.title("Pong Game by FelipeS")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Score
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)  # 100, 20
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 1  # Every time it moves on the x axis is by 2 pixels.
ball.dy = -1

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 270)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 18, "normal"))

# Functions


def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)


# Keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_up, "W")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_a_down, "S")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")


# Main Game Loop
while True:
    wn.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound("bounce2.wav", winsound.SND_ASYNC)
    elif ball.ycor() < -280:
        ball.sety(-280)
        ball.dy *= -1
        winsound.PlaySound("bounce2.wav", winsound.SND_ASYNC)
    elif ball.xcor() > 385:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 18, "normal"))
        winsound.PlaySound("lose.wav", winsound.SND_ASYNC)
    elif ball.xcor() < -385:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 18, "normal"))
        winsound.PlaySound("lose.wav", winsound.SND_ASYNC)
    # Paddle and Ball Collisions
    if ball.xcor() > 330 and (ball.xcor() < 360) and (ball.ycor()) < paddle_b.ycor() + 50 and (
            paddle_b.ycor() - 50 < ball.ycor()):
        ball.setx(330)
        ball.dx *= -1
        winsound.PlaySound("bounce1.wav", winsound.SND_ASYNC)
    elif 335 < ball.xcor() < 365 and (ball.ycor()) < paddle_b.ycor() + 55 and (
            paddle_b.ycor() - 55 < ball.ycor()):
        ball.dy *= -1
        winsound.PlaySound("bounce1.wav", winsound.SND_ASYNC)
    elif ball.xcor() < -330 and (ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 50) and (
            paddle_a.ycor() - 50 < ball.ycor()):
        ball.setx(-330)
        ball.dx *= -1
        winsound.PlaySound("bounce1.wav", winsound.SND_ASYNC)
    elif -335 > ball.xcor() > -365 and (ball.ycor()) < paddle_a.ycor() + 55 and (
            paddle_a.ycor() - 55 < ball.ycor()):
        ball.dy *= -1
        winsound.PlaySound("bounce1.wav", winsound.SND_ASYNC)

    # Paddles Limit
    if paddle_a.ycor() + 50 > 300:
        paddle_a.sety(250)
        paddle_a_up()
        paddle_a_down()
        winsound.PlaySound("border.wav", winsound.SND_ASYNC)
    elif paddle_a.ycor() - 50 < -300:
        paddle_a.sety(-250)
        paddle_a_up()
        paddle_a_down()
        winsound.PlaySound("border.wav", winsound.SND_ASYNC)
    elif paddle_b.ycor() + 50 > 300:
        paddle_b.sety(250)
        paddle_b_up()
        paddle_b_down()
        winsound.PlaySound("border.wav", winsound.SND_ASYNC)
    elif paddle_b.ycor() - 50 < -300:
        paddle_b.sety(-250)
        paddle_b_up()
        paddle_b_down()
        winsound.PlaySound("border.wav", winsound.SND_ASYNC)

