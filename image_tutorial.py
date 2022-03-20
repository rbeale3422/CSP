from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("Image Display Program")

my_image = ImageTk.PhotoImage(Image.open("Beale Missy.jpg"))
img_label = Label(root, image=my_image )
img_label.pack()

button_quit = Button(root, text="Exit Program", command=root.quit)
button_quit.pack()

root.mainloop()