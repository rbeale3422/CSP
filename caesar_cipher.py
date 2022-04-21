"""GUI application that takes a message and encodes it"""
import tkinter as tk
from message_encode import Message # import my class module

def on_submit():
    """To be run when user submits the form"""
    message = message_var.get() # get the unencoded message from the input box
    message = message.lower() # make everything lower case for ease of program
    # if there is not a message in the input box, exit the function
    if message == '':
        return
    # create a new Message object and use it to encrypt the message
    my_message = Message(message, 4)
    encode_var.set(my_message.encrypted_message) # set encoded text to display in the encoded input box

def press_one():
    temp = encode_var.get()
    temp += '1'
    encode_var.set(temp)

# create window and set its size and characteristics
root = tk.Tk()
root.title('Caesar Cipher')
root.geometry('600x600')
root.columnconfigure(1,weight=1) # this causes the text input boxes to expand to fill the space

# 1st row for unencoded message
message_label = tk.Label(
    root,
    text='Enter message to encode:',
    font=('Arial 16 bold'),
    bg='red',
    fg='#FF0'
)
message_label.grid(row=0,column=0,sticky=(tk.W), padx=25)
message_var = tk.StringVar(root) # holds string from the unencoded input widget
message_input = tk.Entry(root,textvariable=message_var)
message_input.grid(row=0,column=1,sticky=(tk.N,tk.E,tk.W,tk.S),padx=10)

# 2nd row for encoded message
encoded_label = tk.Label(
    root,
    text='Encoded Message:',
    font=('Arial 16 bold'),
    bg='green',
    fg='#FF0'
)
encoded_label.grid(row=1,column=0,sticky=(tk.W), padx=25)
encode_var = tk.StringVar(root)
encoded_input = tk.Entry(root,textvariable=encode_var)
encoded_input.grid(row=1,column=1,sticky=(tk.N,tk.E,tk.W,tk.S), padx=10)

# 3rd row for button that initiates the conversion from plain message to encrypted message
encode_btn = tk.Button(root, text='Encode Text')
encode_btn.grid(row=2,column=1,sticky=(tk.E),padx=10,pady=10)
encode_btn.configure(command=on_submit) # calls the on_submit function

#4th row
example_btn = tk.Button(root,text='1',command=press_one)
example_btn.grid(row=4, column=0)

root.mainloop() # keeps window open