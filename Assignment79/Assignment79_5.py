import tkinter as tk

root = tk.Tk()

root.title("Login Form")
root.geometry("350x350")

tk.Label(root,text="Login Form",
         font=("Arial",16,"bold")).pack(pady=20)

tk.Label(root,text="Enter Username",
         font=("Arial",10,"bold")).pack()
entry1 = tk.Entry(root)
entry1.pack(pady=8)

tk.Label(root,text="Enter Password",
         font=("Arial",10,"bold")).pack()
entry2 = tk.Entry(root)
entry2.pack(pady=8)

def Login():
    username = entry1.get()
    password = entry2.get()

    if username == "Ayush" and password == "ayush@123":
        labelResult.config(text="Login gets Successfully!")
    else:
        labelResult.config(text="Invalid Credentials! \nPlease enter valid username and password")

tk.Button(root,text="Login",command=Login).pack(pady=10)

labelResult = tk.Label(root,text="",font=("Arial",10,"bold"))
labelResult.pack(pady=10)

root.mainloop()