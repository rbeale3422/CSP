import tkinter as tk

root = tk.Tk()
root.title('Program Title')
root.geometry('600x600')
root.columnconfigure(1,weight=1)

# 1st row
message_label = tk.Label(
    root,
    text='Enter message to encode:',
    font=('Arial 16 bold'),
    bg='red',
    fg='#FF0'
)
message_var = tk.StringVar(root)
message_input = tk.Entry(root,textvariable=message_var)
message_label.grid(row=0,column=0,sticky=(tk.E),padx=25)
message_input.grid(row=0,column=1,sticky=(tk.N,tk.S,tk.E,tk.W))

# 2nd row
encoded_label = tk.Label(
    root,
    text='Encoded message:',
    font=('Arial 16 bold'),
    bg='green',
    fg='white'
)
encoded_var = tk.StringVar(root)
encoded_input = tk.Entry(root,textvariable=encoded_var)
encoded_label.grid(row=1,column=0,sticky=(tk.E),padx=25)
encoded_input.grid(row=1,column=1,sticky=(tk.N,tk.S,tk.E,tk.W))

# 3rd row
submit_btn = tk.Button(root,text='Encode')
submit_btn.grid(row=2,column=1,sticky=(tk.E),padx=10,pady=10)

root.mainloop()