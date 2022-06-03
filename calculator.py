import tkinter as tk

def update_display(value):
    temp = display_text.get()
    temp += value
    display_text.set(temp)

def clear_display():
    display_text.set('')

def calculate():
    pass

root = tk.Tk()
root.title('Calculator')
root.geometry('195x210')

# text entry across top of window
display_text = tk.StringVar(root)
display = tk.Entry(root, textvariable=display_text)
display.grid(row=0,column=0,columnspan=4,sticky=(tk.N, tk.S, tk.E, tk.W))

# 1st row: Clear, Div, Multiply, Blank
clear_btn = tk.Button(root,text='C',command=clear_display)
clear_btn.grid(row=1,column=0)
div_btn = tk.Button(root,text='/',command=lambda: update_display('/'))
div_btn.grid(row=1,column=1)
multi_btn = tk.Button(root,text='*',command=lambda: update_display('*'))
multi_btn.grid(row=1,column=2)

# 2nd row: 7,8,9,Subtract
seven_btn = tk.Button(root,text='7',command=lambda: update_display('7'))
seven_btn.grid(row=2,column=0)
eight_btn = tk.Button(root,text='8',command=lambda: update_display('8'))
eight_btn.grid(row=2,column=1)
nine_btn = tk.Button(root,text='9',command=lambda: update_display('9'))
nine_btn.grid(row=2,column=2)
subtract_btn = tk.Button(root,text='-',command=lambda: update_display('-'))
subtract_btn.grid(row=2,column=3)

# 3rd row: 4,5,6,Plus
four_btn = tk.Button(root,text='4',command=lambda: update_display('4'))
four_btn.grid(row=3,column=0)
five_btn = tk.Button(root,text='5',command=lambda: update_display('5'))
five_btn.grid(row=3,column=1)
six_btn = tk.Button(root,text='6',command=lambda: update_display('6'))
six_btn.grid(row=3,column=2)
plus_btn = tk.Button(root,text='+',command=lambda: update_display('+'))
plus_btn.grid(row=3,column=3)

# 4th row: 1,2,3,Equals (rowspan)
one_btn = tk.Button(root,text='1',command=lambda: update_display('1'))
one_btn.grid(row=4,column=0)
two_btn = tk.Button(root,text='2',command=lambda: update_display('2'))
two_btn.grid(row=4,column=1)
three_btn = tk.Button(root,text='3',command=lambda: update_display('3'))
three_btn.grid(row=4,column=2)
equals_btn = tk.Button(root,text='=',command=calculate)
equals_btn.grid(row=4,column=3,rowspan=2,sticky=(tk.N, tk.S, tk.E, tk.W))

# 5th row: 0(colspan2),period
zero_btn = tk.Button(root,text='0',command=lambda: update_display('0'))
zero_btn.grid(row=5,column=0,columnspan=2,sticky=(tk.N, tk.S, tk.E, tk.W))
period_btn = tk.Button(root,text='.',command=lambda: update_display('.'))
period_btn.grid(row=5,column=2)


root.mainloop()