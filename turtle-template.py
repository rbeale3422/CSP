import turtle as trtl

# create and setup screen object
wn = trtl.Screen()
wn.screensize(640,480)
wn.bgcolor('black')
wn.title("My Turtle Program")

# create and setup drawing turtle
painter = trtl.Turtle()
painter.color('white')
painter.shape('turtle')

wn.mainloop()
