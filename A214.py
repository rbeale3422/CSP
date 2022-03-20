import tkinter as tk

#function when login button is pressed
def test_my_button():
    entered_password = ent_password.get()
    lbl_auth_password.config(text=entered_password)
    frame_auth.tkraise()

#main window
root = tk.Tk()
root.wm_geometry("400x200")
root.title("Authorization")

frame_login = tk.Frame(root)
frame_login.grid(row=0, column=0, sticky="news")

lbl_username = tk.Label(frame_login, text='Username:')
#lbl_username.pack(padx=25) you can use either pack or grid but not both
lbl_username.grid(row=0, column=0) #could use column as well
ent_username = tk.Entry(frame_login, bd=3)
ent_username.grid(row=1, column=1)
lbl_password = tk.Label(frame_login, text="Password:")
lbl_password.grid(row=2, column=0)
ent_password = tk.Entry(frame_login, bd=3, show="*")
ent_password.grid(row=3, column=1)
btn_login = tk.Button(frame_login, text="Login", command=test_my_button)
btn_login.grid(row=4, column=1)

#create a second frame that will be displayed when user authenticates
frame_auth = tk.Frame(root)
frame_auth.grid(row=0, column=0, sticky="news")
lbl_auth_password = tk.Label(frame_auth)
lbl_auth_password.grid(row=0, sticky="news")

#bring login frame to the front of window
frame_login.tkraise()

root.mainloop()