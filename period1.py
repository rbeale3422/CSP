import tkinter as tk

root = tk.Tk()
root.title('Caesar Cipher')
root.geometry('600x600')
root.columnconfigure(1,weight=1)

# 1st row of information
message_label = tk.Label(
    root,
    text='Enter a message to encode:',
    font=('Arial 16 bold'),
    bg='red',
    fg='#FF0'
)
message_label.grid(row=0,column=0,sticky=(tk.W),padx=25)
message_var = tk.StringVar(root) # holds the text from message_input
message_input = tk.Entry(
    root,
    textvariable=message_var
)
message_input.grid(row=0,column=1,sticky=(tk.N,tk.E,tk.W,tk.S),padx=10)

# row 2
encoded_label = tk.Label(
    root,
    text='Your encoded message is here:',
    font=('Arial 16 bold'),
    bg='green',
    fg='white'
)
encoded_label.grid(row=1,column=0,sticky=(tk.W),padx=25)
encoded_var = tk.StringVar(root) # holds the text from message_input
encoded_input = tk.Entry(
    root,
    textvariable=encoded_var
)
encoded_input.grid(row=1,column=1,sticky=(tk.N,tk.E,tk.W,tk.S),padx=10)

# row 3
submit_btn = tk.Button(
    root,
    text='Encode'
)
submit_btn.grid(row=2,column=1,sticky=(tk.E),padx=10,pady=10)

root.mainloop()