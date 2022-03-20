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
wn.mainloop()