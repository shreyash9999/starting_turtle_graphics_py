from turtle import Turtle, Screen

rambo = Turtle()
# rambo.forward(100)
# rambo.left(90)
# rambo.forward(100)
# rambo.left(90)
# rambo.forward(100)
# rambo.left(90)
# rambo.forward(100)

# for o in range(4):
#     rambo.forward(100)
#     rambo.left(90)
# o = True
# while o:
#     rambo.forward(5)
#     rambo.penup()
#     rambo.forward(5)
#     rambo.pendown()



def dot():

    for o in range(10):
        rambo.forward(5)
        rambo.penup()
        rambo.forward(5)
        rambo.pendown()



dot()


rambo.penup()
rambo.goto(0, -5)
rambo.pendown()
dot()

rambo.penup()
rambo.goto(0, -5)
rambo.pendown()
dot()
rambo.penup()
rambo.goto(0, -10)
rambo.pendown()
dot()
rambo.penup()
rambo.goto(0, -15)
rambo.pendown()
dot()
rambo.penup()
rambo.goto(0, -20)
rambo.pendown()
dot()
rambo.penup()
rambo.goto(0, -25)
rambo.pendown()
dot()



















screen = Screen()
screen.exitonclick()