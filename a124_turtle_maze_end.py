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

# Maze runner event handlers for changing directions
def go_up():
    maze_runner.setheading(90)

def go_down():
    maze_runner.setheading(270)

def go_left():
    maze_runner.setheading(180)

def go_right():
    maze_runner.setheading(0)

# Maze runner even handlers for moving turtle
def go_turtle():
    maze_runner.forward(1)

    # detect collisions between maze_runner and maze walls
    wn_canvas = wn.getcanvas()
    x,y = maze_runner.position()
    margin = 5
    items = wn_canvas.find_overlapping(x+margin, -y+margin, x-margin, -y-margin)

    # check if canvas is not empty
    if (len(items) > 0):
        # get property of lowest object (canvas)
        canvas_color = wn_canvas.itemcget(items[0], 'fill')
        if canvas_color == maze_wall_color:
            #stop game
            maze_runner.color('gray')
            wn.onkeypress(None, 'space')
            wn.onkeypress(None, 'Up')
            wn.onkeypress(None, 'w')
            return
    wn.ontimer(go_turtle, 15) # fires every 15 seconds


# game variable section
number_walls = 25
path_width = 20
wall_length = path_width
angle = 90
wall_thickness = 3
maze_wall_color = 'blue'
maze_runner_color = 'red'

# Initialize Maze Turtle
maze_writer = trtl.Turtle()
maze_writer.pensize(wall_thickness)
maze_writer.color(maze_wall_color)
maze_writer.speed('fastest')

# Initialize Runner Turtle
maze_runner = trtl.Turtle()
maze_runner.shape('turtle')
maze_runner.color(maze_runner_color)
maze_runner.penup()
maze_runner.goto(-50,25)
maze_runner.pendown()

# Draw Maze
for side in range(number_walls):
  wall_length += path_width

  if side > 4:
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

# move up with arrow or w key
wn.onkeypress(go_up, "Up")
wn.onkeypress(go_up, "w")

# move down with arrow or s key
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_down, "s")

# move left with arrow or a key
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_left, "a")

# move right with arrow or d key
wn.onkeypress(go_right, "Right")
wn.onkeypress(go_right, "d")

# move maze_runner with spacebar
wn.onkeypress(go_turtle, "space")

wn.listen() # begin listening for key events
wn.mainloop()