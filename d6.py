import turtle as trtl
import random

# global list with six die face graphic file names
dice = ['d1.png', 'd2.png', 'd3.png', 'd4.png', 'd5.png', 'd6.png']
# global list for die rolls
rolls = []

# function that gets called from the onclick function (needs to take x,y even though we don't need)
def fnx(x,y):
  global dice
  global rolls
  
  die = random.randint(0,5) # roll the die
  if len(rolls) < 10:
    rolls.append(die+1) # add the results to the roll list
  else:
    pass

  #set screen background image based on die roll
  wn.bgpic(dice[die])
  # display all the die rolls up to this point
  label.clear()
  label.write(rolls, font=('Arial',18,'normal'))

# Create a turtle label to display die rolls (keeps history of results)
label = trtl.Turtle()
label.color('red')
label.penup()
label.goto(-250,-150) # set to bottom left-hand corner of screen
label.pendown()
label.hideturtle()

# setup the screen and set it to 600x400 pixels
wn = trtl.Screen()
wn.setup(600,400)

# set initial die roll
first_die = random.randint(0,5)
rolls.append(first_die+1)
label.write(rolls, font=('Arial',18,'normal')) # add first die roll to rolls list
wn.bgpic(dice[first_die]) # set appropriate picture using file names from dice list

# when user clicks on screen, roll another die, add the result to the label, and change background pic
wn.onclick(fnx)

# keep screen open until user closes it 
wn.mainloop()