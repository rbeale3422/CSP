import turtle as trtl

# Initialize Turtle
rob = trtl.Turtle()
rob.speed('fastest')

# Function
def koch_curve(t, length, levels):
    if levels == 0:
      t.forward(length)
      return
    length /= 3.0
    koch_curve(t, length, levels - 1)
    t.left(60)
    koch_curve(t, length, levels - 1)
    t.right(120)
    koch_curve(t, length, levels - 1)
    t.left(60)
    koch_curve(t, length, levels - 1)


# draw snowflake
rob.fillcolor('white')
rob.begin_fill()
koch_curve(rob, 240, 4)
rob.setheading(90)
koch_curve(rob, 240, 4)
rob.setheading(180)
koch_curve(rob, 240, 4)
rob.setheading(270)
koch_curve(rob, 240, 4)
rob.setheading(90)
rob.end_fill()


wn = trtl.Screen()
wn.bgcolor('blue')
wn.mainloop()