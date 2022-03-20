from tkinter import *
from turtle import RawTurtle, TurtleScreen
# from PIL import ImageTk

# Game Variables
display_font = ('Verdana', 14, 'bold')

def go_up():
    painter.setheading(90)
    painter.forward(5)

def go_down():
    painter.setheading(270)
    painter.forward(5)

def go_left():
    painter.setheading(180)
    painter.forward(5)

def go_right():
    painter.setheading(0)
    painter.forward(5)

def reset_turtle():
    painter.reset()
    painter.color('red')
    painter.shape('turtle')

# create main window and divide that window into two parts (canvas x 2)
root = Tk()
root.geometry("800x600")
root.title('Game Program')
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=0)
root.columnconfigure(1, weight=1)

menu_canvas = Canvas(root, bg='black') # menu button section
menu_canvas.grid(row=0, column=0, sticky=(N,E,W,S))
bg_image = PhotoImage(file="brickwall.png")
drawing_canvas = Canvas(root, bg='gray') # area for turtle drawing
drawing_canvas.create_image(0, 0, image=bg_image, anchor='nw')
drawing_canvas.grid(row=0, column=1, sticky=(N,E,W,S))


# add menu buttons to menu_canvas

movement_label = Label(menu_canvas, text="Move", bg='black', fg='white', font=display_font)
movement_label.grid(row=0, columnspan=4, sticky=(E,W))

# up button
up_button = Button(menu_canvas, text='Up')
up_button.grid(row=1, column=1, padx=10, pady=10)
up_button.configure(command=go_up)

# left button
left_button = Button(menu_canvas, text='Lt')
left_button.grid(row=2, column=0, padx=10)
left_button.configure(command=go_left)

# right button
right_button = Button(menu_canvas, text='Rt')
right_button.grid(row=2, column=2, padx=10)
right_button.configure(command=go_right)

# down button
down_button = Button(menu_canvas, text='Dn')
down_button.grid(row=3, column=1, padx=10)
down_button.configure(command=go_down)

# reset button
reset_button = Button(menu_canvas, text='Reset')
reset_button.grid(row=99, column=1, pady=20)
reset_button.configure(command=reset_turtle)

game_area = TurtleScreen(drawing_canvas) # setup drawing_canvas for use with turtles
painter = RawTurtle(game_area) # create a new turtle
painter.color('red')
painter.shape('turtle')



root.mainloop()