<<<<<<< HEAD
from tkinter import *

root = Tk()
root.title('Program Title')
root.iconbitmap('c:/gui/icon.ico')
root.geometry('800x800')


root.mainloop()
=======
import turtle as trtl

# variables
wall_len = 25
path_width = 30
maze_size = 25

wn = trtl.Screen()
wn.screensize(500, 300, "black")
wn.title('Turtle Maze Game')

maze = trtl.Turtle()
maze.color('white')
maze.shape('turtle')

walls = 0
while walls < maze_size:
    maze.forward(wall_len)
    maze.left(90)

    wall_len += path_width
    walls += 1

maze.hideturtle()

wn.mainloop()
>>>>>>> e44f13d69a69dfcbb6acda863472f31a9f837cc8
