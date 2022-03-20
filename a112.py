# import turtle module
import turtle as trl
import random

def get_color():
  r = random.randrange(0,256,1)
  g = random.randrange(0,256,1)
  b = random.randrange(0,256,1)
  return  f'#{r:02x}{g:02x}{b:02x}'

# create turtle object and set his attributes or properties
marley = trl.Turtle()
marley.pencolor(get_color())
marley.pensize(5)
marley.fillcolor(get_color())

# move the turtle to another part of the screen
rand_x = random.randrange(-200,201,1)
rand_y = random.randrange(-200,201,1)
marley.penup()
marley.goto(rand_x,rand_y)
marley.pendown()

# add code here for a circle
marley.begin_fill()
marley.circle(50)
marley.end_fill()

# move the turtle to another part of the screen
rand_x = random.randrange(-200,201,1)
rand_y = random.randrange(-200,201,1)
marley.penup()
marley.goto(rand_x,rand_y)
marley.pendown()

# add code here for an arc
marley.pencolor(get_color())
marley.fillcolor(get_color())
marley.begin_fill()
marley.circle(100,180)
marley.end_fill()

# move the turtle to another part of the screen
rand_x = random.randrange(-200,201,1)
rand_y = random.randrange(-200,201,1)
marley.penup()
marley.goto(rand_x,rand_y)
marley.pendown()

# add code here for an arc that is greater than 90 degrees and has 3 or more steps
marley.pencolor(get_color())
marley.fillcolor(get_color())
marley.begin_fill()
marley.circle(100,random.randrange(91,360,1),random.randrange(3,11,1))
marley.end_fill()

# move the turtle to another part of the screen
rand_x = random.randrange(-200,201,1)
rand_y = random.randrange(-200,201,1)
marley.penup()
marley.goto(rand_x,rand_y)
marley.pendown()

# add code here to create a random polygon using the circle method
marley.pencolor(get_color())
marley.fillcolor(get_color())
marley.begin_fill()
marley.circle(100,360,random.randrange(3,11,1))
marley.end_fill()

# create screen object and make it persist
wn = trl.Screen()
wn.mainloop()