import turtle as trtl

def move_turtle(x:int, y:int):
    painter.penup()
    painter.goto(x,y)
    painter.pendown()

wn = trtl.Screen()
wn.bgcolor('gray')

# Initialize Turtle
painter = trtl.Turtle()
painter.pensize(10)
painter.pencolor('blue')

# spriral
width = 1.0
while width < 100.0:
    painter.fd(width)
    painter.right(10)
    width += 0.5

move_turtle(0,0)
painter.fillcolor('yellow')
painter.begin_fill()
painter.circle(200,360,3) # size, extent, and steps
painter.end_fill()


wn.mainloop()