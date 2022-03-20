#   a116_buggy_image.py
import turtle as trtl

# create spider body 
spider = trtl.Turtle()
spider.pensize(40)
spider.speed('fastest')
spider.circle(20)

# function to move spider without drawing line
def move(x,y):
  spider.penup()
  spider.goto(x,y)
  spider.pendown()

# configure spider legs
num_legs = 8
leg_length = 50
angle = (360 / num_legs) - 25
spider.pensize(5)

# create spider head
spider.goto(0,-30)
spider.fillcolor('black')
spider.begin_fill()
spider.circle(20)
spider.end_fill()

# draw legs
leg = 0
radius = 60
while (leg < num_legs):
  spider.goto(0,20)
  if(leg < 4):
    spider.setheading(angle*leg + 125)
    spider.pendown()
    spider.circle(radius, 120)
    spider.penup()
  else:
    spider.setheading(angle*leg + 90)
    spider.pendown()
    spider.circle(radius, -120)
    spider.penup()
  leg = leg + 1

# draw eyes
spider.pensize(5)
spider.color("mediumpurple")
move(0,-15)
spider.circle(5)
move(10,-15)
spider.circle(5)

# draw violin
spider.fillcolor('red')
spider.color('red')
# print(spider.heading())
spider.setheading(300)
move(-5,20)
spider.begin_fill()
spider.circle(5,360,3)
move(4,40)
spider.setheading(120)
spider.circle(5,360,3)
spider.end_fill()


spider.hideturtle()

wn = trtl.Screen()
wn.mainloop()