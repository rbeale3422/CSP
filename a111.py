#Activity 1.1.1
#Created by Mr. Beale, MBA
#Created on 9/15/2021
#Created for Computer Science Principles

import turtle as trtl

#create a new turtle and name him Rob
Rob = trtl.Turtle()

#set Rob the turtle's attributes
Rob.shape("turtle") #a turtle ought to look like a turtle
Rob.color("#477CEC")
Rob.turtlesize(3)
Rob.pencolor("#477CEC")
Rob.pensize(5)

#create square (using a for loop to decrease code length)
for side in range(4):
    print("Now drawing side number " + str(side+1))
    Rob.forward(100)
    Rob.right(90)

#move turtle
Rob.penup()
Rob.goto(-100,100)
Rob.pendown()

#change color
Rob.color("red")
Rob.pencolor("red")

#create rectangle
Rob.forward(100)
Rob.right(90)
Rob.forward(120)
Rob.right(90)
Rob.forward(100)
Rob.right(90)
Rob.forward(120)
Rob.right(90)

#move turtle
Rob.penup()
Rob.goto(100,100)
Rob.pendown()

#change color
Rob.color("green")
Rob.pencolor("green")

#create a triangle
Rob.setheading(90)
Rob.forward(100)
Rob.right(135)
Rob.forward(150)
Rob.right(135)
Rob.forward(105)
#Rob.circle(75,None,3)

#move turtle
Rob.penup()
Rob.goto(150,-100)
Rob.pendown()

#change color
Rob.color("yellow")
Rob.pencolor("yellow")

#draw a circle
Rob.circle(75)

#don't mess with the screen stuff!
wn = trtl.Screen()
wn.mainloop()