# Turtle color names obtained from https://cs111.wellesley.edu/labs/lab01/colors

import turtle as trtl
import random as rand

def draw_door(pos):
  maze_writer.forward(pos)
  maze_writer.penup()
  maze_writer.forward(path_width*2)
  maze_writer.pendown()

def draw_barrier(pos):
  maze_writer.forward(pos)
  maze_writer.left(90)
  maze_writer.forward(path_width*2)
  maze_writer.backward(path_width*2)
  maze_writer.right(90)

# up = 90, down=270, right=0 and left=180
def go_up():
  maze_runner.setheading(90)

def go_down():
  maze_runner.setheading(270)

def go_left():
  maze_runner.setheading(180)

def go_right():
  maze_runner.setheading(0)

def go_turtle():
  maze_runner.forward(5)

# game variable section
number_walls = 25
path_width = 15
wall_length = path_width
angle = 90
wall_thickness = 3
colors = ['aquamarine', 'blue','CadetBlue', 'CornflowerBlue','cyan2',
          'DarkSlateGray2','DodgerBlue2', 'LightBlue','LightSeaGreen', 
          'LightSkyBlue4','PaleTurquoise1', 'PowderBlue','RoyalBlue2',
          'SteelBlue3','turquoise2']

# Initialize Turtle
maze_writer = trtl.Turtle()
maze_writer.pensize(wall_thickness)
maze_writer.color(rand.choice(colors)) # start with random color
maze_writer.speed('fastest')

maze_runner = trtl.Turtle()
maze_runner.color("red")
maze_runner.shape("turtle")
maze_runner.penup()
maze_runner.goto(-50, 30)
maze_runner.pendown()

# Draw Maze
for side in range(number_walls):
  wall_length += path_width
  maze_writer.color(rand.choice(colors)) # randomly change color from my list each iteration
  if side > 3:
    maze_writer.left(angle)

    # Randomize location of doors and barriers in wall
    door = rand.randint(path_width*2, (wall_length - path_width*2))
    barrier = rand.randint(path_width*2, (wall_length - path_width*2))
    # If door and barrier occur on top of each other, get a new value
    while abs(door-barrier)< path_width:
      door = rand.randint(path_width*2, (wall_length - path_width*2))

    if door < barrier:
      draw_door(door)
      draw_barrier(barrier - door - path_width*2)
      # draw remaining wall, subtracting barrier lengths already drawn
      maze_writer.forward(wall_length - barrier)

    else:
      draw_barrier(barrier)
      draw_door(door - barrier)
      # draw remaining wall, subtracting the door lengths already drawn
      maze_writer.forward(wall_length - door - path_width*2)

maze_writer.hideturtle() # hide turtle only leaving nice, clean maze drawing

# Create screen and keep it open listening for events
wn = trtl.Screen()

wn.onkeypress(go_up, "Up")
wn.onkeypress(go_up, "w")

wn.onkeypress(go_down, "Down")
wn.onkeypress(go_down, "s")

wn.onkeypress(go_left, "Left")
wn.onkeypress(go_left, "a")

wn.onkeypress(go_right, "Right")
wn.onkeypress(go_right, "d")

wn.onkeypress(go_turtle, "space")

wn.listen()
wn.mainloop()