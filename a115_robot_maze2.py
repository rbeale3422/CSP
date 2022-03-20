#   a115_robot_maze.py
import turtle as trtl
import time

#----- maze and turtle config variables
screen_h = 400
screen_w = 420
startx = -100
starty = -100
turtle_scale = 1.5

#------ robot commands
def move():
  robot.dot(10)
  robot.fd(50)

def turn_left():
  robot.speed(0)
  robot.lt(90)
  robot.speed(2)

#----- init screen
wn = trtl.Screen()
wn.setup(width=screen_w, height=screen_h)
robot_image = "robot.gif"
wn.addshape(robot_image)

#----- init robot
robot = trtl.Turtle(shape=robot_image)
robot.hideturtle()
robot.color("darkorchid")
robot.pencolor("darkorchid")
robot.penup()
robot.setheading(90)
robot.turtlesize(turtle_scale, turtle_scale)
robot.goto(startx, starty)
robot.speed(2)
robot.showturtle()

#---- TODO: change maze here
wn.bgpic("maze2.png") # other file names should be maze2.png, maze3.png

#---- TODO: begin robot movement here

# first robot run
# i = 0
# while i < 3: #move forward 3 spaces
#   move()
#   i += 1

# j = 0
# while j < 3: #turn right
#   turn_left()
#   j += 1

# k = 0
# while k < 2: #move forward 2 spaces
#   move()
#   k += 1

# # pause before running second run
# time.sleep(5)

# # reset robot to beginning
# robot.goto(startx,starty)

# # second robot run, nested
# i = 0
# while i < 2:
#   j = 0
#   while j < 3:# move forward 3 spaces
#     move()
#     j += 1
#   turn_left()
#   i += 1
# move() #move forward last space

#---- end robot movement 

wn.mainloop()
