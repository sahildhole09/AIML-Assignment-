import tkinter as tk

root = tk.Tk()

root.title("Area Of Circle")
root.geometry("350x280")

tk.Label(root,text="Calculate Area of Circle",
         font=("Times New Roman",17,"bold")).pack(pady=12)

tk.Label(root,text="Enter the Radius of Circle",
         font=("Times New Roman",12)).pack(pady=10)
entry = tk.Entry(root)
entry.pack(pady=10)

def CircleArea():
    PI = 3.14
    Radius = int(entry.get())

    AreaOfCircle = PI * (Radius)**2

    labelResult.config(text="Area Of Circle is : "+str(AreaOfCircle))

tk.Button(root,text="Calculate Area",command=CircleArea).pack(pady=10)

labelResult = tk.Label(root,text="",font=("Times New Roman",12))
labelResult.pack(pady=10)

root.mainloop()