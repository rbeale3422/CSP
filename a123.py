import turtle as trtl

#-----setup-----
apple_image = "apple.gif" # Store the file name of your shape
pear_image = "pear.gif"
background_image = "background.gif"

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image) # Make the screen aware of the new file
wn.addshape(pear_image)
wn.bgpic(background_image)

apple = trtl.Turtle()
pear = trtl.Turtle()
pear.hideturtle()
drawer = trtl.Turtle()
drawer.hideturtle()

#-----functions-----
# given a turtle, set that turtle to be shaped by the image file
def draw_apple(active_apple):
  active_apple.shape(apple_image)
  active_apple.color("white")
  active_apple.write("A", font=("Arial", 55, "bold"))
  wn.update()

# given a turtle, set that turtle to be shaped by the image
def draw_pear(active_pear):
    active_pear.shape(pear_image)
    wn.update()

def apple_fall(active_apple):
    active_apple.penup()
    active_apple.goto(active_apple.xcor(), active_apple.ycor() -160)
    active_apple.pendown()

def draw_an_A():
    drawer.color("blue")
    drawer.write("A", font=("Arial", 74, "bold"))

#-----function calls-----
draw_apple(apple)
#draw_an_A()
#apple_fall(apple)
#draw_pear(pear)

#wn.onkeypress(apple_fall, "a")
wn.listen()
wn.mainloop()