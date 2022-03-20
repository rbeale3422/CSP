from tkinter import *
from tkinter import ttk
import random

#method to obtain the values from the RGB scales and change canvas color
def set_color():
  r = red.get()
  g = green.get()
  b = blue.get()
  color_str = f'#{r:02x}{g:02x}{b:02x}'
  color_canvas.configure(bg=color_str)

#method called when red scale is changed to update the corresponding label and change canvas color
def r_update(r):
  r_label.configure(text='RED:' + str(hex(int(r))).upper())
  set_color()

#method called when green scale is changed to update the corresponding label and change canvas color
def g_update(g):
  g_label.configure(text='GREEN:' + str(hex(int(g))).upper())
  set_color()

#method called when blue scale is changed to update the corresponding label and change canvas color
def b_update(b):
  b_label.configure(text='BLUE:' + str(hex(int(b))).upper())
  set_color()

#method to copy color string to the system clipboard
def copytoclipboard():
  r = red.get()
  g = green.get()
  b = blue.get()
  color_str = f'#{r:02x}{g:02x}{b:02x}'
  
  root.clipboard_clear()
  root.clipboard_append(color_str.upper())

#create base window object and set initial properties
root = Tk()
root.geometry("400x200")
root.title("RGB Calculator")
# root.iconbitmap('rgb.ico')

#create frames to store other widgets
#mainframe holds the scales and their respective labels
#colorframe holds the RGB label, panel, and both buttons
mainframe = Frame(root)
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
colorframe = Frame(root)
colorframe.grid(column=1, row=0, sticky=(N,W,E,S))
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)

#set scale for each RGB element with value of 0 to 255
#set label and scale for red color
red_label = Label(mainframe, fg="red", text='RED').grid(row=1, column=1, sticky=(N,E,W,S))
red = Scale(mainframe, from_=0, to=255, orient=HORIZONTAL, command=r_update)
red.set(random.randrange(256)) #assign a random red value when starting program
red.grid(row=1, column=2, sticky=(N,E,W,S), columnspan=2)

#set label and scale for green color
green_label = Label(mainframe, fg="green", text='GREEN').grid(row=2, column=1, sticky=(N,E,W,S))
green = Scale(mainframe, from_=0, to=255, orient=HORIZONTAL, command=g_update)
green.set(random.randrange(256)) #assign a random green value when starting program
green.grid(row=2, column=2, sticky=(N,E,W,S), columnspan=2)

#set label and scale for blue color
blue_label = Label(mainframe, fg="blue", text='BLUE').grid(row=3, column=1, sticky=(N,E,W,S))
blue = Scale(mainframe, from_=0, to=255, orient=HORIZONTAL, command=b_update)
blue.set(random.randrange(256)) #assign a random blue value when starting program
blue.grid(row=3, column=2, sticky=(N,E,W,S), columnspan=2)

#display RGB values in Hex format above the color panel
r_label = Label(colorframe, font='courier 8', fg="red", text='RED:' + str(hex(red.get())))
r_label.grid(row=0, column=0)
g_label = Label(colorframe, font='courier 8', fg="green", text='GREEN:' + str(hex(green.get())))
g_label.grid(row=0, column=1)
b_label = Label(colorframe, font='courier 8', fg="blue", text='BLUE:' + str(hex(blue.get())))
b_label.grid(row=0, column=2)

#creat a canvas to display the color derived by the scales
color_canvas = Canvas(colorframe, height=125, width=125, bg='green', bd=5, relief=GROOVE)
color_canvas.grid(row=1, column=0, columnspan=3, sticky=(N,E,W,S))

#display button to copy and exit
btn_copy = Button(colorframe, text='Copy to Clipboard', anchor=E, command=copytoclipboard)
btn_copy.grid(row=2, column=0, columnspan=2, pady=5)
btn_exit = Button(colorframe, text='Exit', anchor=W, command=root.quit)
btn_exit.grid(row=2, column=2)

#create the loop that keeps the window open indefinitely
root.mainloop()