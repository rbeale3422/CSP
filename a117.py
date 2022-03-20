#   Add code to make turtles move in a circle and change colors.
import turtle as trtl

# create an empty list of turtles
my_turtles = []

# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic", "triangle", "square", "arrow", "turtle", "circle"]
turtle_colors = ["red", "blue", "green", "orange", "purple", "gold", "cyan", "magenta", "red", "blue", "green"]

for s in turtle_shapes:
  t = trtl.Turtle(shape=s)
  tcolor = turtle_colors.pop()
  t.fillcolor(tcolor)
  t.pencolor(tcolor)
  t.turtlesize(2)
  my_turtles.append(t)

#  set starting x,y coordinates for first turtle
startx = 0
starty = 0

# set starting turtle direction
direction = 90
distance_mod = 0

# loop through all turtle objects
for t in my_turtles:
  t.penup()
  t.goto(startx, starty)
  t.setheading(direction)
  t.pendown()
  t.right(45)   
  t.forward(50+distance_mod)
  distance_mod += 5

  # increment the x,y coordinates so the turtles are not drawn on each other
  startx = t.xcor()
  starty = t.ycor()
  direction = t.heading()

wn = trtl.Screen()
wn.mainloop()